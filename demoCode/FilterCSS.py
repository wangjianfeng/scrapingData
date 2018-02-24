#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/2/12

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def getInfoByFilterCSS(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj = BeautifulSoup(html)
        nameList = bsobj.findAll("span",{"class":"green"})
        for name in nameList:
            #get_text()清除HTML文档中的所有标签
            print(name.get_text())
    except AttributeError as e:
        return None

    #return title

getInfoByFilterCSS("http://www.pythonscraping.com/pages/warandpeace.html")

