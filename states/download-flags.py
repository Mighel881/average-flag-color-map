import requests
import urllib
from bs4 import BeautifulSoup
import os

#Creating dir
if not os.path.isdir("flags/"):
    os.mkdir("flags/")

#Page that lists the country codes
url = "https://en.wikipedia.org/wiki/Flags_of_the_U.S._states_and_territories"

#downloading the page and creating beautiful soup object
page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")

#iterating through all the images 
for img in soup.find("ul",class_="gallery mw-gallery-nolines nochecker").find_all("img"):
    #the image alt text or the title contains "flag"
    if "flag" in img.get("alt","").lower() or "flag" in img.get("title","").lower():    

        #get state name
        state = img.parent.parent.parent.find("div",class_="gallerytext").find_all("a")[1].text

        #logging progress
        print (state)

        #Adjust url and download image. once downloaded no need to scan for more images
        imgSrc = "https:"+img.get("src")
        urllib.urlretrieve(imgSrc,"flags/{}.png".format(state))
        




