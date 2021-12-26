"lib to make rest calls"
import requests
"3rd part web scraping tool"
from bs4 import BeautifulSoup
"making a get request to wikipedia page"
html = requests.get("https://en.wikipedia.org/wiki/Machine_learning")
"scraping the web page"
bsObj = BeautifulSoup(html.content, "html.parser") 
"printing h1 object"
print(bsObj.h1.string)

"getting all a tags with href and printing out them"
for a in bsObj.find_all('a', href=True):
    print (a['href'])
    """links=bsObj.find_all('a')
for link in links:
    print(link.get('href'))"""
