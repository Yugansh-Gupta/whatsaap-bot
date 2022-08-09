import pyautogui as pg
import time
time.sleep(3)
for i in range(500):
    pg.write("hello")
    pg.press("enter")
