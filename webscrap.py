import requests
from bs4 import BeautifulSoup

#fatch the web pages

url= "https://edunetfoundation.org/"
response=requests.get(url)

#check if the request is suceessful

import requests
from bs4 import BeautifulSoup

#fetch the web pages
url="https://edunetfoundation.org/"
response=requests.get(url)

#check if the request is successful
if response.status_code == 200:
    print("Successfully fetched the web page")
else :
    print("Failed")

#parse the HTML Content
soup=BeautifulSoup(response.text, "html.parser")




#extact Data
title=soup.title.string
print(f"Page Title:{title}")



# extract hyperlinks

links=soup.find_all("a")
for link in links:
    herf =link.get("herf")
    text= link.get_text()
    print(f"Link text : {text},URL:{herf}")



import csv
links=soup.find_all("a")
with open("website_links.csv","w",newline="",encoding="utf-8") as file:
    writer=csv.writer(file)
 
    writer.writerow(["Link Text","URL"])
 
    for link in links:
        href=link.get("href")
        text=link.get_text(strip=True)
        writer.writerow([text,href])
 
print("Link saved successfully")

