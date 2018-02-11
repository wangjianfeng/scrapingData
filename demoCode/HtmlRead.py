from urllib.request import urlopen
from bs4 import BeautifulSoup


#html = urlopen("http://www.pythonscraping.com/pages/page1.html")
html = urlopen("http://www.sina.com")
#html.read()读取HTML内容
bsobj = BeautifulSoup(html.read())
#打印网页的js脚本
print(bsobj.script)