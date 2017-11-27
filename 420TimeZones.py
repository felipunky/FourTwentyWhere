from datetime import datetime
from pywinauto import application, Application, Desktop
from pywinauto.keyboard import SendKeys
import time
import pytz

atz = pytz.all_timezones
timestamp = 0
fourtwenty = "Not 420 nigga"
tz = ""
timeNow = datetime.now().time()
chrome = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
app = Application(backend='uia')
print(atz)
for zone in atz:
    if zone == "Portugal":
        atznow = datetime.now(pytz.timezone(zone)).time()
        atznow = str(atznow)
        tz = (pytz.timezone(zone))
        tz = str(tz)
        timeNowSt = str(timeNow)
        print(tz + ", Exactly: " + atznow)
for zone in atz:

    atznow = datetime.now(pytz.timezone(zone)).time()
    atznow = str(atznow)
    tz = (pytz.timezone(zone))
    tz = str(tz)
    timeNowSt = str(timeNow)
    tz = tz + ", Exactly: " + atznow  
    atznow = atznow.split(":")
    timeNowSt = timeNowSt.split(":")

    if atznow[0] == "04" and atznow[1] == "20":

        fourtwenty = "420 in: " + tz

if fourtwenty != "Not 420 nigga":

    notepad = "%windir%\system32\notepad.exe"
    app_1 = Application()
    app_1.start("Notepad.exe")
    app_1["Notepad"]["Edit"].set_edit_text(fourtwenty)
    time.sleep(2)
    app_1.Notepad.MenuSelect("File -> Exit")
    app_1.Notepad.DontSave.Click()
    fourtwenty = str(fourtwenty).split(',')
    fourtwenty = (fourtwenty[0].replace("'",''))
    fourtwenty = str(fourtwenty).replace("420 in:",'')
    app.start(chrome + ' --force-renderer-accessibility --start-maximized '
              'https://www.google.com.co/')
    time.sleep(1)
    SendKeys('{F6}' + fourtwenty + '{ENTER}', with_spaces=True)
    
    



