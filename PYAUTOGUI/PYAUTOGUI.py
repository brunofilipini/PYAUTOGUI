import pyautogui
import time

time.sleep(1)

# print(pyautogui.size())
# print(pyautogui.position())

# pyautogui.moveTo(100,100, 2)

# pyautogui.moveRel(100, 100, 2)

# pyautogui.click(500, 500, 2, 2, button="left")

# pyautogui.scroll(-250)

# pyautogui.mouseUp(100, 100, button="left")
# pyautogui.mouseDown(100, 100, button="left")

pyautogui.mouseDown(300, 400, button="left")
pyautogui.moveTo(800, 400, 3)
pyautogui.mouseUp()
pyautogui.moveTo(1000, 400, 3)