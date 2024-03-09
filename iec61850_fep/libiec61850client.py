#!/usr/bin/env python3

import os,sys
import ctypes
import time
import lib61850
import logging

from urllib.parse import urlparse
from enum import Enum

class AddCause(Enum):
	ADD_CAUSE_UNKNOWN = 0
	ADD_CAUSE_NOT_SUPPORTED = 1
	ADD_CAUSE_BLOCKED_BY_SWITCHING_HIERARCHY = 2	# ot successful since one of the downstream Loc switches like in CSWI has the value TRUE
	ADD_CAUSE_SELECT_FAILED = 3 					# e.g. wrong ctlnum, or reserved by second client?
	ADD_CAUSE_INVALID_POSITION = 4					# cmdterm -
	ADD_CAUSE_POSITION_REACHED = 5					# if element was there allready
	ADD_CAUSE_PARAMETER_CHANGE_IN_EXECUTION = 6		# Control action is blocked due to running parameter change.
	ADD_CAUSE_STEP_LIMIT = 7						# tapchanger end pos
	ADD_CAUSE_BLOCKED_BY_MODE = 8					# if mod is set to local
	ADD_CAUSE_BLOCKED_BY_PROCESS = 9				# e.g. blocked by eehealth
	ADD_CAUSE_BLOCKED_BY_INTERLOCKING = 10			# blocked by interlocking
	ADD_CAUSE_BLOCKED_BY_SYNCHROCHECK = 11			# blocked by synchrocheck
	ADD_CAUSE_COMMAND_ALREADY_IN_EXECUTION = 12		# operate is ongoing
	ADD_CAUSE_BLOCKED_BY_HEALTH = 13				# blocked by health 
	ADD_CAUSE_1_OF_N_CONTROL = 14					# blocked by any of the relevant controls(stSeld of another related CSWI)
	ADD_CAUSE_ABORTION_BY_CANCEL = 15				# action is cancelled
	ADD_CAUSE_TIME_LIMIT_OVER = 16					# switch did not reach in time
	ADD_CAUSE_ABORTION_BY_TRIP = 17					# overridden control by trip
	ADD_CAUSE_OBJECT_NOT_SELECTED = 18				# not selected
	ADD_CAUSE_OBJECT_ALREADY_SELECTED = 19			# we had it allready
	ADD_CAUSE_NO_ACCESS_AUTHORITY = 20				# ...
	ADD_CAUSE_ENDED_WITH_OVERSHOOT = 21				# end position overshot
	ADD_CAUSE_ABORTION_DUE_TO_DEVIATION = 22		# diff between command and measured val
	ADD_CAUSE_ABORTION_BY_COMMUNICATION_LOSS = 23	# con loss
	ADD_CAUSE_ABORTION_BY_COMMAND = 24				# Control action is blocked due to the data attribute CmdBlk.stVal is TRUE.
	ADD_CAUSE_NONE = 25								# success
	ADD_CAUSE_INCONSISTENT_PARAMETERS = 26			# change in test/ctlnum between select/oper
	ADD_CAUSE_LOCKED_BY_OTHER_CLIENT = 27			# another client selected it

class IedClientError(Enum):
#     /* general errors */
#     /** No error occurred - service request has been successful */
    IED_ERROR_OK = 0
#     /** The service request can not be executed because the client is not yet connected */
    IED_ERROR_NOT_CONNECTED = 1
#     /** Connect service not execute because the client is already connected */
    IED_ERROR_ALREADY_CONNECTED = 2
#     /** The service request can not be executed caused by a loss of connection */
    IED_ERROR_CONNECTION_LOST = 3
#     /** The service or some given parameters are not supported by the client stack or by the server */
    IED_ERROR_SERVICE_NOT_SUPPORTED = 4
#     /** Connection rejected by server */
    IED_ERROR_CONNECTION_REJECTED = 5
#     /** Cannot send request because outstanding call limit is reached */
    IED_ERROR_OUTSTANDING_CALL_LIMIT_REACHED = 6
#     /* client side errors */
#     /** API function has been called with an invalid argument */
    IED_ERROR_USER_PROVIDED_INVALID_ARGUMENT = 10
    IED_ERROR_ENABLE_REPORT_FAILED_DATASET_MISMATCH = 11
#     /** The object provided object reference is invalid (there is a syntactical error). */
    IED_ERROR_OBJECT_REFERENCE_INVALID = 12
#     /** Received object is of unexpected type */
    IED_ERROR_UNEXPECTED_VALUE_RECEIVED = 13
#     /* service error - error reported by server */
#     /** The communication to the server failed with a timeout */
    IED_ERROR_TIMEOUT = 20
#     /** The server rejected the access to the requested object/service due to access control */
    IED_ERROR_ACCESS_DENIED = 21
#     /** The server reported that the requested object does not exist (returned by server) */
    IED_ERROR_OBJECT_DOES_NOT_EXIST = 22
#     /** The server reported that the requested object already exists */
    IED_ERROR_OBJECT_EXISTS = 23
#     /** The server does not support the requested access method (returned by server) */
    IED_ERROR_OBJECT_ACCESS_UNSUPPORTED = 24
#     /** The server expected an object of another type (returned by server) */
    IED_ERROR_TYPE_INCONSISTENT = 25
#     /** The object or service is temporarily unavailable (returned by server) */
    IED_ERROR_TEMPORARILY_UNAVAILABLE = 26
#     /** The specified object is not defined in the server (returned by server) */
    IED_ERROR_OBJECT_UNDEFINED = 27
#     /** The specified address is invalid (returned by server) */
    IED_ERROR_INVALID_ADDRESS = 28
#     /** Service failed due to a hardware fault (returned by server) */
    IED_ERROR_HARDWARE_FAULT = 29
#     /** The requested data type is not supported by the server (returned by server) */
    IED_ERROR_TYPE_UNSUPPORTED = 30
#     /** The provided attributes are inconsistent (returned by server) */
    IED_ERROR_OBJECT_ATTRIBUTE_INCONSISTENT = 31
#     /** The provided object value is invalid (returned by server) */
    IED_ERROR_OBJECT_VALUE_INVALID = 32
#     /** The object is invalidated (returned by server) */
    IED_ERROR_OBJECT_INVALIDATED = 33
#     /** Received an invalid response message from the server */
    IED_ERROR_MALFORMED_MESSAGE = 34
#     /** Service not implemented */
    IED_ERROR_SERVICE_NOT_IMPLEMENTED = 98
#     /** unknown error */
    IED_ERROR_UNKNOWN = 99


