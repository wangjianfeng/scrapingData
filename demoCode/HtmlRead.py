from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        # html.read()读取HTML内容
        bsobj = BeautifulSoup(html.read())
        #title = bsobj.body.h1
        title = bsobj.contents
    except AttributeError as e:
        return None

    return title

title = getTitle("http://data.stats.gov.cn/tablequery.htm?m=QueryData&code=AD0D&wds=%5B%7B%22wdcode%22%3A%22reg%22%2C%22valuecode%22%3A%22000000%22%7D%5D")
if title == None:
    print("Title could not be found")
else:
    print(title)
