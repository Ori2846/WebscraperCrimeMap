import requests
from bs4 import BeautifulSoup
import time


index = 0
page=1
durl = "https://www.foxla.com/"
url = 'https://www.foxla.com/tag/crime-publicsafety'


import json
def WebScrape():
    #Index is used to indicate which story of the page is being used
    #Ex. Story 3 of page 1 would be index 4 page 1
    index = 0
    page = 1
    durl = "https://www.foxla.com/"
    url = 'https://www.foxla.com/tag/crime-publicsafety'
    f = open('history.json')
    data = json.load(f)
    while True:
        if (index > 19):
            print("stop")
            time.sleep(2)
            #If the page is done scraping go to the second page.
            page = page + 1
            url = 'https://www.foxla.com/tag/crime-publicsafety'
            url = url + "?page=" + str(page)
            index = 0

        else:
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                #Finding title of webpage
                print((soup.findAll('h3', attrs={"class": "title"})[index].string))
                x = (soup.findAll('h3', attrs={"class": "title"})[index])
                for a in x.find_all('a', href=True):
                    print("Found the URL:", a['href'])
                    _durl = a['href']
                url2 = durl + _durl
                #Gets Url
                response = requests.get(url2)
                #Once Url is obtained goes to story url
                soup = BeautifulSoup(response.text, 'html.parser')
                name = soup.find('span', {"class": "dateline"}).text[:-3]
                #Name var is the name of the city in California that the crime was comitted in
                print((name))
                index = index + 1
                #if name was found in data add 1 else set it as 1
                if name in data:
                    d = ({name: data[name] + 1})
                else:
                    d = {name: 1}
                #dumps data in json file
                data.update(d)
                data2 = json.dumps(data)
                print(data2)
                jsonFile = open("history.json", "w+")
                jsonFile.write(json.dumps(data))
                jsonFile.close()
            except:
                #If the webpage cannot find a crime go to the next story
                index = index + 1
WebScrape()
