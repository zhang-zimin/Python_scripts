import requests
from bs4 import BeautifulSoup

class douban:
    def __init__(self):
        self.url = 'https://movie.douban.com/top250'
        self.startnum = [i for i in range(0,251,25)]
        self.header = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36'}

    def get_top250(self):
        for start in self.startnum:
            start = str(start)
            html = requests.get(self.url,params={'start':start},headers=self.header)
            soup = BeautifulSoup(html.text,'html.parser')
            names = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-child(1)')
            # with open('movie.txt','w') as f:
            for name in names:
                print(name.get_text())
                # f.write(name.get_text())
if __name__ =='__main__':
    cls = douban()
    cls.get_top250()
