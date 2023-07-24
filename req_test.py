import requests

payload = {'key1': 'value1', 'key2': 'value2'}

url = requests.post("http://httpbin.org/post", data=payload)
url.encoding = "UTF-8"
print(url.text)
'''
if url.status_code == requests.codes.ok:
    print(url.text)
'''    