import datetime as date
import time

while True:

  current = date.datetime.now()
  print(current.strftime("%M"))
  time.sleep(5)
  