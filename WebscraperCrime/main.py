import requests
from bs4 import BeautifulSoup
import time
index = 0
page=1
durl = "https://www.foxla.com/"
url = 'https://www.foxla.com/tag/crime-publicsafety'
import json
f = open('history.json')
data = json.load(f)
print(data)
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
            name=soup.find('span',{"class":"dateline"}).text[:-3]
            print((name))
            index=index+1
            if name in data:
              d = ({name:data[name]+1})
            else:
          	  d = {name:1}
            data.update(d)
            data2 = json.dumps(data)
            print(data2)
            jsonFile = open("history.json", "w+")
            jsonFile.write(json.dumps(data))
            jsonFile.close()
        except:
            index=index+1
