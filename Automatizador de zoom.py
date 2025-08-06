import pyautogui, webbrowser
from time import sleep
print('Ingrese el link')
link = input()

sleep(20)
for n in range(100):
    webbrowser.open(f'{link}')

       

