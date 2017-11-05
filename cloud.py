



import json
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import random

'''
def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
'''
def loadContent(file_name):
    contentList = []
    f = open(file_name, encoding='utf-8')
    content = json.load(f)
    for i in content.keys():
        #print (content[i][2])
        contentList.append(content[i][3])
    print (len(contentList))
    return "".join(contentList)

def cutWord(contenText):
    segList = jieba.cut(contenText, cut_all=True)
    return " ".join(segList)

def drawWordcloud(cutText):
    backgroudImage = plt.imread('elephant.jpg')
    cloud = WordCloud(background_color = 'white',           # 设置背景颜色
                mask = backgroudImage,                      # 设置背景图片
                max_words = 2000,                           #设置最大现实的字数
                font_path=('simhei.ttf'),                   # 设置字体格式，如不设置显示不了中文
                max_font_size = 60,                         # 设置字体最大值
                #scale=1.5,
                collocations=False,
                random_state = 10)                           # 设置有多少种随机生成状态，即有多少种配色方案
    wordCloud = cloud.generate(cutText)
    #plt.imshow(wordCloud.recolor(color_func=grey_color_func, random_state=3))
    wordCloud.to_file("cloud.jpg")


def main():
    contenText = loadContent('info.json')
    cutText = cutWord(contenText)
    drawWordcloud(cutText)

if __name__ == '__main__':
    main()
