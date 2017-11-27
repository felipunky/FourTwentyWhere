from os import path
from pywinauto import Application
import win32api

rhino = "C:\Program Files\Rhinoceros 5 (64-bit)\System\Rhino.exe"

app = Application(backend="uia")

app.start(rhino)

print(app.top_window())
