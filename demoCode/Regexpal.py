#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/2/24
#正则表达式Demo


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj = BeautifulSoup(html)
for img in bsobj.findAll("img",{"src":re.compile("\.\./img/gifts/img.*\.jpg")}):
    print(img['src'])

