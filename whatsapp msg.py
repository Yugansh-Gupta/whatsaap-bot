import pyautogui as pg
import random
import time
hello=("hello","hi")
time.sleep(8)
for i in range(500):
    a=random.choice(hello)
    pg.write(a)
    pg.press("enter")