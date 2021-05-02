# NE-1000 syringe pump control functions

import serial

# properly format input for the syringe pumps
def cmdsp(inputChar2):
    stringInput2 = str(inputChar2) + '\r'
    return bytes(stringInput2, 'ascii')


# command to change the diameter
# keep space between command code and associated inputs
def setDIAcmd(dia):                         #units are mm
    DIAstr = 'DIA ' + str(dia)
    return cmdsp(DIAstr)


# command to select phase num
def selPHN(phaseNum):
    phaseNumStr = 'PHN ' + str(phaseNum)
    return cmdsp(phaseNumStr)


# set function to pumping rate type
def funcRate():
    funcRateStr = 'FUN RAT'
    return cmdsp(funcRateStr)


# set rate w/correct units
def pumpRate(pumping_rate, pumping_units):
    pumpRateStr = 'RAT ' + str(pumping_rate) + ' ' + str(pumping_units)
    return cmdsp(pumpRateStr)


# set rate w/o units (no units [nu])
def pump_rate_nu(pumping_rate):
    return cmdsp('RAT ' + str(pumping_rate))


# function to set the volume
def setVol(pumpVol):
    pumpVolStr = 'VOL ' + str(pumpVol)
    return cmdsp(pumpVolStr)


# function to set the volume units--this cannot be combined with the setting the units
# see the manual for the valid inputs
def setVolUnits(pumpVolUnits):
    pumpVolUnitsStr = 'VOL ' + str(pumpVolUnits)
    return cmdsp(pumpVolUnitsStr)


# function for cmd to set pump direction
def setDir(pumpDir):
    pumpDirStr = 'DIR ' + str(pumpDir)
    return cmdsp(pumpDirStr)


# function for cmd to input stop set
#probably not necessary
def setStp():
    stpStr = 'FUN STP'
    return cmdsp(stpStr)


def runPrgmNum(PHS_num):
    PHS_num_str = 'RUN ' + str(PHS_num)
    return cmdsp(PHS_num_str)