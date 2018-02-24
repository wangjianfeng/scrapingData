#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/2/24

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj = BeautifulSoup(html)

#打印出子标签children
# for child in bsobj.find("table",{"id":"giftList"}).children:
#     print(child)

#打印出后代标签descendants
# for descendant in bsobj.find("table",{"id":"giftList"}).descendants:
#     print(descendant)

#打印出第一行以外的所有兄弟行next_siblings
for sibling in bsobj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)