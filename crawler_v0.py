# !/usr/bin/python
import re #regular expression
import urllib #open any resources by URL
# apiKey FDA7423D18A5DECCA2C8BD169361941A
# steamID 76561198062810172
# ID 102544444

# test URL 
turl="https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=FDA7423D18A5DECCA2C8BD169361941A&matches_requested=1&&account_id=102544444&format=XML"

def getHTML(url):
	page=urllib.urlopen(url)
	html=page.read()
	return html
	
print getHTML(turl)

