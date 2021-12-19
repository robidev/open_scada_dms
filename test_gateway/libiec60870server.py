#!/usr/bin/env python3
from lib60870 import *
import time

class IEC60870_5_104_server:

    def printCP56Time2a(self, time):
        print("%02i:%02i:%02i %02i/%02i/%04i" % ( CP56Time2a_getHour(time),
                        CP56Time2a_getMinute(time),
                        CP56Time2a_getSecond(time),
                        CP56Time2a_getDayOfMonth(time),
                        CP56Time2a_getMonth(time),
                        CP56Time2a_getYear(time) + 2000) )

    def clock(self, param, con, asdu, newTime):
        print("Process time sync command with time ")
        self.printCP56Time2a(newTime)
        newSystemTimeInMs = CP56Time2a_toMsTimestamp(newTime)
        #/* Set time for ACT_CON message */
        CP56Time2a_setFromMsTimestamp(newTime, Hal_getTimeInMs())
        #/* update system time here */
        return True

    def GI_h(self, param, connection, asdu, qoi):
        print(f"Received interrogation for group {qoi}")

        if (qoi == 20): #{ /* only handle station interrogation */
            alParams = IMasterConnection_getApplicationLayerParameters(connection)
            IMasterConnection_sendACT_CON(connection, asdu, False)

            #* The CS101 specification only allows information objects without timestamp in GI responses */
            # measuredvalue
            type = MeasuredValueScaled
            newAsdu = CS101_ASDU_create(alParams, False, CS101_COT_INTERROGATED_BY_STATION, 0, 1, False, False)
            io = None
            for ioa in self.IOA_list:
                if self.IOA_list[ioa]['type'] == type:
                    if io == None:
                        io = cast( MeasuredValueScaled_create(None,ioa, self.IOA_list[ioa]['data'], IEC60870_QUALITY_GOOD), InformationObject) #
                        CS101_ASDU_addInformationObject(newAsdu, io)
                    else:
                        CS101_ASDU_addInformationObject(newAsdu, cast( MeasuredValueScaled_create(cast(io,MeasuredValueScaled),ioa,self.IOA_list[ioa]['data'],IEC60870_QUALITY_GOOD), InformationObject) )
            if io != None:
                InformationObject_destroy(io)
                IMasterConnection_sendASDU(connection, newAsdu)
            CS101_ASDU_destroy(newAsdu)

            #singlepoint
            type = SinglePointInformation
            newAsdu = CS101_ASDU_create(alParams, False, CS101_COT_INTERROGATED_BY_STATION, 0, 1, False, False)
            io = None
            for ioa in self.IOA_list:
                if self.IOA_list[ioa]['type'] == type:
                    if io == None:
                        io = cast( SinglePointInformation_create(None, ioa, self.IOA_list[ioa]['data'], IEC60870_QUALITY_GOOD), InformationObject)
                        CS101_ASDU_addInformationObject(newAsdu, io)
                    else:
                        CS101_ASDU_addInformationObject(newAsdu, cast( SinglePointInformation_create(cast(io,SinglePointInformation), ioa,self.IOA_list[ioa]['data'],IEC60870_QUALITY_GOOD), InformationObject) )
            if io != None:
                InformationObject_destroy(io)
                IMasterConnection_sendASDU(connection, newAsdu)
            CS101_ASDU_destroy(newAsdu)

            #doublepoint
            type = DoublePointInformation
            newAsdu = CS101_ASDU_create(alParams, False, CS101_COT_INTERROGATED_BY_STATION, 0, 1, False, False)
            io = None
            for ioa in self.IOA_list:
                if self.IOA_list[ioa]['type'] == type:
                    if io == None:
                        io = cast( DoublePointInformation_create(None, ioa, self.IOA_list[ioa]['data'], IEC60870_QUALITY_GOOD), InformationObject)
                        CS101_ASDU_addInformationObject(newAsdu, io)
                    else:
                        CS101_ASDU_addInformationObject(newAsdu, cast( DoublePointInformation_create(cast(io,DoublePointInformation), ioa,self.IOA_list[ioa]['data'],IEC60870_QUALITY_GOOD), InformationObject) )
            if io != None:
                InformationObject_destroy(io)
                IMasterConnection_sendASDU(connection, newAsdu)
            CS101_ASDU_destroy(newAsdu)


            IMasterConnection_sendACT_TERM(connection, asdu)
        else:
            IMasterConnection_sendACT_CON(connection, asdu, True)



    def ASDU_h(self, param, connection, asdu):
        print("ASDU received")
        cot = CS101_ASDU_getCOT(asdu)
        if cot == CS101_COT_ACTIVATION:
            io = CS101_ASDU_getElement(asdu, 0)
            ioa = InformationObject_getObjectAddress(io)
            if not ioa in self.IOA_list:
                print("could not find IOA")
                CS101_ASDU_setCOT(asdu, CS101_COT_UNKNOWN_IOA)
            else:
                ioa_object = self.IOA_list[ioa]
                if (CS101_ASDU_getTypeID(asdu) == C_SC_NA_1):
                    print("received single command")
                    if ioa_object['type'] == SingleCommand:
                        sc = cast( io, SingleCommand)
                        
                        print(f"IOA: {InformationObject_getObjectAddress(io)} switch to {SingleCommand_getState(sc)}, select:{SingleCommand_isSelect(sc)}")
                        ioa_object['data'] = SingleCommand_getState(sc)
                        if self.IOA_list[ioa]['callback'] != None:
                            self.IOA_list[ioa]['callback'](ioa,ioa_object, self, SingleCommand_isSelect(sc))

                        CS101_ASDU_setCOT(asdu, CS101_COT_ACTIVATION_CON)
                    else:
                        print("mismatching asdu type:")
                        CS101_ASDU_setCOT(asdu, CS101_COT_UNKNOWN_TYPE_ID)

                if (CS101_ASDU_getTypeID(asdu) == C_DC_NA_1):
                    print("received double command")
                    if ioa_object['type'] == DoubleCommand:
                        sc = cast( io, DoubleCommand)
                        print(f"IOA: {InformationObject_getObjectAddress(io)} switch to {DoubleCommand_getState(sc)}, select:{DoubleCommand_isSelect(sc)}")
                        ioa_object['data'] = DoubleCommand_getState(sc)
                        if self.IOA_list[ioa]['callback'] != None:
                            self.IOA_list[ioa]['callback'](ioa,ioa_object, self, DoubleCommand_isSelect(sc))

                        CS101_ASDU_setCOT(asdu, CS101_COT_ACTIVATION_CON)
                    else:
                        print("mismatching asdu type:")
                        CS101_ASDU_setCOT(asdu, CS101_COT_UNKNOWN_TYPE_ID)

            InformationObject_destroy(io)
        elif cot == CS101_COT_ACTIVATION_TERMINATION:
            print("GI done")
        else:
            print("ASDU unknown: " + str(CS101_ASDU_getCOT(asdu)))
            CS101_ASDU_setCOT(asdu, CS101_COT_UNKNOWN_COT)

        IMasterConnection_sendASDU(connection, asdu)

        return True


    def Conn_req(self, param, address):
        print("New connection request")
        return True

    def Conn_event(self, param, con, event):
        if (event == CS104_CON_EVENT_CONNECTION_OPENED):
            print(f"Connection opened {con}")
        elif (event == CS104_CON_EVENT_CONNECTION_CLOSED):
            print(f"Connection closed {con}")
        elif (event == CS104_CON_EVENT_ACTIVATED):
            print(f"Connection activated {con}")
        elif (event == CS104_CON_EVENT_DEACTIVATED):
            print(f"Connection deactivated {con}")

    def read(self, param, connection, asdu, ioa):
        if ioa in self.IOA_list:
            # update data
            if self.IOA_list[ioa]['callback'] != None:
                self.IOA_list[ioa]['callback'](ioa,self.IOA_list[ioa], self)

            newAsdu = CS101_ASDU_create(self.alParams, False, CS101_COT_SPONTANEOUS, 0, 1, False, False)
            if self.IOA_list[ioa]['type'] == MeasuredValueScaled:
                io = cast(MeasuredValueScaled_create(None, ioa, self.IOA_list[ioa]['data'], IEC60870_QUALITY_GOOD),InformationObject)
            elif self.IOA_list[ioa]['type'] == SinglePointInformation:
                io = cast(SinglePointInformation_create(None, ioa, self.IOA_list[ioa]['data'], IEC60870_QUALITY_GOOD),InformationObject)
            elif self.IOA_list[ioa]['type'] == DoublePointInformation:
                io = cast(DoublePointInformation_create(None, ioa, self.IOA_list[ioa]['data'], IEC60870_QUALITY_GOOD),InformationObject)
            else:
                return False
            CS101_ASDU_addInformationObject(newAsdu, io)
            InformationObject_destroy(io)
            #/* Add ASDU to slave event queue - don't release the ASDU afterwards!
            CS104_Slave_enqueueASDU(self.slave, newAsdu)
            CS101_ASDU_destroy(newAsdu)  
            return True
        return False


    def __init__(self, ip = "0.0.0.0"):
        self.clockSyncHandler = CS101_ClockSynchronizationHandler(self.clock)
        self.interrogationHandler = CS101_InterrogationHandler(self.GI_h)
        self.asduHandler = CS101_ASDUHandler(self.ASDU_h)
        self.connectionRequestHandler = CS104_ConnectionRequestHandler(self.Conn_req)
        self.connectionEventHandler = CS104_ConnectionEventHandler(self.Conn_event)
        self.readEventHandler = CS101_ReadHandler(self.read)

        self.slave = CS104_Slave_create(100, 100)
        CS104_Slave_setLocalAddress(self.slave, ip)
        #   /* Set mode to a single redundancy group
        CS104_Slave_setServerMode(self.slave, CS104_MODE_SINGLE_REDUNDANCY_GROUP)

        #/* get the connection parameters - we need them to create correct ASDUs */
        self.alParams = CS104_Slave_getAppLayerParameters(self.slave)

        #/* set the callback handler for the clock synchronization command */
        CS104_Slave_setClockSyncHandler(self.slave, self.clockSyncHandler, None)

        #/* set the callback handler for the interrogation command */
        CS104_Slave_setInterrogationHandler(self.slave, self.interrogationHandler, None)

        #/* set handler for other message types */
        CS104_Slave_setASDUHandler(self.slave, self.asduHandler, None)

        #/* set handler to handle connection requests (optional) */
        CS104_Slave_setConnectionRequestHandler(self.slave, self.connectionRequestHandler, None)

        #/* set handler to track connection events (optional) */
        CS104_Slave_setConnectionEventHandler(self.slave, self.connectionEventHandler, None)

        CS104_Slave_setReadHandler(self.slave, self.readEventHandler, None)

        self.IOA_list = {}

    def add_ioa(self, number, type = MeasuredValueScaled, data = 0, callback = None, event = False):
        if not number in self.IOA_list:
            self.IOA_list[int(number)] = { 'type': type, 'data': data, 'callback': callback, 'event': event }
            return 0
        else:
            return -1


    def update_data(self):
        for ioa in self.IOA_list:
            if self.IOA_list[ioa]['callback'] != None:
                self.IOA_list[ioa]['callback'](ioa,self.IOA_list[ioa], self)


    def update_ioa(self, ioa, data):
        value = int(float(data))
        if value != self.IOA_list[ioa]['data']: #check if value is different, else ignore
            self.IOA_list[ioa]['data'] = value
            if self.IOA_list[ioa]['event'] == True:
                newAsdu = CS101_ASDU_create(self.alParams, False, CS101_COT_SPONTANEOUS, 0, 1, False, False)
                if self.IOA_list[ioa]['type'] == MeasuredValueScaled:
                    io = cast(MeasuredValueScaled_create(None, ioa, self.IOA_list[ioa]['data'], IEC60870_QUALITY_GOOD),InformationObject)
                elif self.IOA_list[ioa]['type'] == SinglePointInformation:
                    io = cast(SinglePointInformation_create(None, ioa, self.IOA_list[ioa]['data'], IEC60870_QUALITY_GOOD),InformationObject)
                elif self.IOA_list[ioa]['type'] == DoublePointInformation:
                    io = cast(DoublePointInformation_create(None, ioa, self.IOA_list[ioa]['data'], IEC60870_QUALITY_GOOD),InformationObject)
                else:
                    return -1

                CS101_ASDU_addInformationObject(newAsdu, io)
                InformationObject_destroy(io)
                #/* Add ASDU to slave event queue - don't release the ASDU afterwards!
                CS104_Slave_enqueueASDU(self.slave, newAsdu)
                CS101_ASDU_destroy(newAsdu)

        return 0

    def start(self):
        CS104_Slave_start(self.slave)

        if CS104_Slave_isRunning(self.slave) == False:
            print("Starting server failed!\n")
            return -1
        return 0

    #scaledValue = 0

    #while True:
    #  time.sleep( 1 )
      #newAsdu = CS101_ASDU_create(self.alParams, False, CS101_COT_PERIODIC, 0, 1, False, False)
      #io = cast(MeasuredValueScaled_create(None, 110, scaledValue, IEC60870_QUALITY_GOOD),InformationObject)
      #scaledValue += 1
      #CS101_ASDU_addInformationObject(newAsdu, io)
      #InformationObject_destroy(io)
      #/* Add ASDU to slave event queue - don't release the ASDU afterwards!
      #CS104_Slave_enqueueASDU(self.slave, newAsdu)
      #CS101_ASDU_destroy(newAsdu)

    def stop(self):
        CS104_Slave_stop(self.slave)
        CS104_Slave_destroy(self.slave)

#test the class
if __name__== "__main__":
    srv = IEC60870_5_104_server()
    srv.add_ioa(100, MeasuredValueScaled,1)
    srv.add_ioa(101, MeasuredValueScaled,22,None,True)
    srv.add_ioa(102, MeasuredValueScaled,42)
    srv.add_ioa(200, SinglePointInformation,False)
    srv.add_ioa(300, DoublePointInformation,1)
    srv.add_ioa(301, DoublePointInformation,2)
    srv.add_ioa(5000, DoubleCommand,1)
    srv.add_ioa(5001, DoubleCommand,2)
    srv.start()
    val = 0
    while True:
        time.sleep( 2 )
        srv.update_ioa(101,val)
        val = val + 2

