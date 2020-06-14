import requests
from lxml import etree
from pyquery import PyQuery as py

travel_name = input("请输入你要查询的一日游旅游地信息")
for page in range(1,4):
    url = 'https://piao.qunar.com/daytrip/list.htm?keyword={}&region=&from=mdl_search&sort=&page={}'.format(travel_name,page)
print(url)

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36"
}

res = requests.get(url,headers= headers).text
doc = py(res)
name = doc(".name").items()
sight_item_price=doc(".sight_item_price").items()
relation_count=doc(".relation_count").items()

for x,s,f  in zip(name,sight_item_price,relation_count):
    name1 = x.text()
    sight_item_price1 = s.text()
    relation_count1 = f.text()
    travel = (name1+sight_item_price1+relation_count1)
    print(travel)
    f = open('./'+' {}一日游'.format(travel_name)+'.txt',"a",encoding="utf-8")
    f.write(travel+"/n")
    f.close()
