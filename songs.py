songKeyWord = input("Enter song/artist : ").strip().split(" ")
# https://gaana.com/search/enjoy%20the%20ride
url = "https://gaana.com/search/songs/"
for i in songKeyWord:
    url+=i+"%20"
url = url[:(len(url)-3)]

import requests
from bs4 import BeautifulSoup
import webbrowser
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')

mainDiv = soup.find('div', class_="songlist-type2")
songList = mainDiv.findAll('h3', class_="item-heading")
songLinkList = []
index = 1
print("Here are some matching results ")
for i in songList:
    print(str(index)+". "+i.find('a').get_text())
    songLink = i.find('a')["href"]
    songLinkList.append(songLink)
    index+=1
song = int(input("Choose a song : "))
print(webbrowser.open(songLinkList[song-1]))
