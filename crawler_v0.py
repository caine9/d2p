# !/usr/bin/python
import re #regular expression
import urllib #open any resources by URL
import MySQLdb #Connect to MySQL
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

#match details
https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?key=FDA7423D18A5DECCA2C8BD169361941A&match_id=1795548666
#heroes
https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key=FDA7423D18A5DECCA2C8BD169361941A&language=en_us

