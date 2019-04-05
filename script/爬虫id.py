import urllib.request
import json
from threading import Timer
from datetime import datetime
import os
import time
import random
import requests
proxy ={
	"http":"",
}
startid=912000000

def getip():
	turl = "http://api.ip.data5u.com/dynamic/get.html?order=436eb43459ff51b21500492057dbe343&json=1&sep=3"
	try:
		res = requests.get(turl, timeout=10).json()
		for item in res['data']:
			proxy['http'] = 'http://' + item['ip'] + ':' + str(item['port'])
	except Exception as e:
		print("请求ip池")
		time.sleep(1)
		getip()

def geturl():pass
def getvalue():
	pass
def getdata(base, num):

	# 处理所有参数
	print(base)
	a = set()
	i = 7
	proxy['http'] = 'http://61.135.217.7'
	while len(a)<num:

		url = "http://www.chinaports.com/shiptracker/shipinit.do"
		USER_AGENTS = [
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"
			"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
			"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
			"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
			"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
			"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
		]
		user_agent = random.choice(USER_AGENTS)
		headers = headers = {'User-Agent': USER_AGENTS[0]}
		userid = base + i
		try:
			print(proxy)
			values = {'method':'shipInfo','userid':userid,'source':'0','num':'155116352359',}
			data = urllib.parse.urlencode(values).encode('utf-8')
			request = urllib.request.Request(url, data = data, headers = headers)
			response = urllib.request.urlopen(request)
		except Exception as e:
			print("换ip")
			time.sleep(2)
			getdata(startid+i, 100000)
			break
		html = response.read().decode('utf-8')
		print(html)

		arr = html.replace('"',"").replace("[","").replace("]","").split(", ")
		number=0
		for shipdata in arr:
			if shipdata== "null" or shipdata=="0" or shipdata=="":
				number=number+1
		if arr[0]!="" and arr[1] not in a and arr[1]!="null" and number <17:
			print("ok")
			a.add(arr[1])
			#with open("./shipinfo.json",'w',encoding='utf-8') as json_file:
			#	json.dump(shipinfo,json_file,ensure_ascii=False)
			#时间设置

			#with open("./shipdyna.json",'w',encoding='utf-8') as json_file:
			#	json.dump(shipdyna,json_file,ensure_ascii=False)
			with open("./id.txt",'a',encoding='utf-8') as idtxt:
				idtxt.write(str(userid)+"\n")
			#操作数据库
			print(i)
		i = i +14
		if (i-7)%200==0:

			time.sleep(2)
			print(str(i)+"_______")
			time.sleep(2)
			print("_______")


if __name__ == "__main__":
	now = datetime.now()
	print(now.hour, now.minute)
	getdata(startid, 100000)
	# 每隔3小时检测一次
	#系泊状态则间隔时间稍长一些
