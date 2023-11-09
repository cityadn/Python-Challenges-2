def dac_conversion(dac_reading):
    #Constants:
    resolution = 1023
    system_voltage = 5
    constant = system_voltage/resolution
    #AnalogueVoltage = ((SystemVoltage/resolution) * DACReading
    analogue_voltage = constant * dac_reading
    return analogue_voltage

dac_reading = int(input("Enter the digital number:\n"))
print("{:.2f}".format(dac_conversion(dac_reading)))
