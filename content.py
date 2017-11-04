#!Python
# code=utf-8

'''
author:nevil
date:20171101
version:0
'''

import requests
import re
import json
from bs4 import BeautifulSoup
import datetime





def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    try:
        titleList = re.findall(r'<p class="bkrw_bt" style="font-size:18px; font-weight:bold;">.*</p>', html)
        sourceList = re.findall(r'\| 来源：.*?\|', html)
        dateList = re.findall(r'\| 更新时间：.*?\|', html)
        txtList = re.findall(r'<!--新闻正文-->[\s\S]*<!--新闻正文 end-->', html)
        
        title = titleList[0][61:-4]
        source = sourceList[0].split('：')[1].strip(' \|').strip('<a href=\'http://\' target=_blank>')
        date = dateList[0].split('：')[1].strip(' \|')
        txts = str(BeautifulSoup(txtList[0], 'lxml').get_text()).strip('\n')
        ilt.append([title, source, date, txts])
        
        #count = re.findall(r'', html)
    except:
        return ""

def main():
    starttime = datetime.datetime.now()
    #long running


    info = {}
    infoList = list()

    urlLists = open('urlList.txt')
    urlList = urlLists.readlines()
    for index,url in enumerate(urlList):
        url=url.strip('\n')
        html = getHTMLText(url)
        parsePage(infoList, html)
        info[index] = infoList.pop(0)
    
    print (len(info))
    
    with open("info.json",'w', encoding='utf-8') as json_file:
        json.dump(info, json_file, ensure_ascii=False)
    
    endtime = datetime.datetime.now()
    time = (endtime - starttime).seconds
    print ('耗时: ',time,' seconds')

if __name__ == '__main__':
    main()