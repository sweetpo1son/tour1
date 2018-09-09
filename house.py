search='http://www.tmsf.com/newhouse/property_searchall.htm?searchkeyword=&keyword=&sid=&districtid=&areaid=&dealprice=&propertystate=&propertytype=&ordertype=&priceorder=&openorder=&view720data=&page=1&bbs=&avanumorder=&comnumorder='
neww='http://www.tmsf.com/newhouse/property_330184_20333706_price.htm'

u='http://www.tmsf.com/index.jsp'
import urllib.request
from bs4 import BeautifulSoup
import re
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=u, headers=headers)
with urllib.request.urlopen(req) as url:
    s=url.read()
soup = BeautifulSoup(s)

big=soup.find(id='myCont14')
newhouse=big.find_next()

for x in newhouse.find_all('a'):
    community(x['href'])


def community(ur):
    useful='http://www.tmsf.com'+ur[:-8]+'price.htm?page='
    count=0
    while True ：
        count+=1
        try:
            req = urllib.request.Request(url=useful+str(count), headers=headers)
            with urllib.request.urlopen(req) as url:
                s=url.read()
        except:
            break
        soup = BeautifulSoup(s)
        