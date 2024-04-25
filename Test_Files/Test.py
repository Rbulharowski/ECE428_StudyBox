import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()


mylcd.lcd_display_string("Does Ryan ", 1, 4)

mylcd.lcd_display_string("like Zoey?", 2, 4)
sleep(4)
mylcd.lcd_clear()
mylcd.lcd_display_string("Processing.....", 1)
sleep(6)
mylcd.lcd_clear()
mylcd.lcd_display_string("True", 1, 6)
sleep(1)
mylcd.lcd_display_string("More than",3,5)
mylcd.lcd_display_string("she knows <3", 4, 3)
sleep(5)
mylcd.lcd_clear()