logger = logging.getLogger(__name__)

class iec61850client():

	def __init__(self, readvaluecallback = None, loggerRef = None, cmdTerm_cb = None, Rpt_cb = None):
		global logger
		if loggerRef != None:
			logger = loggerRef

		self.polling = {}
		self.connections = {}
		#callbacks, WARNING when a callback is called from a non-python created thread, socketio breaks..
		self.readvaluecallback = readvaluecallback
		self.cmdTerm_cb = cmdTerm_cb
		self.Rpt_cb = Rpt_cb

		self.cb_refs = [] # used to ensure the garbage collector does not clean up used callbacks
		self.reporting = {} # used on reconnect to reenable the rcb's


	@staticmethod
	def printValue(value):
		_type = lib61850.MmsValue_getTypeString(value)
		_type = str(_type)
		if _type == "boolean":
			return ("%r" % lib61850.MmsValue_getBoolean(value)), _type
		if _type == "array":
			return ("arr"), _type
		if _type ==  "bcd":
			return ("bcd"), _type
		if _type ==  "binary-time":
			return ("%i" % lib61850.MmsValue_getBinaryTimeAsUtcMs(value)), _type
		if _type == "bit-string":
			return ("%i" % lib61850.MmsValue_getBitStringAsInteger(value)), _type
		if _type == "access-error":
			return ("ACCESS ERROR"), _type
		if _type == "float":
			return ("%f" % lib61850.MmsValue_toFloat(value)), _type
		if _type == "generalized-time":
			return ("%u" % lib61850.MmsValue_toUnixTimestamp(value)), _type
		if _type == "integer":
			return ("%i" % lib61850.MmsValue_toInt64(value)), _type
		if _type == "oid":
			return ("OID ERROR"), _type
		if _type == "mms-string":
			return ("%s" % lib61850.MmsValue_toString(value).decode("utf-8")), _type
		if _type == "structure":
			return ("STRUCTURE"), _type
		if _type == "octet-string":
			len = lib61850.MmsValue_getOctetStringSize(value)
			buf = lib61850.MmsValue_getOctetStringBuffer(value)
			#magic cast to convert a swig pointer into a ctypes pointer, the int(buf) works, but why?
			buff = ctypes.cast(buf, ctypes.POINTER(ctypes.c_char))
			#allocate a buffer for the result
			res = bytearray(len)
			#create a pointer to the result buffer
			rptr = (ctypes.c_char * len).from_buffer(res)
			#copy the memory from the swig buffer to the result buffer
			ctypes.memmove(rptr, buff, len)
			return ("%s" % ''.join(format(x, '02x') for x in res)), _type
		if _type == "unsigned":
			return ("%u" % lib61850.MmsValue_toUint32(value)), _type
		if _type == "utc-time":
			return ("%u" % lib61850.MmsValue_getUtcTimeInMs(value)), _type
		if _type == "visible-string":
			return ("%s" % lib61850.MmsValue_toString(value).decode("utf-8")), _type
		if _type == "unknown(error)":
			return ("UNKNOWN ERROR"), _type
		return ("CANNOT FIND TYPE"), _type


	@staticmethod
	def printDataDirectory(con, doRef):
		tmodel = {}
		if doRef.find("/") == -1:
			logger.error("invalid datadirecory")
			return {}

		error = lib61850.IedClientError()
		dataAttributes = lib61850.IedConnection_getDataDirectoryFC(con, ctypes.byref(error), doRef)

		if error.value != 0:
			logger.error("could not get logical device list, error:%i" % error.value)

		if dataAttributes:
			dataAttribute = lib61850.LinkedList_getNext(dataAttributes)

			while dataAttribute:
				daName = ctypes.cast(lib61850.LinkedList_getData(dataAttribute),ctypes.c_char_p).value.decode("utf-8")
				daRef = doRef+"."+daName[:-4]
				fcName = daName[-3:-1]

				submodel = iec61850client.printDataDirectory(con,daRef)
				if submodel:
					tmodel[daName[:-4]] = submodel
					
				else:
					tmodel[daName[:-4]] = {}
					tmodel[daName[:-4]]['reftype'] = "DA"
					tmodel[daName[:-4]]['FC'] = fcName
					tmodel[daName[:-4]]['value'] = "UNKNOWN"
					#read DA
					fc = lib61850.FunctionalConstraint_fromString(fcName) 
					value = lib61850.IedConnection_readObject(con, ctypes.byref(error), daRef, fc)

					if error.value == 0:
						tmodel[daName[:-4]]['value'], tmodel[daName[:-4]]['type'] = iec61850client.printValue(value)
						lib61850.MmsValue_delete(value)

				dataAttribute = lib61850.LinkedList_getNext(dataAttribute)

			lib61850.LinkedList_destroy(dataAttributes)
		return tmodel


	@staticmethod
	def discovery(con):
		tmodel = {}

		error = lib61850.IedClientError()
		deviceList = lib61850.IedConnection_getLogicalDeviceList(con, ctypes.byref(error))

		if error.value != 0:
			logger.error("could not get logical device list, error:%i" % error.value)

		if deviceList:
			device = lib61850.LinkedList_getNext(deviceList)
			while device:
				LD_name=ctypes.cast(lib61850.LinkedList_getData(device),ctypes.c_char_p).value.decode("utf-8")
				tmodel[LD_name] = {}

				logicalNodes = lib61850.IedConnection_getLogicalDeviceDirectory(con, ctypes.byref(error), LD_name)
				if error.value != 0:#ret becomes int if connection is lost
					lib61850.LinkedList_destroy(deviceList)
					return model
					
				logicalNode = lib61850.LinkedList_getNext(logicalNodes)
				while logicalNode:
					LN_name=ctypes.cast(lib61850.LinkedList_getData(logicalNode),ctypes.c_char_p).value.decode("utf-8")
					tmodel[LD_name][LN_name] = {}

					#[LNobjects, error] = iec61850.IedConnection_getLogicalNodeVariables(con, LD_name+"/"+LN_name)
					LNobjects = lib61850.IedConnection_getLogicalNodeDirectory(con, ctypes.byref(error), LD_name+"/"+LN_name,lib61850.ACSI_CLASS_DATA_OBJECT)
					if error.value != 0:#ret becomes int if connection is lost
						lib61850.LinkedList_destroy(logicalNodes)
						lib61850.LinkedList_destroy(deviceList)
						return model

					LNobject = lib61850.LinkedList_getNext(LNobjects)
					while LNobject:
						Do = ctypes.cast(lib61850.LinkedList_getData(LNobject),ctypes.c_char_p).value.decode("utf-8")
						tmodel[LD_name][LN_name][Do] = {}

						doRef = LD_name+"/"+LN_name+"."+Do

						tmodel[LD_name][LN_name][Do] = iec61850client.printDataDirectory(con, doRef)

						LNobject = lib61850.LinkedList_getNext(LNobject)
					lib61850.LinkedList_destroy(LNobjects)

					LNdss = lib61850.IedConnection_getLogicalNodeDirectory(con, ctypes.byref(error), LD_name+"/"+LN_name, lib61850.ACSI_CLASS_DATA_SET)
					if error.value != 0:#ret becomes int if connection is lost
						lib61850.LinkedList_destroy(logicalNodes)
						lib61850.LinkedList_destroy(deviceList)
						return tmodel

					LNds = lib61850.LinkedList_getNext(LNdss)
					while LNds:

						DSname = ctypes.cast(lib61850.LinkedList_getData(LNds),ctypes.c_char_p).value.decode("utf-8")
						tmodel[LD_name][LN_name][DSname] = {}

						#
						isDel = ctypes.c_bool(False)
						dataSetMembers = lib61850.IedConnection_getDataSetDirectory(con, ctypes.byref(error), LD_name+"/"+LN_name+"."+DSname, ctypes.byref(isDel))  
						if error.value != 0:#ret becomes int if connection is lost
							lib61850.LinkedList_destroy(LNdss)
							lib61850.LinkedList_destroy(logicalNodes)
							lib61850.LinkedList_destroy(deviceList)
							return tmodel

						#all DS are assumed not deletable 
						if isDel == True:
							logger.info("  DS: %s, is Deletable" % DSname)
						else:
							logger.info("  DS: %s, not Deletable" % DSname)
						dataSetMemberRef = lib61850.LinkedList_getNext(dataSetMembers)

						i = 0
						while dataSetMemberRef:
							dsRef = ctypes.cast(lib61850.LinkedList_getData(dataSetMemberRef),ctypes.c_char_p).value.decode("utf-8")
							DX = dsRef[:-4]
							FC = dsRef[-3:-1]
							tmodel[LD_name][LN_name][DSname][str(i)] = {}
							tmodel[LD_name][LN_name][DSname][str(i)]['reftype'] = "DX"
							tmodel[LD_name][LN_name][DSname][str(i)]['type'] = "reference"
							tmodel[LD_name][LN_name][DSname][str(i)]['value'] = DX
							tmodel[LD_name][LN_name][DSname][str(i)]['FC'] = FC
							dataSetMemberRef = lib61850.LinkedList_getNext(dataSetMemberRef)
							i += 1
						lib61850.LinkedList_destroy(dataSetMembers)
						LNds = lib61850.LinkedList_getNext(LNds)

					lib61850.LinkedList_destroy(LNdss)


					LNrpp = lib61850.IedConnection_getLogicalNodeDirectory(con, ctypes.byref(error), LD_name+"/"+LN_name, lib61850.ACSI_CLASS_URCB)
					if error.value != 0:#ret becomes int if connection is lost
						lib61850.LinkedList_destroy(logicalNodes)
						lib61850.LinkedList_destroy(deviceList)
						return tmodel

					LNrp = lib61850.LinkedList_getNext(LNrpp)
					while LNrp:
						Rp = ctypes.cast(lib61850.LinkedList_getData(LNrp),ctypes.c_char_p).value.decode("utf-8")
						tmodel[LD_name][LN_name][Rp] = {}

						doRef = LD_name+"/"+LN_name+"."+Rp

						tmodel[LD_name][LN_name][Rp] = iec61850client.printDataDirectory(con, doRef)

						LNrp = lib61850.LinkedList_getNext(LNrp)
					lib61850.LinkedList_destroy(LNrpp)


					LNbrr = lib61850.IedConnection_getLogicalNodeDirectory(con, ctypes.byref(error), LD_name+"/"+LN_name, lib61850.ACSI_CLASS_BRCB)
					if error.value != 0:#ret becomes int if connection is lost
						lib61850.LinkedList_destroy(logicalNodes)
						lib61850.LinkedList_destroy(deviceList)
						return tmodel

					LNbr = lib61850.LinkedList_getNext(LNbrr)
					while LNbr:
						Br = ctypes.cast(lib61850.LinkedList_getData(LNbr),ctypes.c_char_p).value.decode("utf-8")
						tmodel[LD_name][LN_name][Br] = {}

						doRef = LD_name+"/"+LN_name+"."+Br

						tmodel[LD_name][LN_name][Br] = iec61850client.printDataDirectory(con, doRef)

						LNbr = lib61850.LinkedList_getNext(LNbr)
					lib61850.LinkedList_destroy(LNbrr)

					logicalNode = lib61850.LinkedList_getNext(logicalNode)

				lib61850.LinkedList_destroy(logicalNodes)
				device = lib61850.LinkedList_getNext(device)

			lib61850.LinkedList_destroy(deviceList)
		return tmodel


	@staticmethod
	def getMMsValue(typeVal, value, size=8, typeval = -1):
		#allocate mmsvalue based on type
		if typeVal == "visible-string" or typeval == lib61850.MMS_VISIBLE_STRING:
			return lib61850.MmsValue_newVisibleString(str(value))
		if typeVal == "boolean" or typeval == lib61850.MMS_BOOLEAN:
			if (type(value) is str and value.lower() == "true") or (type(value) is bool and value == True):
				return lib61850.MmsValue_newBoolean(True)
			else:
				return lib61850.MmsValue_newBoolean(False)
		if typeVal == "integer" or typeval == lib61850.MMS_INTEGER:
			return lib61850.MmsValue_newInteger(int(value))
		#untested
		if typeVal == "unsigned" or typeval == lib61850.MMS_UNSIGNED:
			return lib61850.MmsValue_newUnsignedFromUint32(int(value))
		if typeVal == "mms-string" or typeval == lib61850.MMS_STRING:
			return lib61850.MmsValue_newMmsString(str(value))
		if typeVal == "float" or typeval == lib61850.MMS_FLOAT:
			return lib61850.MmsValue_newFloat(float(value))
		if typeVal ==  "binary-time" or typeval == lib61850.MMS_BINARY_TIME:
			return lib61850.MmsValue_newBinaryTime(int(value))
		if typeVal == "bit-string" or typeval == lib61850.MMS_BIT_STRING:
			bs = lib61850.MmsValue_newBitString(size)
			return lib61850.MmsValue_setBitStringFromInteger(bs,int(value))
		if typeVal == "generalized-time" or typeval == lib61850.MMS_GENERALIZED_TIME:
			return lib61850.MmsValue_newUtcTimeByMsTime(int(value))
		if typeVal == "utc-time" or typeval == lib61850.MMS_UTC_TIME:
			return lib61850.MmsValue_newUtcTimeByMsTime(int(value))
		if typeVal == "octet-string" or typeval == lib61850.MMS_OCTET_STRING:
			sl = len(value)
			sptr = (ctypes.c_char * sl).from_buffer(value)

			buf = lib61850.MmsValue_newOctetString(sl,127)
			buff = ctypes.cast(int(buf), ctypes.POINTER(ctypes.c_char))

			ctypes.memmove(buff, sptr, sl)
			return buf
		#unsupported types
		if typeVal == "array" or typeval == lib61850.MMS_ARRAY:
			return None
		if typeVal ==  "bcd" or typeval == lib61850.MMS_BCD:
			return None
		if typeVal == "access-error" or typeval == lib61850.MMS_DATA_ACCESS_ERROR:
			return None
		if typeVal == "oid" or typeval == lib61850.MMS_OBJ_ID:
			return None
		if typeVal == "structure" or typeval == lib61850.MMS_STRUCTURE:
			return  None
		if typeVal == "unknown(error)":
			return None
		logger.error("Mms value type %s not supported" % typeVal)
		return None


	@staticmethod
	def writeValue(con, model, ref, value):
		submodel, path = iec61850client.parseRef(model,ref)

		if not submodel:
			logger.error("cannot find ref: %s in model" % ref)
			return {},-1
		if not 'FC' in submodel:
			logger.error("ref is not DA")
			return {},-1

		fc = lib61850.FunctionalConstraint_fromString(submodel['FC']) 
		mmsvalue = iec61850client.getMMsValue(submodel['type'],value)
		if not mmsvalue:
			return model,-1

		error = lib61850.IedClientError()
		lib61850.IedConnection_writeObject(con, ctypes.byref(error), ref, fc, mmsvalue)
		lib61850.MmsValue_delete(mmsvalue)
		if error.value == 0:
			model, err = iec61850client.updateValueInModel(con, model, ref)
			return model, err
		return model, error.value


	@staticmethod
	def updateValueInModel(con, model, ref):
		err = -1
		val, path = iec61850client.parseRef(model,ref)

		# recursive subfunction
		def update_recurse(con, submodel, path):
			err = -1
			if len(path) < 1:
				logger.error("recusion into model went wrong")
				err = -1
			elif len(path) == 1:
				if submodel[ path[0] ] and 'reftype' in submodel[ path[0] ] and submodel[ path[0] ]['reftype'] == 'DA':
					fcName = submodel[ path[0] ]['FC']
					#read DA
					fc = lib61850.FunctionalConstraint_fromString(fcName) 
					error = lib61850.IedClientError()
					value = lib61850.IedConnection_readObject(con, ctypes.byref(error), ref, fc)
					if error.value == 0:
						submodel[ path[0] ]['value'],  submodel[ path[0] ]['type'] = iec61850client.printValue(value)
						lib61850.MmsValue_delete(value)
						err = 0
					else:
						logger.error("could not read DA: %s from device" % ref)
						err = error.value

				else:
					submodel[ path[0] ] = iec61850client.printDataDirectory(con, ref)
					if submodel[ path[0] ]:# check if value or empty returned
						err = 0
					else:
						err = -1
			else:
				submodel[ path[0] ], err = update_recurse(con, submodel[ path[0] ], path[1:])
			return submodel, err

		#recurse the model
		model, err = update_recurse(con, model, path)
		return model, err


	@staticmethod
	def parseRef(model,ref):
		path = []
		if ref == "" or ref == None:
			return model, path
		
		_ref = ref.split("/")
		if len(_ref) == 1:
			path.append(ref)
			if ref in model:
				return model[ref], path
			else:
				logger.error("cannot find LD in model")
				return {}, []
		
		if len(_ref) > 2:
			logger.error("cannot parse ref, more than 1 '/' encountered ")
			return {}, []
		#one / encountered
		LD = _ref[0]
		path.append(LD)
		
		if not LD in model:
			logger.error("cannot find LD in model")
			return {}, []
		mm = model[LD]

		_ref = _ref[1].split(".")
		for i in range( len(_ref) ):
			path.append(_ref[i])

			if not _ref[i] in mm:
				logger.error("cannot find node in model: %s" % _ref[i])
				return {},[]

			mm = mm[ _ref[i] ]

		return mm, path


	@staticmethod
	def getRef(model,path):
		ref = ""
		mm = model
		for i in range( len(path) ):
			if not path[i] in mm:
				logger.error("cannot find node in model: %s in %s" % (path[i],ref))
				return ref, mm

			if i == 1:
				ref += "/"
			elif i > 1:
				ref += "."
			ref += path[i]
			mm = mm[ path[i] ]
		return ref, mm


	@staticmethod
	def printrefs(model, ref="", depth=0):
		_ref = ""
		for element in model:
			if depth == 0:
				_ref = element
			elif depth == 1:
				_ref = ref + "/" + element
			elif depth > 1:
				_ref = ref + "." + element
			if 'value' in model[element]:
				print(_ref + ":\t" + str(model[element]['value']))
			else:
				iec61850client.printrefs(model[element],_ref, depth + 1)


	# retrieve an active connection to IED, and up to date datamodel, stored in 'connections'
	def getIED(self, host, port):
		if port == "" or port == None:
			port = 102

		if host == None:
			logger.error("missing hostname")
			return -1

		tupl = host + ":" + str(port)
		if tupl in self.connections and self.connections[tupl]["con"] != None:
			if not self.connections[tupl]["model"]:
				con = self.connections[tupl]["con"]
				model = iec61850client.discovery(con)
				if model: #if model is not empty
					# store the model
					self.connections[tupl]["model"] = model
					return 0
				else:
					#we could not perform a discovery, so remove connection
					lib61850.IedConnection_destroy(con)
					self.connections[tupl]["con"] = None
					return -1
			else:
				#we have a connection and a model
				return 0
		
		if not tupl in self.connections:
			self.connections[tupl] = {}
			self.connections[tupl]["con"] = None
			self.connections[tupl]["model"] = {}

		con = lib61850.IedConnection_create()
		error = lib61850.IedClientError()
		lib61850.IedConnection_connect(con,ctypes.byref(error), host, port)
		if error.value == lib61850.IED_ERROR_OK:
			# store the active connection
			self.connections[tupl]["con"] = con
			# read the model
			model = iec61850client.discovery(con)
			if model: #if model is not empty
				# store the model
				self.connections[tupl]["model"] = model

				#reenable the rcb's if applicable
				if tupl in self.reporting and len(self.reporting[tupl]) > 0:
					for refdata in self.reporting[tupl]:
						rcb = refdata["rcb"]
						error = lib61850.IedClientError()
						rcb = lib61850.IedConnection_getRCBValues(con, ctypes.byref(error), refdata["RPT"], rcb)
						RptId = lib61850.ClientReportControlBlock_getRptId(rcb)
						lib61850.IedConnection_installReportHandler(con, refdata["RPT"], RptId, refdata["cbh"], id(refdata["refdata"]))

						lib61850.ClientReportControlBlock_setRptEna(rcb, True)
						lib61850.ClientReportControlBlock_setGI(rcb, True)
						lib61850.IedConnection_setRCBValues(con, ctypes.byref(error), rcb, lib61850.RCB_ELEMENT_RPT_ENA | lib61850.RCB_ELEMENT_GI, False)
						refdata["rcb"] = rcb

				return 0
			else:
				return -1
		else:
			lib61850.IedConnection_destroy(con)
			return -1


	def removeIED(self, host, port):
		if port == "" or port == None:
			port = 102

		if host == None:
			logger.error("missing hostname")
			return -1

		tupl = host + ":" + str(port)
		if tupl in self.connections and self.connections[tupl]["con"] != None:
			con = self.connections[tupl]["con"]
			error = lib61850.IedClientError()
			lib61850.IedConnection_abort(con,ctypes.byref(error))
			# This will close the MMS association by sending an ACSE abort message to the server. 
			# After sending the abort message the connection is closed immediately. 
			# The client can assume the connection to be closed when the function returns and the destroy method can be called. 
			# If the connection is not in "connected" state an IED_ERROR_NOT_CONNECTED error will be reported.
			#
			#remove connection
			lib61850.IedConnection_destroy(con)
			self.connections[tupl]["con"] = None
			return 0
		return -1


	# write a value to an active connection
	def registerWriteValue(self, ref, value):
		uri_ref = urlparse(ref)
		port = uri_ref.port
		if port == "" or port == None:
			port = 102

		if uri_ref.scheme != "iec61850":
			logger.error("incorrect scheme, only iec61860 is supported, not %s" % uri_ref.scheme)
			return -1

		if uri_ref.hostname == None:
			logger.error("missing hostname: %s" % ref)
			return -1

		tupl = uri_ref.hostname + ":" + str(port)

		#check if connection is active, or reconnect
		err = self.getIED(uri_ref.hostname, port)
		if err == 0:
			con = self.connections[tupl]['con']
			if not con:
				logger.error("no valid connection")
				return -1			

			model = self.connections[tupl]['model']
			if not model:
				logger.error("no valid model")
				return -1
			
			#todo:check if needed
			model, error = iec61850client.writeValue(con, model, uri_ref.path[1:], value)
			if error == 0:
				self.connections[tupl]['model'] = model
				submodel, path = iec61850client.parseRef(model,uri_ref.path[1:]) #get value from model via ref
				logger.debug("Value '%s' written to %s" % (str(submodel), ref) )

				if self.readvaluecallback != None:
					self.readvaluecallback(ref, submodel)

				return 0
			else:
				logger.error("could not write '%s' to %s with error: %i" % (str(value), ref, error))
				if error == 3: #we lost the connection
					lib61850.IedConnection_destroy(con)
					self.connections[tupl]['con'] = None
				return error
		else:
			logger.error("no connection to IED: %s:%s" % (uri_ref.hostname, port) )
		return -1


	# read a value from an active connection
	def ReadValue(self, ref):
		uri_ref = urlparse(ref)
		port = uri_ref.port
		if port == "" or port == None:
			port = 102

		if uri_ref.scheme != "iec61850":
			logger.error("incorrect scheme, only iec61860 is supported, not %s" % uri_ref.scheme)
			return {}, -1

		if uri_ref.hostname == None:
			logger.error("missing hostname: %s" % ref)
			return {}, -1

		tupl = uri_ref.hostname + ":" + str(port)


		#check if connection is active, or reconnect
		err = self.getIED(uri_ref.hostname, port)
		if err == 0:
			con = self.connections[tupl]['con']
			if not con:
				logger.error("no valid connection")
				return {}, -1			

			model = self.connections[tupl]['model']
			if not model:
				logger.error("no valid model")
				return {}, -1

			submodel, path = iec61850client.parseRef(model, uri_ref.path[1:])
			if submodel: #ref exists in model
				model, error = iec61850client.updateValueInModel(con, model, uri_ref.path[1:])
				if error == 0:
					self.connections[tupl]['model'] = model
					submodel, path = iec61850client.parseRef(model, uri_ref.path[1:])
					logger.debug("Value '%s' read from %s" % (str(submodel), ref) )

					if self.readvaluecallback != None:
						self.readvaluecallback(ref, submodel)

					return submodel, 0 
				else:
					logger.error("could not read '%s' with error: %i" % (ref, error))
					if error == 3: #we lost the connection
						lib61850.IedConnection_destroy(con)
						self.connections[tupl]['con'] = None
			else:
				logger.error("could not find %s in model" % uri_ref.path[1:])
		else:
			logger.error("no connection to IED: %s:%s" % (uri_ref.hostname, port) )
		return {}, -1

	def ReportHandler_cb(self, param, report):
		#parameter is dataset by ref.
		refdata = ctypes.cast(param, ctypes.py_object).value
		key = refdata[0]
		tupl = refdata[1]
		LD = refdata[2]
		LN = refdata[3]
		DSRef = refdata[4]

		a = lib61850.ClientReport_getRcbReference(report)
		b = lib61850.ClientReport_getRptId(report)
		reason = lib61850.ClientReport_getReasonForInclusion(report, 0)
		d = lib61850.ReasonForInclusion_getValueAsString(reason)
		#print("Callback: RTP received report for %s with rptId %s, DSRef %s and inclusion: %s" % ( a,b,DSRef,d ) )
		
		dataSetValues = lib61850.ClientReport_getDataSetValues(report)
		dataset = self.connections[tupl]['model'][LD][LN][DSRef]
		for index in dataset:
			reason = lib61850.ClientReport_getReasonForInclusion(report, int(index))
			if reason != lib61850.IEC61850_REASON_NOT_INCLUDED:
				mmsval = lib61850.MmsValue_getElement(dataSetValues, int(index))
				DaRef = dataset[index]['value']
				val, _type = iec61850client.printValue(mmsval)
				logger.debug(DaRef + ":" + val + "(" + _type + ")")

				submodel, _ = iec61850client.parseRef(self.connections[tupl]['model'],DaRef)
				submodel["value"] = val
				
				if self.Rpt_cb != None:
					self.Rpt_cb(key, submodel)


	def registerForReporting(self, key, tupl, ref):
		# check if present in dataset/report, and subscribe 
		LD = ""
		LN = ""
		DS = ""
		Idx = ""
		con = self.connections[tupl]['con']
		model = self.connections[tupl]['model']

		class BreakIt(Exception): pass

		try:
			for LD_name in model:
				for LN_name in model[LD_name]:
					for DSname in model[LD_name][LN_name]:
						if ( "0" in model[LD_name][LN_name][DSname] and 
								"reftype" in model[LD_name][LN_name][DSname]["0"] and 
								model[LD_name][LN_name][DSname]["0"]['reftype'] == "DX" ):
							for index in model[LD_name][LN_name][DSname]:
								if ref.startswith(model[LD_name][LN_name][DSname][index]['value']):
									logger.info("DATASET found! Ref:%s in DSref: %s" % (ref, model[LD_name][LN_name][DSname][index]['value']))
									logger.info("  DSRef:%s" % LD_name + "/" + LN_name + "." + DSname )
									LD = LD_name
									LN = LN_name
									DS = DSname
									Idx = index
									raise BreakIt
		except BreakIt:
			pass

		if Idx == "":
			logger.error("RPT: could not find dataset for ref: %s" % ref)
			return False

		for RP in model[LD][LN]:
			if "DatSet" in model[LD][LN][RP] and model[LD][LN][RP]["DatSet"]["value"] == LD + "/" + LN + "$" + DS:
				logger.info("RPT found! Ref:%s" % LD + "/" + LN + "." + RP)
				RPT = LD + "/" + LN + "." + model[LD][LN][RP]["DatSet"]["FC"] + "." + RP

				error = lib61850.IedClientError()
				if RPT in self.cb_refs:
					logger.info("RPT allready registered")
					rcb = lib61850.IedConnection_getRCBValues(con, ctypes.byref(error), RPT, None)
					if lib61850.ClientReportControlBlock_getRptEna(rcb):
						logger.info("RPT allready enabled")
					else:
						logger.info("RPT disabled")
					return True


				rcb = lib61850.IedConnection_getRCBValues(con, ctypes.byref(error), RPT, None)
				RptId = lib61850.ClientReportControlBlock_getRptId(rcb)

				cbh = lib61850.ReportCallbackFunction(self.ReportHandler_cb)

				refdata = [key, tupl, LD, LN, DS]
				refid = id(refdata) #model[LD][LN][DS])# bytes(str(LD + "/" + LN + "." + DS).encode('utf-8')) # ctypes.c_char_p( ref )
				lib61850.IedConnection_installReportHandler(con, RPT, RptId, cbh, refid)
				
				#lib61850.ClientReportControlBlock_setResv(rcb, True)
				if lib61850.ClientReportControlBlock_getRptEna(rcb) == True:
					logger.info("RPT allready enabled by another client")
					continue

				lib61850.ClientReportControlBlock_setRptEna(rcb, True)
				lib61850.ClientReportControlBlock_setGI(rcb, True)
				lib61850.IedConnection_setRCBValues(con, ctypes.byref(error), rcb, lib61850.RCB_ELEMENT_RPT_ENA | lib61850.RCB_ELEMENT_GI, True)

				self.cb_refs.append(RPT)


				#register rcb on this connection, so it can be enabled on a reconnect
				RcbData = {}
				RcbData["rcb"] = rcb
				RcbData["cbh"] = cbh # hard reference to ensure this pointer is not cleaned by the garbage collector
				RcbData["RPT"] = RPT # ref to report
				RcbData["refdata"] = refdata # hard ref to dataset

				if not tupl in self.reporting:
					self.reporting [tupl] = []
				self.reporting[tupl].append(RcbData)

				logger.info("RPT registered succesfull")
				return True
		logger.error("could not find report for dataset")
		return False

		


	# register value for reading
	def registerReadValue(self,ref):
		if ref in self.polling:
			logger.debug("reference: %s allready registered" % ref)
			return 0

		uri_ref = urlparse(ref)
		port = uri_ref.port
		if port == "" or port == None:
			port = 102


		if uri_ref.scheme != "iec61850":
			logger.error("incorrect scheme, only iec61860 is supported, not %s" % uri_ref.scheme)
			return -1

		if uri_ref.hostname == None:
			logger.error("missing hostname: %s" % ref)
			return -1

		tupl = uri_ref.hostname + ":" + str(port)

		#check if connection is active, or reconnect
		err = self.getIED(uri_ref.hostname, port)
		if err == 0:
			#only add an IED if it could be connected to
			con = self.connections[tupl]['con']
			model = self.connections[tupl]['model']
			#check if the ref exists in the model
			submodel, path = iec61850client.parseRef(model, uri_ref.path[1:])
			if submodel:
				rpt = self.registerForReporting(ref, tupl, uri_ref.path[1:])
				if rpt == False:
					# fallback to periodic poll when no report+dataset configured
					#if we allready have it in the list
					self.polling[ref] = 1
				#self.polling[ref] = 1
				return 0
			else:
				logger.error("could not find %s in model" % uri_ref.path[1:])
		else:
			logger.error("no connection to IED: %s:%s, ref:%s not registered" % (uri_ref.hostname, port, ref) )
		return -1


	# retrieve all registered values by polling
	def poll(self):
		for key in self.polling:
			uri_ref = urlparse(key)

			port = uri_ref.port
			if port == "" or port == None:
				port = 102


			if uri_ref.scheme != "iec61850":
				logger.error("incorrect scheme, only iec61860 is supported, not %s" % uri_ref.scheme)
				continue

			if uri_ref.hostname == None:
				logger.error("missing hostname: %s" % key)
				continue

			tupl = uri_ref.hostname + ":" + str(port)

			#check if connection is active, or reconnect
			err = self.getIED(uri_ref.hostname, port)
			if err == 0:
				con = self.connections[tupl]['con']
				model = self.connections[tupl]['model']
				if con and model:
					model, err = iec61850client.updateValueInModel(con, model, uri_ref.path[1:])
					if err == 0:
						self.connections[tupl]['model'] = model
						submodel, path = iec61850client.parseRef(model, uri_ref.path[1:])
						logger.debug("value:%s read from key: %s" % (str(submodel), key))
						#call function with ref+value
						if self.readvaluecallback != None:
							self.readvaluecallback(key, submodel)

					else:
						logger.error("model not updated for %s with error: %i" % (key, err))
						if err == 3: #we lost the connection
							lib61850.IedConnection_destroy(con)
							self.connections[tupl]['con'] = None
				else:
					logger.debug("no connection or model")

			else:
				logger.debug("IED not available for %s with error: %i" % (key, err))


	# retrieve datamodel from server
	def getDatamodel(self, ref=None, hostname="localhost", port=102):
		# if uri provided, it will have presedence over hostname and port
		if ref != None:
			uri_ref = urlparse(ref)
			hostname = uri_ref.hostname
			port = uri_ref.port

		# if port is explicitly defined as "" or None, assume 102
		if port == "" or port == None:
			port = 102

		err = self.getIED(hostname, port)
		if err == 0:
			tupl =  hostname + ":" + str(port)
			return self.connections[tupl]['model']
		else:
			logger.debug("no connection to IED: %s:%s" % (hostname, port) )
			return {}
	

	def getRegisteredIEDs(self):
		return self.connections


	def commandTerminationHandler_cb(self, param, con):
		#buff = ctypes.cast(param, ctypes.POINTER(ctypes.c_char))
		buff = ctypes.cast(param,ctypes.c_char_p).value.decode("utf-8")
		#logger.debug("commandTerminationHandler_cb called: %s", buff)
		lastApplError = lib61850.ControlObjectClient_getLastApplError(con)

		#/* if lastApplError.error != 0 this indicates a CommandTermination- */
		if self.cmdTerm_cb != None:
			if lastApplError.error != 0:
				addCause = AddCause(lastApplError.addCause).name
				self.cmdTerm_cb("object:%s Received CommandTermination-, LastApplError: %i, addCause: %s" % (buff, lastApplError.error, addCause))
			else:
				self.cmdTerm_cb("object:%s Received CommandTermination+" % buff)


	def get_controlObject(self, tupl, uri_ref):
		global logger
		control = None
		con = self.connections[tupl]['con']

		if not 'control' in self.connections[tupl]:
			self.connections[tupl]['control'] = {}

		if not uri_ref.path[1:] in self.connections[tupl]['control'] or self.connections[tupl]['control'][ uri_ref.path[1:] ] == None:

			control = lib61850.ControlObjectClient_create(uri_ref.path[1:], con)

			self.connections[tupl]['control'][ uri_ref.path[1:] ] = control

			ctlModel = lib61850.ControlObjectClient_getControlModel(control)
			if ctlModel == lib61850.CONTROL_MODEL_DIRECT_ENHANCED or ctlModel == lib61850.CONTROL_MODEL_SBO_ENHANCED:
				logger.info("control object: enhanced security")
				cbh = lib61850.CommandTerminationHandler(self.commandTerminationHandler_cb)

				ref = bytes(uri_ref.path[1:].encode('utf-8'))

				lib61850.ControlObjectClient_setCommandTerminationHandler(control, cbh, ctypes.c_char_p( ref ))
				self.cb_refs.append(cbh) # hard reference to ensure this pointer is not cleaned by the garbage collector
				self.cb_refs.append(ref)
			else:
				logger.info("control object: normal security")
		else:
			control = self.connections[tupl]['control'][ uri_ref.path[1:] ]
		return control


	def operate(self, ref, value):
		global logger
		error = -1
		addCause = ""

		if ref != None:
			uri_ref = urlparse(ref)
			hostname = uri_ref.hostname
			port = uri_ref.port

		# if port is explicitly defined as "" or None, assume 102
		if port == "" or port == None:
			port = 102
		
		err = self.getIED(hostname, port)
		if err == 0:
			tupl =  hostname + ":" + str(port)

			control = self.get_controlObject(tupl, uri_ref)
			
			lib61850.ControlObjectClient_setOrigin(control, "mmi", 3)
			mmsType = lib61850.ControlObjectClient_getCtlValType(control)
			ctlVal = iec61850client.getMMsValue("",value,0,mmsType)

			error = lib61850.ControlObjectClient_operate(control, ctlVal, 0)
			if error == 1:
				logger.info("operate: %s returned succesfull" % value)
			else:
				logger.error("operate: %s returned failed" % value)
				lastApplError = lib61850.ControlObjectClient_getLastApplError(control)
				addCause = AddCause(lastApplError.addCause).name
				logger.info("LastApplError: %i, addCause: %s" % ( lastApplError.error, addCause))

			#time.sleep(2)
			lib61850.MmsValue_delete(ctlVal)		
		return error, addCause

	def select(self, ref, value):
		global logger
		addCause = ""
		error = -1

		if ref != None:
			uri_ref = urlparse(ref)
			hostname = uri_ref.hostname
			port = uri_ref.port

		# if port is explicitly defined as "" or None, assume 102
		if port == "" or port == None:
			port = 102

		err = self.getIED(hostname, port)
		if err == 0:
			tupl =  hostname + ":" + str(port)
			
			control = self.get_controlObject(tupl, uri_ref)

			ctlModel = lib61850.ControlObjectClient_getControlModel(control)
			if ctlModel == lib61850.CONTROL_MODEL_SBO_NORMAL:
				logger.debug("SBO ctlmodel")
				error = lib61850.ControlObjectClient_select(control)
				if error == 1:
					logger.info("select: %s returned succesfull" % value)
				else:
					logger.error("select: %s returned failed" % value)
					lastApplError = lib61850.ControlObjectClient_getLastApplError(control)
					addCause = AddCause(lastApplError.addCause).name
					logger.error("LastApplError: %i, addCause: %s" % ( lastApplError.error, addCause))

			elif ctlModel == lib61850.CONTROL_MODEL_SBO_ENHANCED:
				logger.debug("SBOw ctlmodel")

				mmsType = lib61850.ControlObjectClient_getCtlValType(control)
				ctlVal = iec61850client.getMMsValue("",value,0,mmsType)
				lib61850.ControlObjectClient_setOrigin(control, "mmi", 3)
				error = lib61850.ControlObjectClient_selectWithValue(control, ctlVal)
				if error == 1:
					logger.info("select: %s returned succesfull" % value)
				else:
					logger.error("select: %s returned failed" % value)
					lastApplError = lib61850.ControlObjectClient_getLastApplError(control)
					addCause = AddCause(lastApplError.addCause).name
					logger.error("LastApplError: %i, addCause: %s" % ( lastApplError.error, addCause))

				#time.sleep(2)
				lib61850.MmsValue_delete(ctlVal)

			else:
				logger.error("cannot select object with ctlmodel: %i" % ctlModel)
				addCause = ("cannot select object with ctlmodel: %i" % ctlModel)
				error = -1

		return error, addCause

	def cancel(self, ref):
		error = -1

		if ref != None:
			uri_ref = urlparse(ref)
			hostname = uri_ref.hostname
			port = uri_ref.port

		# if port is explicitly defined as "" or None, assume 102
		if port == "" or port == None:
			port = 102

		err = self.getIED(hostname, port)
		if err == 0:
			tupl =  hostname + ":" + str(port)
			control = self.get_controlObject(tupl, uri_ref)
			error = lib61850.ControlObjectClient_cancel(control)

		return error



