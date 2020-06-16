
import requests
from bs4 import BeautifulSoup

link=requests.get("https://en.wikipedia.org/wiki/Deep_learning")   #opening the link using requests.get
bs=BeautifulSoup(link.content,"html.parser")                       #Using beautifulsoup parsing html content in link
print(bs.title.string)                                             #getting only string content from title tag
#print(bs.find_all('a'))
for link in bs.find_all('a'):                                      #looping through tags in all over link
    x=link.get('href')                                             #from that tags getting href attribute content
    file=open("links.txt","a+")                                    #opening file in append mode
    file.write(str(x))                                             #writing the links to file
    file.write("\n")
print("writing to file completed")
file.close()