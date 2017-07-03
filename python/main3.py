import curses
import time

if(False):###is this the raspberryPi?
  import RPi.GPIO as IO
else:
  class GPIO:
    BOARD = 1;
    OUT = 2;
    def setmode(self,x):
      pass
    def setup(self,pin,mode):
      pass  
    def output(self,pin,value):  
      pass
  IO = GPIO()    


class Car:
  def __init__(self,wheel1,wheel2):
    #wheel is [pinA,pinB,pinEN]
    #wheel1 is right, wheel2 is left 
    IO.setup(wheel1["pinA"], IO.OUT)
    IO.setup(wheel1["pinB"], IO.OUT)
    IO.setup(wheel1["pinEN"], IO.OUT)
    IO.setup(wheel2["pinA"], IO.OUT)
    IO.setup(wheel2["pinB"], IO.OUT)
    IO.setup(wheel2["pinEN"], IO.OUT)
    self.wheel1 = wheel1
    self.wheel2 = wheel2
    
  def Move(self,direction):
    IO.output(self.wheel1["pinEN"], False)
    IO.output(self.wheel2["pinEN"], False)      
    if(direction == "D"):
      IO.output(self.wheel1["pinA"], True)
      IO.output(self.wheel1["pinB"], False)      
      IO.output(self.wheel2["pinA"], True)
      IO.output(self.wheel2["pinB"], False)
      IO.output(self.wheel1["pinEN"], True)
      IO.output(self.wheel2["pinEN"], True)
      print("\/")                     
    elif(direction == "U"):
      IO.output(self.wheel1["pinA"], False)
      IO.output(self.wheel1["pinB"], True)      
      IO.output(self.wheel2["pinA"], False)
      IO.output(self.wheel2["pinB"], True)
      IO.output(self.wheel1["pinEN"], True)
      IO.output(self.wheel2["pinEN"], True) 
      print("/\\")
    
    elif(direction == "R"):
      IO.output(self.wheel1["pinA"], False)
      IO.output(self.wheel1["pinB"], True)      
      IO.output(self.wheel1["pinEN"], True)
      print(">>")
    elif(direction == "L"):
      IO.output(self.wheel2["pinA"], False)
      IO.output(self.wheel2["pinB"], True)
      IO.output(self.wheel2["pinEN"], True) 
      print("<<")
    else:
      print("--")
      
  pass  
  
IO.setmode(IO.BOARD)


on = True
myCar = Car({"pinA":27,"pinB":22,"pinEN":17},
                 {"pinA":24,"pinB":25,"pinEN":23})

while(on):
  stdscr = curses.initscr()
  curses.cbreak()
  stdscr.keypad(1)

  stdscr.refresh()

  key = ''
  while key != ord('q'):
      key = stdscr.getch()
      #stdscr.addch(20,25,key)
      #stdscr.refresh()
      if(key == curses.KEY_DOWN):
        print("D")
        myCar.Move("D")
        #time.sleep(1)
      elif(key == curses.KEY_DOWN):
        print("U")
        myCar.Move("U")
      elif(key == curses.KEY_LEFT):
        print("L")
        myCar.Move("L")
      elif(key == curses.KEY_RIGHT):
        print("R")
        myCar.Move("R")  
      else:
        print("other")
        myCar.Move("-")
      pass
  on = False
curses.endwin()

