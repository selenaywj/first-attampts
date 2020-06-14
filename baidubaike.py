from bs4 import BeautifulSoup
from urllib.request import urlopen
import random
import re

base_url = "https://baike.baidu.com"
his = ["/item/%E4%B8%81%E7%A6%B9%E5%85%AE"]

for i in range(20):
    url = base_url+his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup= BeautifulSoup(html,features='lxml')
    print(i, soup.find('h1').get_text(),'    url: ', his[-1])

    sub_urls = soup.find_all("a",{"target":"_blank","href":re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls,1)[0]['href'])
    else:
        his.pop()

