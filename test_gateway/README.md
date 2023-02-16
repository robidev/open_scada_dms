This is a test gateway to have a simple IEC60870-5-104 RTU that generates some changing values for the open scada dms project

Please note it uses the (awesome!) libiec60870 library from MZ-automation, that contains the GPLv3 license.

ioa 5000 is to enable/disable periodic update of test values. 
the behavior can be enabled by writing a 1 to this singlecommand IOA, and disabled by writing a 0