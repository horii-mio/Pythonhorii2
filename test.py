# Pythonhorii2
#そのままだとssl認証エラーが発生するため追記
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#

import urllib.request
from bs4 import BeautifulSoup
req = urllib.request.urlopen("http://quality-start.in/company/")
soup = BeautifulSoup(req,"html.parser")
divtab = soup.find("div",class_="list-group")
array = []
array = divtab.find_all("a",class_="list-group-item")

for v in array:
    print(v.string)
#testだよ
#topic1だよ
