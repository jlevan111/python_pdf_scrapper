import random


def wristband_pulse(sensorID):
    ##This is where the wristband API would be called. If I had one.
    print("***************************************************")
    print("******* FUNCTION NAME: wristband_pulse*************")
    print("***************************************************")
    print("***************************************************")
    print("******* Sensor Number:", sensorID, "***************")
    print("***************************************************")
    pulse = round(60 * random.uniform(1.1,.9),1)
    
    return pulse


def wristband_o2(sensorID):
    ##This is where the wristband API would be called. If I had one.
    print("***************************************************")
    print("******* FUNCTION NAME: wristband_o2*************")
    print("***************************************************")
    print("***************************************************")
    print("******* Sensor Number:", sensorID, "***************")
    print("***************************************************")
    o2 = round(90 * random.uniform(1.1,.9),1)
    
    return o2