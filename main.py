# -*- coding: utf-8 -*-

import Components
import time
import datetime as date
import sys

#Setting up all the data screens for the LCD
def Menu(value):
  global State, Page, Study_hrs, Study_mins, Repeat, Audio, Shock, Break_hrs, Break_mins, Remain_Hours, Remain_Mins, Reps
  #Page -1
  Welcome =     [ "     Welcome to     ",
                  "         the        ", 
                  "      Study Box     ", 
                  "                    "]
  #Page 0                
  Start =       [ "   Please Select    ", 
                  "     an option      ", 
                  "Start       Settings", 
                  "  ^            %    ", 
                  "  %            ^    "]
  #Page 20          
  Settings =    [ "   Study Settings   ", 
                  "Audio:        Shock:", 
                  "                    ", 
                  " ^                % ",
                  " %                ^ "]
  total = 0
  line = ""
  if Audio:
    total += 2
    line += "ON"
  else:
    total += 3
    line += "OFF"
  if Shock:
    total += 2
  else:
    total += 3
  
  for i in range(20 - total):
    line += " "
  if Shock:
    line += "ON"
  else:
    line += "OFF"
  Settings[2] = line
  
  #Page 1         
  Method =      [ "   Please Select    ", 
                  "   a Study Method   ", 
                  "Pomodora      Custom", 
                  "   ^             %  ",
                  "   %             ^  "]
  #Page 2            
  Pomodora =    [ "   Please Select    ", 
                  " a Pomodora Method  ", 
                  "Short           Long", 
                  "  ^              %  ",
                  "  %              ^  "]
  #Page 11         
  StudyTime =   [ "   Set Study Time   ", 
                  "  Hours:   Minutes: ", 
                  "    00   :    00    ", 
                  "     ^         %    ",
                  "     %         ^    ",
                  "     $         %    ",
                  "     %         $    "]
  Study_Time = "    "
  if Study_hrs < 10:
    Study_Time += "0" + str(Study_hrs) + "   :    "
  else:
     Study_Time += str(Study_hrs) + "   :    "
  if Study_mins < 10:
    Study_Time += "0" + str(Study_mins) + "    "
  else:
    Study_Time += str(Study_mins) + "    "
  StudyTime[2] = Study_Time
  
  #Page 12             
  BreakTime =   [ "   Set Break Time   ", 
                  "  Hours:   Minutes: ", 
                  "    00   :    00    ", 
                  "     ^         %    ",
                  "     %         ^    ",
                  "     $         %    ",
                  "     %         $    "]
  Break_Time = "    "
  if Break_hrs < 10:
    Break_Time += "0" + str(Break_hrs) + "   :    "
  else:
     Break_Time += str(Break_hrs) + "   :    "
  if Break_mins < 10:
    Break_Time += "0" + str(Break_mins) + "    "
  else:
    Break_Time += str(Break_mins) + "    "
  BreakTime[2] = Break_Time
  
  #Page 3            
  Repititions = [ " Set Study Repeats  ", 
                  "      Repeats       ", 
                  "         00         ", 
                  "          ^         ",
                  "          $         "]
  Rep_Number = "         "
  if Repeat < 10:
    Rep_Number += "0" + str(Repeat) + "         "
  else:
    Rep_Number += str(Repeat) + "         "
  Repititions[2] = Rep_Number 
  
  
  #Page 4           
  Phone =       [ "  Please Put Your   ", 
                  "  Phone on the Box  ", 
                  "      Calibrate:    ", 
                  "          ^         ",
                  "    ^Attempting^    ",
                  "       Failed       ",
                  "      Success       "]
  #Page 5             
  Studying =    [ "Rep ##: Study Time: ", 
                  "                    ", 
                  "       00:00        ", 
                  "                    "]
      
  #Page 6            
  Break =       [ "Rep ##: Break Time: ", 
                  "                    ", 
                  "       00:00        ", 
                  "                    "]
  if Reps < 10:
    Studying[0] = "Rep 0" + str(Reps) + ": Study Time: "
    Break[0] = "Rep 0" + str(Reps) + ": Break Time: " 
  else:
    Studying[0] = "Rep " + str(Reps) + ": Study Time: "
    Break[0] = "Rep " + str(Reps) + ": Break Time: "
    
  TimeLine = "       "
  if Remain_Hours < 10:
    TimeLine += "0" + str(Remain_Hours) + ":"
  else:
    TimeLine += str(Remain_Hours) + ":"
  if Remain_Mins < 10:
    TimeLine += "0" + str(Remain_Mins) + "        "
  else:
    TimeLine += str(Remain_Mins) + "        "
  
  Studying[2] = TimeLine
  Break[2] = TimeLine
    
  #Page 7                
  Finish =      [ "   Done Studying    ", 
                  "                    ", 
                  "    Great Job!!!    ", 
                  "                    "]
  match value:
    case 0:
      return Start
    case 20:
      return Settings
    case 1:
      return Method
    case 2:
      return Pomodora
    case 11:
      return StudyTime
    case 12:
      return BreakTime
    case 3:
      return Repititions
    case 4:
      return Phone
    case 5:
      return Studying
    case 6:
      return Break
    case 7:
      return Finish
    case -1:
      return Welcome

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# This function will response to the user's input based on what menu it is on currently
def response(command):
  global State, Page, Study_hrs, Study_mins, Repeat, Audio, Shock, Break_hrs, Break_mins  
  match command:
    case "Left":
      match Page:
    
        case 0:
          if State == 1:
            State = 0
            box.updateArrows(Menu(Page),State)
            
        case 20 | 1 | 2:
          if State == 1:
            State = 0
            box.updateArrows(Menu(Page),State)
          elif State == 0:
            Page = 0
            State = 0
            box.printScreen(Menu(Page))    
    
        case 11:
          if State == 0:
            Page = 1
            State = 0
            box.printScreen(Menu(Page)) 
            
          elif State == 1:
            State = 0
            box.updateArrows(Menu(Page),State)
          
            
          elif State == 2:
            if Study_hrs == 0:
              Study_hrs = 99
            else:
              Study_hrs -= 1
            box.updateData(Menu(Page))
            
          elif State == 3:
            if Study_mins == 0:
              Study_mins = 59
            else:
              Study_mins -= 1
            box.updateData(Menu(Page))
    
        case 12:
          if State == 1:
            State = 0
            box.updateArrows(Menu(Page))
          elif State == 0:
            Page = 1
            State = 0
            box.printScreen(Menu(Page)) 
            
          elif State == 2:
            if Break_hrs == 0:
              Break_hrs = 99
            else:
              Break_hrs -= 1
            box.updateData(Menu(Page))
            
          elif State == 3:
            if Break_mins == 0:
              Break_mins = 59
            else:
              Break_mins -= 1
            box.updateData(Menu(Page))
    
        case 3:
          if State == 0:
            Page = 1
            State = 0
            box.printScreen(Menu(Page)) 
            
          elif State == 1:
            if Repeat == 1:
              Repeat == 99
            else:
              Repeat -= 1
            box.updateData(Menu(Page))
              
        case 4:
          if State == 0:
            Page = 3
            State = 0
            box.printScreen(Menu(Page))
        case 5 | 6 | 7 | -1:
          pass
    
  
    case "Right":
      match Page:
    
        case 0 | 20 | 1 | 2:
          if State == 0:
            State = 1
            box.updateArrows(Menu(Page),State)
                
        case 11:
          if State == 0:
            State = 1
            box.updateArrows(Menu(Page),State) 
            
          elif State == 1 and (Study_hrs + Study_mins) > 0:
            Page = 12
            State = 0
            box.printScreen(Menu(Page))
          
            
          elif State == 2:
            if Study_hrs == 99:
              Study_hrs = 0
            else:
              Study_hrs += 1
            box.updateData(Menu(Page))
            
          elif State == 3:
            if Study_mins == 59:
              Study_mins = 0
            else:
              Study_mins += 1
            box.updateData(Menu(Page))
            
        case 12:
          if State == 0:
            State = 1
            box.updateArrows(Menu(Page),State) 
            
          elif State == 1 and (Study_hrs + Study_mins) > 0:
            Page = 3
            State = 0
            box.printScreen(Menu(Page))
          
            
          elif State == 2:
            if Break_hrs == 99:
              Break_hrs = 0
            else:
              Break_hrs += 1
            box.updateData(Menu(Page))
            
          elif State == 3:
            if Break_mins == 59:
              Break_mins = 0
            else:
              Break_mins += 1
            box.updateData(Menu(Page))
            
        case 3:
          if State == 0:
            Page = 4
            State = 0
            box.printScreen(Menu(Page)) 
            
          elif State == 1:
            if Repeat == 99:
              Repeat == 1
            else:
              Repeat += 1
            box.updateData(Menu(Page))
            
        case 4 | 5 | 6 | 7 | -1:
          pass
    
  
    case "Enter":
      match Page:
    
        case 0:
          if State == 0:
            Page = 1
            State = 0
            box.printScreen(Menu(Page))
          elif State == 1:
            Page = 20
            State = 0
            box.printScreen(Menu(Page))
            
        case 20:
          if State == 0:
            Audio = not Audio
            box.updateData(Menu(Page))
          #Adjust Later
          elif State == 1:
            Shock = not Shock
            box.updateData(Menu(Page))
            
        case 1:
          if State == 0:
            Page = 2
            State = 0
            box.printScreen(Menu(Page))
          elif State == 1:
            Page = 11
            State = 0
            box.printScreen(Menu(Page))
            
        case 2:
          if State == 0:
            Study_hrs = 0
            Study_mins = 25
            Break_hrs = 0
            Break_mins = 5
            
          elif State == 1:
            Study_hrs = 0
            Study_mins = 45
            Break_hrs = 0
            Break_mins = 15
           
          Page = 3
          State = 0
          box.printScreen(Menu(Page))
           
        case 11 | 12:
          if State == 0:
            State = 2
            box.updateArrows(Menu(Page),State)
          elif State == 1:
            State = 3
            box.updateArrows(Menu(Page),State)
          elif State == 2:
            State = 0
            box.updateArrows(Menu(Page),State)
          elif State == 3:
            State = 1
            box.updateArrows(Menu(Page),State)
            
        case 3:
          if State == 0:
            State = 1
            box.updateArrows(Menu(Page),State)
          elif State == 1:
            State = 0
            box.updateArrows(Menu(Page),State)
            
        case 4:
          calibrateWeight()
          
        case 5 | 6 | 7 | -1:
          pass

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# This function will take three measurements from the pressure sensor and find the average. This average weight will be used
# to compare to so that it can determine it the phone is being used or if it was removed
def calibrateWeight():
  global State, Page
  
  State = 1
  box.updateArrows(Menu(Page),State)
  measurements = []
  
  for i in range(5):
    measurements.append(box.pressureRead())
    time.sleep(2)
  print(measurements) 
  
  if max(measurements) - min(measurements) > 100:
    State = 2
    box.updateArrows(Menu(Page),State)
    time.sleep(3)
    State = 0
    box.updateArrows(Menu(Page),State)
  else:
    Weight = sum(measurements)/len(measurements)
    print(Weight)
    State = 3
    box.updateArrows(Menu(Page),State)
    time.sleep(3)
    beginStudy(Weight)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#This function is the Study and Break loop. It tracks how much time you have for studying and for your break time