if __name__=="__main__":
	logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
		level=logging.DEBUG)
	# note the `logger` from above is now properly configured
	logger.debug("started")

	hostname = "localhost"
	tcpPort = 9102
	if len(sys.argv)>1:
		hostname = sys.argv[1]
	if len(sys.argv)>2:
		port = sys.argv[2]


	#error = lib61850.IedClientError()
	#con = lib61850.IedConnection_create()
	#lib61850.IedConnection_connect(con,ctypes.byref(error), hostname, tcpPort)
	#if (error.value == lib61850.IED_ERROR_OK):

	#	model = iec61850client.discovery(con)
		
	#	model, err = iec61850client.updateValueInModel(con, model, "IED3_SMVMUnn")
	#	print(err)
		#iec61850client.printrefs(val,"",len(path))


		#for key in model:
		#	logger.info("[" + model[key]['FC'] + "] " + model[key]['type'] + "\t" + key + "\t" + model[key]['value'])

		#for key in model:
		#	logger.error("[" + model[key]['FC'] + "] " + model[key]['type'] + "\t" + key + "\t" + model[key]['value'])
		#        /* Read RCB values */
		
		# rcb = lib61850.IedConnection_getRCBValues(con,ctypes.byref(error), "simpleIOGenericIO/LLN0.RP.EventsRCB01", None)

		# if error.value != lib61850.IED_ERROR_OK:
		# 	print("getRCBValues service error!")
		# 	exit()

		# #/* prepare the parameters of the RCP */
		# lib61850.ClientReportControlBlock_setResv(rcb, True)
		# lib61850.ClientReportControlBlock_setTrgOps(rcb, lib61850.TRG_OPT_DATA_CHANGED | lib61850.TRG_OPT_QUALITY_CHANGED | lib61850.TRG_OPT_GI)
		# lib61850.ClientReportControlBlock_setDataSetReference(rcb, "simpleIOGenericIO/LLN0$Events")
		# lib61850.ClientReportControlBlock_setRptEna(rcb, True)
		# lib61850.ClientReportControlBlock_setGI(rcb, True)
		# rptid = lib61850.ClientReportControlBlock_getRptId(rcb)

		# cbRef = lib61850.ReportCallbackFunction(cb)
		# lib61850.IedConnection_installReportHandler(con,"simpleIOGenericIO/LLN0.RP.EventsRCB",rptid,cbRef,None)
		# print("cb installed")
		# lib61850.IedConnection_setRCBValues(con,ctypes.byref(error), rcb, lib61850.RCB_ELEMENT_RESV | lib61850.RCB_ELEMENT_DATSET | lib61850.RCB_ELEMENT_TRG_OPS | lib61850.RCB_ELEMENT_RPT_ENA | lib61850.RCB_ELEMENT_GI, True)
		# print("setRCB called")
		# if error.value != lib61850.IED_ERROR_OK:
		# 	print("setRCBValues service error!")

		# time.sleep(1)

		# #/* Trigger GI Report */
		# lib61850.ClientReportControlBlock_setGI(rcb, True)
		# lib61850.IedConnection_setRCBValues(con,ctypes.byref(error), rcb, lib61850.RCB_ELEMENT_GI, True)
		# print("gi send, waiting 5 sec.")
		# if error.value != lib61850.IED_ERROR_OK:
		# 	print("Error triggering a GI report (code: %i)"% err)
		
		# time.sleep(5)

	#	lib61850.IedConnection_close(con)
	#else:
	#	logger.error("Failed to connect to %s:%i\n"%(hostname, tcpPort))
	#lib61850.IedConnection_destroy(con)

	cl = iec61850client()
	model = cl.getDatamodel(None,'localhost',102)
	cl.printrefs(model)

	#err = cl.registerReadValue("iec61850://127.0.0.1:9102/IED3_SMVMUnn/MMXU2.AvAPhs")
	#err = cl.registerReadValue("iec61850://127.0.0.1:9102/IED3_SMVMUnn/MMXU2.AvPhVPhs.mag.f")
	#err = cl.registerReadValue("iec61850://127.0.0.1:9102/IED3_SMVMUnn/TCTR1.Amp")
	#err = cl.registerReadValue("iec61850://127.0.0.1:9102/IED3_SMVMUnn/TCTR2.Amp.instMag.i")

	#err = cl.registerWriteValue("iec61850://127.0.0.1:9102/IED3_SMVMUnn/LLN0.MSVCB01.SvEna",True)
	#while True:
	#cl.poll()
	#cl.registerWriteValue("iec61850://127.0.0.1:9102/IED3_SMVMUnn/LLN0.MSVCB01.SvEna",False)
	#time.sleep(0.719)
	#cl.poll()
	#cl.registerWriteValue("iec61850://127.0.0.1:9102/IED3_SMVMUnn/LLN0.MSVCB01.SvEna",True)
	error = cl.select("iec61850://127.0.0.1:102/IED1_XCBRGenericIO/CSWI2.Pos", "True")
	if error == 1:
		print("selected successfully")
	else:
		print("failed to select")	
	#control = None
	if cl.operate("iec61850://127.0.0.1:102/IED1_XCBRGenericIO/CSWI2.Pos", "True") == 1:
		print("operated successfully")
	else:
		print("failed to operate")
	
	error = cl.select("iec61850://127.0.0.1:102/IED1_XCBRGenericIO/CSWI1.Pos", "True")
	if error == 1:
		print("selected successfully")
	else:
		print("failed to select")	
	#control = None
	if cl.operate("iec61850://127.0.0.1:102/IED1_XCBRGenericIO/CSWI1.Pos", "True") == 1:
		print("operated successfully")
	else:
		print("failed to operate")

