import pyautogui
import time

def click(x,y):
    time.sleep(0.8)
    pyautogui.click(x,y)

def main():
    pyautogui.click(1833, 65)
    time.sleep(3)
    for i in range(3):
        click(1692, 590)
        click(1778, 245)
        click(1571, 286)
        click(1490, 502)
        pyautogui.write('0.0023', interval=0.01)
        click(1606, 850)
        click(1726, 782)
        sb1=pyautogui.pixel(1723, 600)
        sb2=pyautogui.pixel(1723, 600)
        while sb1==sb2:
            sb2=pyautogui.pixel(1723, 600)

'''
screenWidth, screenHeight = pyautogui.size()
currentMouseX0, currentMouseY0 = pyautogui.position()
print(currentMouseX0, currentMouseY0)
time.sleep(10)
currentMouseX1, currentMouseY1 = pyautogui.position()
print(currentMouseX1, currentMouseY1)
time.sleep(10)
currentMouseX2, currentMouseY2 = pyautogui.position()
print(currentMouseX2, currentMouseY2)
time.sleep(10)
currentMouseX3, currentMouseY3 = pyautogui.position()
print(currentMouseX3, currentMouseY3)
time.sleep(10)
currentMouseX4, currentMouseY4 = pyautogui.position()
print(currentMouseX4, currentMouseY4)
time.sleep(10)
currentMouseX5, currentMouseY5 = pyautogui.position()
print(currentMouseX5, currentMouseY5)
time.sleep(10)
currentMouseX6, currentMouseY6 = pyautogui.position()
print(currentMouseX6, currentMouseY6)
time.sleep(10)
'''

main()
