#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/2/24
# 通过对wiki百科进行单个域名信息的遍历
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

# html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
# bsobj = BeautifulSoup(html)

#version1.0
# for link in bsobj.findAll("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

#version2.0
# for link in bsobj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

#version3.0
random.seed(datetime.datetime.now())
def getLinks(articleURl):
    html = urlopen("https://en.wikipedia.org"+articleURl)
    bsobj = BeautifulSoup(html)
    return bsobj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0 :
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    getLinks(newArticle)