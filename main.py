from bs4 import BeautifulSoup
import requests
import time
from urllib.parse import urlencode
from re import match, findall

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    'Accept-Language': 'en-US,en;q=0.5',
}
query = "Monolithic architecture"
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
params['tbs'] = ','.join(tbs_param)
params = urlencode(params)
https = int(time.time()) % 2 == 0
bare_url = u"https://www.google.com/search?" if https else u"http://www.google.com/search?"
url = bare_url + params
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
divs = soup.findAll("div", attrs={"class": "g"})
results_div = soup.find("div", attrs={"id": "resultStats"})
results_div = soup.find("div", attrs={"class": "g"})
results_div_text = results_div.get_text()
if results_div_text:
    regex = r"((?:\d+[,\.])*\d+)"
    m = findall(regex, results_div_text)
    num = m[0].replace(",", "").replace(".", "")
    number_of_results = int(num)
else:
    number_of_results = 0
j = 0
print(results_div_text)
for li in divs:
    print(li)
    # res.page = i
    # res.index = j

    # res.name = _get_name(li)
    # res.link = _get_link(li)
    # res.google_link = _get_google_link(li)
    # res.description = _get_description(li)
    # res.thumb = _get_thumb()
    # res.cached = _get_cached(li)
    # res.number_of_results = number_of_results
    # res.is_pdf = _get_is_pdf(li)
    
    # if void is True:
    #     if res.description is None:
    #         continue
    # results.append(res)
    # j += 1

