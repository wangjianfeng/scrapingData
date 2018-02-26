from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re
import random

pages = set()
def getYearLinks(baseUrl,typeCode):

