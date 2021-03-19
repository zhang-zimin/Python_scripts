import requests
from requests.sessions import session

url = 'https://liulissr.name/auth/login'
payload = {
    'email':'641945043@qq.com',
    'passwd':'zhang19961029',
}

def login():
    s = requests.session()
    res = s.post(url,data = payload)
    print(res.status_code)

login() 
