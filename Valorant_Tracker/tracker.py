## pip install pyautogui for win32gui
from win32gui import GetWindowText, GetForegroundWindow
import pyautogui as pg
import time

while(True):
    print(GetWindowText(GetForegroundWindow()))
    print(pg.position())
    time.sleep(5)
