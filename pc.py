import requests

newsurl = 'http://news.sina.com.cn/china/'
res = requests.get(newsurl)
print(res.text)