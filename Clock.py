from os import path
from pywinauto import Application
from pywinauto import keyboard
import time
import win32api
import datetime

timeNow = (datetime.datetime.now().time())
dateTime = (datetime.datetime.now())
timeNowSt = str(timeNow)

print(timeNow)

timeNowSt = timeNowSt.split(":")

if timeNowSt[0] == "16" and timeNowSt[1] == "20":
    
    notepad = "%windir%\system32\notepad.exe"

    app_1 = Application()

    app_1.start("Notepad.exe")

    app_1["Notepad"]["Edit"].set_edit_text("Fucking 420!")

elif timeNowSt[0] == "04" and timeNowSt[1] == "20":

    notepad = "%windir%\system32\notepad.exe"

    app_1 = Application()

    app_1.start("Notepad.exe")

    app_1["Notepad"]["Edit"].set_edit_text("Fucking 420!")

else:

    timeThen = datetime.datetime.strptime('2018-4-20T04:20:00Z', '%Y-%m-%dT%H:%M:%SZ')

    timeDistance = (dateTime-timeThen)

    notepad = "%windir%\system32\notepad.exe"

    app_1 = Application()

    app_1.start("Notepad.exe")

    app_1["Notepad"]["Edit"].set_edit_text("%s microseconds until 420" % (timeDistance))

    time.sleep(3)

    app_1.Notepad.MenuSelect("File -> Exit")

    app_1.Notepad.DontSave.Click()
    

        

    

                
      

            


