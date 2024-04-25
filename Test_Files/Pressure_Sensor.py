import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015(address=0x48, busnum = 1)

GAIN = 1

while True:
    values = adc.read_adc(1, gain=GAIN)
    print(values)
    time.sleep(0.1)
