import pyautogui,time
input('start')
f = open("text.txt",'r')
for word in f :
    pyautogui.typewrite(word)
    pyautogui.press("enter")

