import pyautogui

print("This program only works on 1080p screens")
print("Please set your steam chat window to snap to the right half of your screen")
y_loops = int(input("Please enter how many rows of steam emotes you have: "))

for i in range(y_loops):
    x=i*23
    y = 798 + x
    for i in range(13):

        z=24*i

        pyautogui.moveTo(1826,1002)
        pyautogui.click()

        pyautogui.moveTo(1540, y)

        pyautogui.moveRel(z, 0)
        pyautogui.click()
        
    
