from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import json

def getJsonContent(url):
    try:
        response = urlopen(url).read().decode('utf-8')
        responseJson = json.loads(response)
    except HTTPError as e:
        return None

    return responseJson.get("returndata")

url = "http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A030701%22%7D%5D&k1=1519624234568"
jsonobj1 = getJsonContent(url)
for json in jsonobj1['datanodes']:
    print(json['data']['strdata'])

