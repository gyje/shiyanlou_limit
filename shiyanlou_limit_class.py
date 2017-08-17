base_url="https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&order=latest&page="
headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Cookie':'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
'Host':'www.shiyanlou.com',
'Referer':'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&order=latest&page=2',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
import requests,gevent,gevent.monkey,time
from pyquery import PyQuery as pq
from threading import Thread
gevent.monkey.patch_socket()
def get_limit(doc_content):
	content=doc_content(".col-sm-6")
	temp=content.find(".limited-label")
	par=temp.parents(".col-sm-6")
	if r"限免" in temp.text():
		for i in range(10):
			num=i
			limittime=par.find(".limited-label").eq(num).text()
			limittitle=par.find(".course-name").eq(num).text()
			limitcontent=par.find(".course-desc").eq(num).text()
			limit=limittime+"\n"+limittitle+"\n"+limitcontent+"\n"
			if limit=="\n\n\n":
				break
			else:
				print (limit)
def check_single_page(page_url):
	temp=pq(requests.get(page_url,headers=headers).text)
	get_limit(temp)
def run():
	taske=[gevent.spawn(check_single_page,base_url+str(u)) for u in range(1,21)]
	gevent.joinall(taske)
def threadrun():
	for i in range(1,21):
		t=Thread(target=check_single_page,args=(base_url+str(i),))
		t.start()
if __name__=="__main__":
	threadrun()
