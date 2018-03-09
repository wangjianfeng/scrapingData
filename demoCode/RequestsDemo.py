import requests

# response = requests.get("https://www.baidu.com")
# print(type(response))
# print(response.status_code)
# print(response.text)
# print(response.cookies)

data = {
    'name':'Alex',
    'age':37
}
response = requests.get("http://httpbin.org/get",params=data)
print(response.text)

response2 = requests.get("https://www.baidu.com")
for key,value in response2.cookies.items():
    print(key +'='+value)