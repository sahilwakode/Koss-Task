import asyncio 
import time
import urllib2
from bs4 import BeautifulSoup       #libraries imported
url="https://reqres.in/api/users?page{el}"

page=urllib2.urlopen(url)      #opening url in page

a=BeautifulSoup(page)        # substituting the values

print(a.prettify())     #print



