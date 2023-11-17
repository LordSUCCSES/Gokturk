#Oluşturucu LordSUCCSES
#Geliştirici Utq-li

#discord : Utq-li15101#1830 | lordsuccses

import os
import time

from requests.exceptions import RequestException

try:
    print("Update is starting... GOKTURK HACK TIM")
    os.system("git clone https://github.com/LordSUCCSES/Gokturk.git")
    os.system("clear")
    print("Update is finished! GOKTURK HACK TIM")
    time.sleep(1.5)
    print("Opening the tool...")
    time.sleep(2.5)

    try:
        with open('gokturk.py', 'r') as file:
            code = compile(file.read(), 'gokturk.py', 'exec')
            exec(code)
    except FileNotFoundError:
        print("gokturk.py dosyası bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")


except RequestException as e:
    print(f"İnternet bağlantısı hatası: {e}")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
