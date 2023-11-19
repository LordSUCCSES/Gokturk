#Oluşturucu LordSUCCSES
#Geliştirici Utq-li

#discord : Utq-li15101#1830 | lordsuccses

import os

print("Welcome to GOKTURK HACK TIM's tool...\n Downloading the packets.")

os.system("apt install python")
os.system("apt install python2")
os.system("apt install python3")
os.system("apt install os")
os.system("apt install git")
os.system("apt install ngrok")
os.system("apt install socket")
os.system("apt install time")
os.system("apt install webbrowser")
os.system("apt install requests")
os.system("apt install threading")
os.system("apt install tkinter")
os.system("apt install colorama")

print("All installed successfully!")
print("Now you will open gokturk.py")

try:
    with open('gokturk.py', 'r') as file:
        code = compile(file.read(), 'gokturk.py', 'exec')
        exec(code)
except FileNotFoundError:
    print("gokturk.py dosyası bulunamadı.")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
