import pyautogui
import time
import pyperclip


pyautogui.PAUSE = 1

pyautogui.hotkey("win")
pyautogui.moveTo(89,693,duration=1)
pyautogui.click(89,693);pyautogui.typewrite("chrome", interval=0.2)
pyautogui.hotkey("enter")

#pyautogui.moveTo(1315,31,duration=1)
#pyautogui.click(1315,31)

time.sleep(7)

pyautogui.moveTo(315,47,duration=1)
pyautogui.click(315,47);pyautogui.typewrite("never gonna give you up", interval=0.2)

pyautogui.hotkey("enter")

time.sleep(7)

pyautogui.moveTo(446,443,duration=1)
pyautogui.click(446,443)

time.sleep(180)

pyautogui.hotkey("ctrl","f4")

