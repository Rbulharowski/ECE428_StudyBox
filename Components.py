#The purpose of this file is to set up the Ultrasonic sensor, Pressure Sensor, LCD Display, Buttons and Audio
#so that it can be used by the main.py file.

#Import the neccessary files or libraries
import time
import I2C_LCD_driver
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import pygame


class Components:
    
    #initialization function
    def __init__(self):
        
        #Pressure Sensor
        self.press = Adafruit_ADS1x15.ADS1015(address=0x48, busnum = 1)
        
        #LCD Display
        self.user = I2C_LCD_driver.lcd()
        
        #Ultra Sonic Sensor
        GPIO.setmode(GPIO.BCM)
        self.TRIG = 23
        self.ECHO = 25
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
        GPIO.output(self.TRIG, False)
        
        #Audio Output
        pygame.mixer.init()
        
        #Button Inputs 
        self.Left = 12
        self.Right = 16
        self.Enter = 20
        GPIO.setup(self.Left, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.Right, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.Enter, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
    # Reads the pressure sensor value
    def pressureRead(self):
        GAIN = 1
        values = self.press.read_adc(1, gain=GAIN)
        return values
    
    # Read distance value from the ultrasonic sensor
    def distanceRead(self):
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)
        
        while GPIO.input(self.ECHO) == 0:
            pulse_start = time.time()
            
        while GPIO.input(self.ECHO) == 1:
            pulse_end = time.time()
            
        pulse_duration = pulse_end - pulse_start
        
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance
    
    # This is a test function that can only be accessed if the Components.py file is ran by itself
    # This function test to see if audio will play through the Raspberry Pi audio jack if the right conditions are met
    # Audio files are found in the Audio_File Folder
    def inputTest(self):
        weight = self.pressureRead()
        distance = self.distanceRead()
        self.user.lcd_display_string("Weight: " + str(weight) + "   ", 1)
        self.user.lcd_display_string("Distance: " + str(distance) + " cm   ", 3)
        if weight > 2000 or distance < 10:
          pygame.mixer.music.load("Audio_Files/Alarm.mp3")
          pygame.mixer.music.play()
          while pygame.mixer.music.get_busy() == True:
            continue

    # This fuction is used to update all 4 rows of the LCD display based on the inputed menu  
    def printScreen(self, rows):
      self.user.lcd_display_string(rows[0],1)
      self.user.lcd_display_string(rows[1],2)
      self.user.lcd_display_string(rows[2],3)
      self.user.lcd_display_string(rows[3],4)
    
    # This function only updates the 4th row of the LCD display. Arrows are what usually populate the display
    def updateArrows(self, rows, state):
      self.user.lcd_display_string(rows[3+state],4)
    
    # This function only updates the 3rd row of the LCD display
    def updateData(self, rows):
      self.user.lcd_display_string(rows[2],3)
    
    # This function wait until a button is pressed and send the value of which button is pressed
    def userInput(self):
      while GPIO.input(self.Left) == GPIO.HIGH or GPIO.input(self.Right) == GPIO.HIGH or GPIO.input(self.Enter) == GPIO.HIGH:
        pass
      
      while True:
        if GPIO.input(self.Left) == GPIO.HIGH:
          return "Left"
        if GPIO.input(self.Right) == GPIO.HIGH:
          return "Right"
        if GPIO.input(self.Enter) == GPIO.HIGH:
          return "Enter" 
    
    # It plays the alarm sound from the Audio_Files folder
    def playAlarm(self):
      pygame.mixer.music.load("Audio_Files/Alarm.mp3")
      pygame.mixer.music.play()
      
        
# If this file is run, it will run this function which tests the button inputs, and all of the components.    
if __name__ == '__main__':
    test = Components()
    data = False
    while True:
        if data == False:
          if GPIO.input(test.Left) == GPIO.HIGH:
            print("Left was pressed")
            data = True 
          if GPIO.input(test.Right) == GPIO.HIGH:
            print("Right was pressed")
            data = True 
          if GPIO.input(test.Enter) == GPIO.HIGH:
            print("Enter was pressed")
            data = True 
        if GPIO.input(test.Enter) == GPIO.LOW and GPIO.input(test.Left) == GPIO.LOW and GPIO.input(test.Right) == GPIO.LOW:
          data = False
        test.inputTest()
        time.sleep(0.5)
        
        
        
        
    
        

        
