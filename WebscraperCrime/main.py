import requests
from bs4 import BeautifulSoup
import time
index = 0
page=1
durl = "https://www.foxla.com/"
url = 'https://www.foxla.com/tag/crime-publicsafety'
while True:
    if(index > 19):
        print("stop")
        time.sleep(2)
        page = page + 1
        url = 'https://www.foxla.com/tag/crime-publicsafety'
        url = url + "?page=" + str(page)
        index=0

    else:
        try:

            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            print((soup.findAll('h3', attrs={"class":"title"})[index].string))
            x = (soup.findAll('h3', attrs={"class":"title"})[index])
            for a in x.find_all('a', href=True):
                print( "Found the URL:", a['href'])
                _durl = a['href']
            url2=durl+_durl
            response = requests.get(url2)
            soup = BeautifulSoup(response.text, 'html.parser')
            print((soup.find('span',{"class":"dateline"}).text)[:-3])
            index=index+1
        except:
            index=index+1

