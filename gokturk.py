import socket
from time import sleep
import tkinter as tk
import webbrowser

def github():
    webbrowser.open("https://github.com/LordSUCCSES")

def findip():
    url = input("Enter Web Site: ")
    name = str(input("Enter Web Site Name: "))
    s = socket.gethostbyname(url)
    print(s + ": " + name + "\nGÖKTÜRK HACK TEAM")

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
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    sleep(5)
    print("Your IP: " + ip)

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

def pcname():
    name = socket.gethostname()
    print(f"Your Computer Name: {name}")

print("1: Find Web IP\n2: Scan Web Port\n3: Web Server Send To Data\n4: My IP\n5: My Find Port\n6: My Computer Name\n7: Who Are We")

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
    open()
else:
    print("Enter a Valid Number")