def beginStudy(Weight):
  global State, Page, Study_hrs, Study_mins, Repeat, Audio, Shock, Break_hrs, Break_mins, Remain_Hours, Remain_Mins, Reps
  
  timer = date.datetime.now()
  Reps = 1
  while Reps <= Repeat:
    Remain_Hours = Study_hrs
    Remain_Mins = Study_mins
    Page = 5
    State = 0
    box.printScreen(Menu(Page))
    
    Current_min = timer.strftime("%M")
    Saved_min = Current_min
    
    while Remain_Hours > 0 or Remain_Mins > 0:
      timer = date.datetime.now()
      Current_min = timer.strftime("%M")
      print(str(timer.strftime("%X")) + " || " + str(Current_min) + " || " + str(Saved_min))
      pressure = box.pressureRead()
      distance = box.distanceRead()
      
      if (abs(Weight - pressure) > 75 or distance < 10) and Audio:
        
        box.playAlarm()
      
      if Current_min != Saved_min:
        Saved_min = Current_min
        
        if Remain_Mins > 0:
          Remain_Mins -= 1
        else:
          if Remain_Hours > 0:
            Remain_Hours -= 1
            Remain_Mins = 59
          else:
            sys.exit()
        box.updateData(Menu(Page))
      time.sleep(3)
    
    Remain_Hours = Break_hrs
    Remain_Mins = Break_mins
    Page = 6
    State = 0
    box.printScreen(Menu(Page))
    
    timer = date.datetime.now()
    Current_min = timer.strftime("%M")
    Saved_min = Current_min
    
    while Remain_Hours > 0 or Remain_Mins > 0:
      timer = date.datetime.now()
      Current_min = timer.strftime("%M")
      
      if abs(Weight - distance) > 75 or distance < 10:
        box.playAlarm()
      
      if Current_min != Saved_min:
        Saved_min = Current_min
        
        if Remain_Mins > 0:
          Remain_Mins -= 1
        else:
          if Remain_Hours > 0:
            Remain_Hours -= 1
            Remain_Mins = 59
          else:
            sys.exit()
        box.updateData(Menu(Page))     
      time.sleep(3)
      
    Reps += 1
  
  Page = 7
  box.printScreen(Menu(Page))
  time.sleep(5)
  Page = 0
  box.printScreen(Menu(Page))
  

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Declare fuctions
global State, Page, Study_hrs, Study_mins, Repeat, Audio, Shock, Break_hrs, Break_mins, Remain_Hours, Remain_Mins, Reps 
State = 0
Page = 0

Study_hrs = 0
Study_mins = 0
Break_hrs = 0
Break_mins = 0
Remain_Hours = 0
Remain_Mins = 0
Reps = 1

Repeat = 1

Audio = True
Shock = True

box = Components.Components() 
# Study Box Start up screens
box.printScreen(Menu(-1))
time.sleep(3)
box.printScreen(Menu(0))

# Reads in the user's button inputs and responds
while True:
  command = box.userInput()
  
  response(command)
  time.sleep(0.2)

