import pyautogui
import random
import time


def moveMouse():
    x = random.uniform(1,100)
    pyautogui.moveTo(random.uniform(1, 1000), random.uniform(1, 1000), duration = 1)

starttime = time.monotonic()
while True:
    callingAfter = (60.0 - ((time.monotonic() - starttime) % 60.0))
    #print("Next Mouse Move After" + callingAfter)
    moveMouse()
    time.sleep(5);

 







