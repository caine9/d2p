# !/usr/bin/python
import re #regular expression
import urllib #open any resources by URL
import os #operating systen
# apiKey FDA7423D18A5DECCA2C8BD169361941A
# steamID 76561198062810172
# ID 102544444

# test URL 
hero_url="http://www.dota2.com.cn/heroes/index.htm"
item_url="http://www.dota2.com.cn/items/index.htm"
hero_reg=r"/images/heroes/.*_sb\.png"
item_reg=r"/images/.*_lg\.png"

#抓取网页
def getHTML(url):
	page=urllib.urlopen(url)
	html=page.read()
	return html

#正则抓图片
def getImg(res,reg):
	a=re.compile(reg)

	return re.findall(a,res)
	
#下载并命名
def getHeroesDownloaded(list):
	prefix="http://www.dota2.com.cn"
	for i in list:
		reg=r"(?<=heroes/).*(?=_sb)"
		a=re.compile(reg)
		b=re.findall(a,i)
		path='D://py/img/heroes/'+b[0]+'.png'

		urllib.urlretrieve(prefix+i,path)

def getItemsDownloaded(list):
	prefix="http://www.dota2.com.cn"
	for i in list:
		reg=r"(?<=images/).*(?=_lg)"
		a=re.compile(reg)
		b=re.findall(a,i)
		print b[0]
		if 'moon' in b[0] or 'lotus' in b[0]: 
			continue
		path='D://py/img/items/'+b[0]+'.png'
		urllib.urlretrieve(prefix+i,path)
		
		
# 运行函数
hero_res=getHTML(hero_url)
item_res=getHTML(item_url)
	
hero_list=getImg(hero_res,hero_reg)
item_list=getImg(item_res,item_reg)

# getHeroesDownloaded(hero_list)
getItemsDownloaded(item_list)
