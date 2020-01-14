#coding:utf8
from bs4 import BeautifulSoup
import re
import urlparse
#总调代码
class SpiderMain(object):
	def _init_(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloder.HtmlDownloader()
		self.parser = html_parser = html_parser.Html_parser()
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self,root_url):
		cont = 1
		self.urls.add_mew_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print ('craw %d : %s'(count,new_url))
				html_cont = self.downloader.download(new_url)
				new_urls,new_data = self.parser.parse(new_url,html_cont)
				self.urls.add_mew_urls(new_urls)
				self,outputer.collect_data(new_data)

				if count == 1000:
					break
				count = count+1
			except:
				print ('crae failed')

		self.outputer.output_html()
#url管理器
class UrlManager(object):
	def _init_(self):
		self.new_urls = set()
		self.old_urls = set()

	def add_new_url(self,url):
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	def add_new_urls(self):
		if urls is None or len(urls) == 0:
			return
		if url in urls:
			self.add_new_url(url)

	def has_new_url(self):
		return len(self.new_urls) != 0

	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url
#下载器
class HtmlDownloader(object):
	def downlosd(self,url):
		if url is None:
			return None
		response = urllib2.urlopen(url)
		if response.getcode()!= 200:
			return None
		return response.read()
#解析器
class HtmlParser(object):
	def _get_new_urls(self,page_url,soup):
		new_urls = set()
		links = soup.find_all('a',herf=re.compile(r"/view/\d+\.htm"))
		for link in links:
			new_url = link['herf']
			new_full_url = urlparser.urljoin(page_url,new_url)
			new_url.sdd(new_full_url)
		return new_urls


	def _get_new_data(self,page_url,soup):
		res_data = {}
		res_data['url'] = page_url
		title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
		res_data['title'] = title_node.get_text()
		summary_node = soup.find('div',class_="lemma-summary")
		res_data['summary'] = summary_node.get_text()
		return res_data


	def parse(self,page_url,html_cont):
		if page_url is None or html_cont is None:
			return
		soup = BeautifulSoup(html_cont,'html_parser',from_encoding='utf-8')
		new_urls = self.get_new_urls(page_url,soup) 
		new_data = self.get_new_data(page_url,soup)
		return new_urls,new_data
#输出
class HtmlOutputer(object):
	def _init_(self):
		self.datas = []

	def collect_data(self,data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):
		fout = open ('output.html','w')
		fout.write("<html>")
		fout.write("<body>")
		fout.write("<table>")
		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td>%s</td>"%data['url'])
			fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
			fout.write("<td>%s</td>"%data['summary'].encode('utf-8'))
			fout.write("</tr>")
		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")
		fout.close()





if _name_=="_main_":
	root_url="https://baike.baidu.com/item/Python/407313?fr=aladdin"
	obj_spider=SpiderMain()
	obj_spider.craw(root_url)
