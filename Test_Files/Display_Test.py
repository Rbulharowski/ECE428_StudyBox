# The purpose of this file is to test if the I2C LCD driver is functional.
import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()


mylcd.lcd_display_string("Hello World ", 1, 4)

sleep(4)
mylcd.lcd_clear()
mylcd.lcd_display_string("Processing.....", 2)
sleep(6)
mylcd.lcd_clear()
mylcd.lcd_display_string("True", 3, 6)
sleep(1)
mylcd.lcd_display_string("Greetings",4,5)

sleep(5)
mylcd.lcd_clear()
