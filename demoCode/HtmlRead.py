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

title = getTitle("http://data.stats.gov.cn/easyquery.htm?m=getOtherWds&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&k1=1519630280957")
if title == None:
    print("Title could not be found")
else:
    print(title)
