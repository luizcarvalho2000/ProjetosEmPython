import random
import pyautogui as pg
import time

words = ('Donkey', 'Dumb', 'Idiot')
time.sleep(8)
while True:
    a = random.choice(words)
    pg.write("You are a "+ a)
    pg.press('enter')
    time.sleep(0)


