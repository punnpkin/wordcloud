'''
import json
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import random

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

def loadContent(file_name):
    contentList = []
    f = open(file_name, encoding='utf-8')
    content = json.load(f)
    for i in content.keys():
        #print (content[i][2])
        contentList.append(content[i][0])
    print (len(contentList))
    return "".join(contentList)

def cutWord(contenText):
    segList = jieba.cut(contenText, cut_all=True)
    return " ".join(segList)

def main():
    contenText = loadContent('info.json')    cutText = cutWord(contenText)
    print (cutText)
    #drawWordcloud(cutText)

if __name__ == '__main__':
    main()
'''