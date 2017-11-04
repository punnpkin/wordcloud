#!Python
# code=utf-8

'''
author:nevil
date:20171101
version:0
'''

import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePageList(ilt, html):
    try:
        urlList = re.findall(r'<a href="/xinwendaodu/\d{4}\-\d+\-\d+/\d+.html" style="color:#00508f;"', html)
        #print (urlList)
        for i in range(len(urlList)):
            url = urlList[i][22:-24]
            ilt.append('http://news.ustb.edu.cn/xinwendaodu/'+url)
    except:
        return ""



def main():
    depth = 9
    start_url = 'http://news.ustb.edu.cn/xinwendaodu/'
    passageList = list()
    
    try:
        html = getHTMLText(start_url+'index.html')
        parsePageList(passageList, html)
    except:
        pass
    
    for i in range(depth):
        try:
            html = getHTMLText(start_url+'index_'+(str)(i+2)+'.html')
            parsePageList(passageList, html)
        except:
            pass
    
    print (len(passageList))
    
    urlList = open('urlList.txt', 'w')
    for i in passageList:
        urlList.write(i+'\n')

if __name__ == '__main__':
    main()