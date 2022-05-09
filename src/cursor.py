import pyautogui
import os
import msvcrt
import sys
pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

print("Дял выхода нажмите на любую клавишу!")
while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)
        print(positionStr, end="")
        print('\b' * len(positionStr), end="", flush=True)
        if msvcrt.kbhit():
            os.system('cls')
            print("Программа завершена.")
            sys.exit()