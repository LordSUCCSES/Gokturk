#Oluşturucu LordSUCCSES
#Geliştirici Utq-li

#discord : Utq-li15101#1830 | lordsuccses

import os
from requests.exceptions import RequestException

try:
    print("Update is starting... GOKTURK HACK TIM")
    os.system("git clone https://github.com/LordSUCCSES/Gokturk.git")
except RequestException as e:
    print(f"İnternet bağlantısı hatası: {e}")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
