# The purpose of this file is to determine if a the Analog to Digial Converter is functional
# and if you can get a variety of input pressures.
import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015(address=0x48, busnum = 1)

GAIN = 1

while True:
    values = adc.read_adc(1, gain=GAIN)
    print(values)
    time.sleep(0.1)
