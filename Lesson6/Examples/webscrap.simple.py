import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/Web_scraping")
bs = BeautifulSoup(response.text,"lxml")
file = open("output.txt","w")


#get all the parapgaphs
for paragraph in bs.find_all("p"):
    print(paragraph.text)
    #write content to file
    file.write(paragraph.text)


file.close()