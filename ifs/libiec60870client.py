#!/usr/bin/env python3
from lib60870 import *
from urllib.parse import urlparse
import time

class IEC60870_5_104_client:
    # Connection event handler 
    def connectionHandler (self, parameter, connection, event):
        tupl = ctypes.cast(parameter, ctypes.py_object).value
        if event == CS104_CONNECTION_OPENED:
            print("Connection established")
            self.connections[tupl]['state'] = 1
        elif event == CS104_CONNECTION_CLOSED:
            print("Connection closed")
            self.connections[tupl]['state'] = 0
        elif event == CS104_CONNECTION_STARTDT_CON_RECEIVED:
            print("Received STARTDT_CON")
            self.connections[tupl]['state'] = 2
        elif event == CS104_CONNECTION_STOPDT_CON_RECEIVED:
            print("Received STOPDT_CON")
            self.connections[tupl]['state'] = 1


    #CS101_ASDUReceivedHandler implementation
    #For CS104 the address parameter has to be ignored
    def asduReceivedHandler (self, parameter, address, asdu):
        data = {}
        tupl = ctypes.cast(parameter, ctypes.py_object).value
        if not tupl in self.connections:
            print("error: cannot find %s in connections" % str(tupl))
            return False

        print("RECVD ASDU type: %s(%i) elements: %i" % (
            TypeID_toString(CS101_ASDU_getTypeID(asdu)),
            CS101_ASDU_getTypeID(asdu),
            CS101_ASDU_getNumberOfElements(asdu)
        ))

        if CS101_ASDU_getTypeID(asdu) == C_IC_NA_1:
            self.connections[tupl]['GI'] = True

        if (CS101_ASDU_getTypeID(asdu) == M_ME_TE_1):

            print("  measured scaled values with CP56Time2a timestamp:")

            for i in range(CS101_ASDU_getNumberOfElements(asdu)):

                io = cast(CS101_ASDU_getElement(asdu, i), MeasuredValueScaledWithCP56Time2a) 
                ioa = InformationObject_getObjectAddress(cast(io, InformationObject) )
                value = MeasuredValueScaled_getValue(cast(io, MeasuredValueScaled) )
                print("    IOA: %i value: %i" % (ioa,value ))
                self.connections[tupl]['data'][ioa] = {'value': value, 'ASDU': M_ME_TE_1}
                data[ioa] = {'value': value, 'ASDU': M_ME_TE_1}
                MeasuredValueScaledWithCP56Time2a_destroy(io)

        elif (CS101_ASDU_getTypeID(asdu) == M_SP_NA_1):
            print("  single point information:")

            for i in range(CS101_ASDU_getNumberOfElements(asdu)):

                io = cast(CS101_ASDU_getElement(asdu, i), SinglePointInformation) 
                ioa = InformationObject_getObjectAddress(cast(io,InformationObject) )
                value = SinglePointInformation_getValue(cast(io,SinglePointInformation) )
                print("    IOA: %i value: %i" % (ioa,value ))
                self.connections[tupl]['data'][ioa] = {'value': value, 'ASDU': M_SP_NA_1}
                data[ioa] = {'value': value, 'ASDU': M_SP_NA_1}
                SinglePointInformation_destroy(io)
        elif (CS101_ASDU_getTypeID(asdu) == M_DP_NA_1):
            print("  double point information:")

            for i in range(CS101_ASDU_getNumberOfElements(asdu)):

                io = cast(CS101_ASDU_getElement(asdu, i), DoublePointInformation)
                ioa = InformationObject_getObjectAddress(cast(io,InformationObject) ) 
                value = DoublePointInformation_getValue(cast(io,DoublePointInformation) )
                print("    IOA: %i value: %i" % (ioa,value ))
                self.connections[tupl]['data'][ioa] = {'value': value, 'ASDU': M_DP_NA_1}
                data[ioa] = {'value': value, 'ASDU': M_DP_NA_1}
                DoublePointInformation_destroy(io)
        elif (CS101_ASDU_getTypeID(asdu) == M_ME_NB_1):
            print("  measured value scaled:")

            for i in range(CS101_ASDU_getNumberOfElements(asdu)):

                io = cast(CS101_ASDU_getElement(asdu, i), MeasuredValueScaled) 
                ioa = InformationObject_getObjectAddress(cast(io,InformationObject) )
                value = MeasuredValueScaled_getValue(cast(io,MeasuredValueScaled) )
                print("    IOA: %i value: %i" % (ioa,value ))
                self.connections[tupl]['data'][ioa] = {'value': value, 'ASDU': M_ME_NB_1}
                data[ioa] = {'value': value, 'ASDU': M_ME_NB_1}
                MeasuredValueScaled_destroy(io)     
        elif (CS101_ASDU_getTypeID(asdu) == C_SC_NA_1):
            print("received single command response")
            for i in range(CS101_ASDU_getNumberOfElements(asdu)):

                io = cast(CS101_ASDU_getElement(asdu, i), SinglePointInformation) 
                ioa = InformationObject_getObjectAddress(cast(io,InformationObject) )
                value = SinglePointInformation_getValue(cast(io,SinglePointInformation) )
                print("    IOA: %i value: %i" % (ioa,value ))
                self.connections[tupl]['data'][ioa] = {'value': value, 'ASDU': C_SC_NA_1}
                data[ioa] = {'value': value, 'ASDU': C_SC_NA_1}
                SinglePointInformation_destroy(io)

        elif (CS101_ASDU_getTypeID(asdu) == C_DC_NA_1):
            print("received double command response")
            for i in range(CS101_ASDU_getNumberOfElements(asdu)):

                io = cast(CS101_ASDU_getElement(asdu, i), DoublePointInformation) 
                ioa = InformationObject_getObjectAddress(cast(io,InformationObject) )
                value = DoublePointInformation_getValue(cast(io,DoublePointInformation) )
                print("    IOA: %i value: %i" % (ioa,value ))
                self.connections[tupl]['data'][ioa] = {'value': value, 'ASDU': C_DC_NA_1}
                data[ioa] = {'value': value, 'ASDU': C_DC_NA_1}
                DoublePointInformation_destroy(io)

        elif (CS101_ASDU_getTypeID(asdu) == C_TS_TA_1):
            self.connections[tupl]['testfr_received'] += 1
            print("  received test command with timestamp. send: %i, received: %i" % (self.connections[tupl]['testfr_send'],self.connections[tupl]['testfr_received']))
            return True

        if self.callback != None and len(data) > 0:
            self.callback(tupl, data)
        return True


    def __init__(self, callback):
        self.connections = {}
        self.timeout = 2
        self.callback = callback
        self.p_connectionHandler = CS104_ConnectionHandler(self.connectionHandler)
        self.p_asduReceivedHandler = CS101_ASDUReceivedHandler(self.asduReceivedHandler)



    # retrieve an active connection to an RTU, and up to date datamodel, stored in 'connections'
    def getRTU(self, host, port):
        if port == "" or port == None:
            port = 2404

        if host == None:
            print("missing hostname")
            return -1

        tupl = host + ":" + str(port)
        if tupl in self.connections and self.connections[tupl]["con"] != None:
            if self.connections[tupl]["GI"] == False:
                con = self.connections[tupl]["con"]
                if CS104_Connection_sendInterrogationCommand(con, CS101_COT_ACTIVATION, 1, IEC60870_QOI_STATION) == False:
                    print("error: could not send GI")
                    CS104_Connection_sendStopDT(con)
                    CS104_Connection_destroy(con)
                    self.connections[tupl]["con"] = None
                    self.connections[tupl]["state"] = 0
                    return -1

                counter = 0
                while self.connections[tupl]["GI"] == False and counter < self.timeout: 
                    counter += 1
                    time.sleep(1)
                if self.connections[tupl]["GI"] == True:
                    return 0
                else:
                    CS104_Connection_sendStopDT(con)
		            #we could not perform a GI, so remove connection
                    CS104_Connection_destroy(con)
                    self.connections[tupl]["con"] = None
                    self.connections[tupl]["state"] = 0
                    return -1
            else:
		#we have a connection and a model
                return 0
		
        if not tupl in self.connections or self.connections[tupl]["con"] == None:
            self.connections[tupl] = {}
            self.connections[tupl]["con"] = None
            self.connections[tupl]["GI"] = False
            self.connections[tupl]["data"] = {}
            self.connections[tupl]["state"] = 0
            self.connections[tupl]['testfr_received'] = 0
            self.connections[tupl]['testfr_send'] = 0
            self.connections[tupl]['self'] = tupl

            con = CS104_Connection_create(host, port)
            if CS104_Connection_connect(con) == False:
                print("error: could not connect")
                CS104_Connection_destroy(con)
                return -1

            if CS104_Connection_sendStartDT(con) == False:
                print("error: could not send startDT")
                CS104_Connection_destroy(con)
                return -1

            CS104_Connection_setConnectionHandler(con, self.p_connectionHandler, id(self.connections[tupl]['self']))
            CS104_Connection_setASDUReceivedHandler(con, self.p_asduReceivedHandler, id(self.connections[tupl]['self']))

            counter = 0
            while self.connections[tupl]["state"] == 0 and counter < self.timeout: 
                counter += 1
                time.sleep(1)

            if self.connections[tupl]["state"] == 2:
                # read the model
                if CS104_Connection_sendInterrogationCommand(con, CS101_COT_ACTIVATION, 1, IEC60870_QOI_STATION) == False:
                    print("error: could not send GI")
                    CS104_Connection_sendStopDT(con)
                    CS104_Connection_destroy(con)
                    self.connections[tupl]["state"] = 0
                    return -1

                # store the active connection
                self.connections[tupl]["con"] = con
                counter = 0
                while self.connections[tupl]["GI"] == False and counter < self.timeout: 
                    counter += 1
                    time.sleep(1)
                if self.connections[tupl]["GI"] == True:
                    return 0
            else:
                CS104_Connection_sendStopDT(con)
                CS104_Connection_destroy(con)
                self.connections[tupl]["state"] = 0
                self.connections[tupl]["con"] = None
            return -1


    def parseref(self,ref):
        uri_ref = urlparse(ref)
        port = uri_ref.port
        if port == "" or port == None:
            port = 2404

        if uri_ref.scheme != "iec60870-5-104":
            print("incorrect scheme, only iec60870-5-104 is supported, not %s" % uri_ref.scheme)
            return None

        if uri_ref.hostname == None:
            print("missing hostname: %s" % ref)
            return None

        tupl = uri_ref.hostname + ":" + str(port)

        #check if connection is active, or reconnect
        err = self.getRTU(uri_ref.hostname, port)
        if err == 0:
            con = self.connections[tupl]['con']
            if not con:
                print("no valid connection")
                return None		

            model = self.connections[tupl]['data']
            if not model:
                print("no valid model")
                return None
			
            _ref = uri_ref.path[1:].split("/")
            type = _ref[0]
            ioa = _ref[1]
            return {"RTU":self.connections[tupl], "type":type, "ioa":int(ioa) }


    def select(self,ref, value):
        obj = self.parseref(ref) 
        if obj != None:
            ca = 1 # common address
            if obj['type'] == "SinglePointCommand":
                dc = cast(SingleCommand_create(None, obj['ioa'], value, True, 0), InformationObject)
                print("Send select command C_SC_NA_1")
            elif obj['type'] == "DoublePointCommand":
                dc = cast(DoubleCommand_create(None, obj['ioa'], value, True, 0), InformationObject)
                print("Send select command C_DC_NA_1")
            else:
                return 0

            CS104_Connection_sendProcessCommandEx(obj["RTU"]["con"], CS101_COT_ACTIVATION, ca, dc)
            InformationObject_destroy(dc)
            return 1
        return 0


    def operate(self,ref, value):
        obj = self.parseref(ref) 
        if obj != None:
            ca = 1 # common address
            if obj['type'] == "SinglePointCommand":
                dc = cast(SingleCommand_create(None, obj['ioa'], value, False, 0), InformationObject)
                print("Send operate command C_SC_NA_1")
            elif obj['type'] == "DoublePointCommand":
                dc = cast(DoubleCommand_create(None, obj['ioa'], value, False, 0), InformationObject)
                print("Send operate command C_DC_NA_1")
            else:
                return 0

            CS104_Connection_sendProcessCommandEx(obj["RTU"]["con"], CS101_COT_ACTIVATION, ca, dc)
            InformationObject_destroy(dc)
            return 1
        return 0

    def testframe(self, host, port):
        if port == "" or port == None:
            port = 2404

        if host == None:
            print("missing hostname")
            return -1

        err = self.getRTU(host, port)
        if err == 0:
            tupl = host + ":" + str(port)
            con = self.connections[tupl]['con']
            if not con:
                print("no valid connection")
                return -1
            if self.connections[tupl]['testfr_send'] > self.connections[tupl]['testfr_received'] + 5:
                print("error: too many missed testframes, closing connection")
                CS104_Connection_sendStopDT(self.connections[tupl]["con"])
                CS104_Connection_destroy(self.connections[tupl]["con"])
                self.connections[tupl]["con"] = None
                self.connections[tupl]["state"] = 0
                return -1

            newTime = sCP56Time2a() 
            CP56Time2a_createFromMsTimestamp(CP56Time2a(newTime), Hal_getTimeInMs())
            if CS104_Connection_sendTestCommandWithTimestamp(con, 1, 0x4938, newTime) == False:
                print("error: could not send testframe, closing connection")
                CS104_Connection_sendStopDT(con)
                CS104_Connection_destroy(con)
                self.connections[tupl]["con"] = None
                self.connections[tupl]["state"] = 0              
                return -1

            self.connections[tupl]['testfr_send'] += 1
            return 0


    def removeRTU(self,host,port):
        if port == "" or port == None:
            port = 2404

        tupl = host + ":" + str(port)
        if tupl in self.connections and self.connections[tupl]["con"] != None:
            CS104_Connection_sendStopDT(self.connections[tupl]["con"])
            CS104_Connection_destroy(self.connections[tupl]["con"])
            self.connections[tupl]["con"] = None

        self.connections[tupl]["state"] = 0


def testcallb(tupl, data):
    print("RTU:" + tupl + " - update:" + str(data))

#test the class
if __name__== "__main__":
    client = IEC60870_5_104_client(testcallb)
    if client.getRTU("localhost", 2404) == 0:
        tupl = "localhost:2404"
        # perform read of latest data
        print(client.connections[tupl]["data"])
        #perform operate
        if client.select("iec60870-5-104://localhost:2404/DoublePointCommand/6000", 1) == 1:
            if client.operate("iec60870-5-104://localhost:2404/DoublePointCommand/6000", 1) == 1:
                print("oper success")
            else:
                print("oper failed")
        else:
            print("select failed")


