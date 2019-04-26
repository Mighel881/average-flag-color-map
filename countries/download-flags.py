import requests
import urllib
from bs4 import BeautifulSoup
import os

#Creating dir
if not os.path.isdir("flags/"):
    os.mkdir("flags/")

#Page that lists the country codes
url = "https://en.m.wikipedia.org/wiki/ISO_3166-1_alpha-2"

#downloading the page and creating beautiful soup object
page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")

#going through each row in the table
for tr in soup.find_all("table")[2].find_all("tr")[1:]:

    #getting country code
    code = tr.td.get("id")

    #logging progress
    print (code)

    #Getting country wikipedia page
    wikiUrl = "https://wikipedia.org" + tr.a.get("href")
    wikiPage = requests.get(wikiUrl)
    wikiSoup = BeautifulSoup(wikiPage.text,"html.parser")
    
    #iterating through all images on the page
    for img in wikiSoup.find_all("img"):
        try:

            if "flag" in img.parent.get("title").lower():
            #the image alt text or the title contains "flag"
            #if "flag" in img.get("alt","").lower() or "flag" in img.get("title","").lower():    

                #Adjust url and download image. once downloaded no need to scan for more images
                imgSrc = "https:"+img.get("src")
                urllib.urlretrieve(imgSrc,"flags/{}.png".format(code))
                break
        except Exception as exc:
            print exc
    
