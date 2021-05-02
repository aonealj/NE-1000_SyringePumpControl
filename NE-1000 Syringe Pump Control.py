# NE-1000 syringe pump control functions

import serial

# setup for communications
def setup_serial(port_name, baud_rate, time_out):
    com_port = serial.Serial()
    com_port.port = port_name
    com_port.baudrate = baud_rate
    com_port.timeout = time_out
    com_port.write_timeout = time_out
    return com_port


# properly format input for the syringe pumps
def cmdsp(inputChar2):
    return bytes(str(inputChar2) + '\r', 'ascii')


# command to change the diameter
# keep space between command code and associated inputs
def setDIAcmd(dia):  # units are mm
    return cmdsp('DIA ' + str(dia))


# command to select phase num
def selPHN(phaseNum):
    return cmdsp('PHN ' + str(phaseNum))


# set function to pumping rate type
def funcRate():
    return cmdsp('FUN RAT')


# set rate w/correct units
def pumpRate(pumping_rate, pumping_units):
    return cmdsp('RAT ' + str(pumping_rate) + ' ' + str(pumping_units))


# set rate w/o units (no units [nu])
def pump_rate_nu(pumping_rate):
    return cmdsp('RAT ' + str(pumping_rate))


# function to set the volume
def setVol(pumpVol):
    return cmdsp('VOL ' + str(pumpVol))


# function to set the volume units--this cannot be combined with the setting the units
# see the manual for the valid inputs
def setVolUnits(pumpVolUnits):
    return cmdsp('VOL ' + str(pumpVolUnits))


# function for cmd to set pump direction
def setDir(pumpDir):
    return cmdsp('DIR ' + str(pumpDir))


# function for cmd to input stop set
# probably not necessary
def setStp():
    return cmdsp('FUN STP')


def runPrgmNum(PHS_num):
    return cmdsp('RUN ' + str(PHS_num))
