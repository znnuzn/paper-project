# coding:utf-8
# 中国新闻网 危化品 http://www.bj.chinanews.com/
# py-2
import re
import urllib
import requests
hea = {'User-Agent':'Moczilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3223.8 Safari/537.36'}
html = requests.get('http://search.sina.com.cn/?c=news&ie=utf-8&q=%E5%8D%B1%E5%8C%96%E5%93%81%E4%BA%8B%E6%95%85&col=&range=&source=&from=&country=&size=&time=&a=&page=5&pf=2131425449&ps=2134309112&dpc=1',headers = hea)
page = 5
s = 'http://search.sina.com.cn/?c=news&ie=utf-8&q=%E5%8D%B1%E5%8C%96%E5%93%81%E4%BA%8B%E6%95%85&col=&range=&source=&from=&country=&size=&time=&a=&page='
w = '&pf=2131425449&ps=2134309112&dpc=1'
while page <= 15:
    page = page + 1
    url = s+str(page)+w
    con = urllib.urlopen(url).read()
    title = re.findall(r'<p class="content">(.*?)<span style="color:#C03">', con)
    time = re.findall(r'</span>(.*?)<span style="color:#C03">', con)
    uurl = re.findall(r'<h2><a href="(.*?)" target="_blank">', con)
    with open('D:/Python/ziliao/weihuapin2.txt', 'a') as f:
       #   print  e in title:
        for e in title:
            f.write(e) 
            f.write("\n")
            print (e)
       #   print '时间'
        for l in time:
            f.write(l)
            f.write("\n")
            print (l)
       #   print '时间'
        for h in uurl:
            f.write(h)
            f.write("\n")
            print (h)

