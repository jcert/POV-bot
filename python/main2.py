import wx
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


class MyFrame(wx.Frame):
  """ We simply derive a new class of Frame. """
  def __init__(self, parent, title):
    wx.Frame.__init__(self, parent, title=title, size=(200,100))
    self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
    self.Show(True)
    self.Bind(wx.EVT_CHAR_HOOK, self.OnAbout)
    self.myCar = Car({"pinA":1,"pinB":1,"pinEN":1},
                     {"pinA":2,"pinB":2,"pinEN":2})
  
  def OnAbout(self, evt):
    keypress = evt.GetKeyCode()
    if(keypress == wx.WXK_DOWN):
      print("D")
      self.myCar.Move("D")
      #time.sleep(1)
    elif(keypress == wx.WXK_UP):
      print("U")
      self.myCar.Move("U")
    elif(keypress == wx.WXK_LEFT):
      print("L")
      self.myCar.Move("L")
    elif(keypress == wx.WXK_RIGHT):
      print("R")
      self.myCar.Move("R")
    elif(keypress == ord("Q")):
      print("Quit")
      self.Close()  
    else:
      print("other")
      self.myCar.Move("-")
    pass

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = MyFrame(None, "Robo") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.
app.MainLoop()


