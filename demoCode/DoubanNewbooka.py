import requests
from requests.exceptions import RequestException
import re
import json

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<div.*?detail-frame.*?<a.*?>(.*?)</a>.*?color-lightgray">(.*?)</span>.*?color-gray">(.*?)</p>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'title':item[0],
            'point':item[1].strip(),
            'message':item[2].strip()
        }

def write_to_txt(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()


def main():
    url = 'https://book.douban.com/latest?icn=index-latestbook-all'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_txt(item)


if __name__ == '__main__':
    main()