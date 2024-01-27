from bs4 import BeautifulSoup
import requests
import time
from urllib.parse import urlencode
from re import match, findall

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    'Accept-Language': 'en-US,en;q=0.5',
}
query = """site:jobs.lever.co AND 'Software Engineer'"""
page=0
per_page=10
lang='en'
area='com'
ncr=False
time_period="month"
sort_by_date=True
params = {
    'nl': lang,
    'q': query.encode('utf8'),
    'start': page * per_page,
    'num': per_page
}
time_mapping = {
    'hour': 'qdr:h',
    'week': 'qdr:w',
    'month': 'qdr:m',
    'year': 'qdr:y'
}
tbs_param = []
if time_period and time_period in time_mapping:
    tbs_param.append(time_mapping[time_period])
if sort_by_date:
    tbs_param.append('sbd:1')
params['country'] = "USA"
params['tbs'] = ','.join(tbs_param)
params = urlencode(params)
print(params)
https = int(time.time()) % 2 == 0
bare_url = u"https://www.google.com/search?" if https else u"http://www.google.com/search?"
url = bare_url + params
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
divs = soup.findAll("div", attrs={"class": "g"})
print(len(divs))
print(divs[0])
for li in divs:
    a = li.find('a')
    link = a["href"]
    print(link)