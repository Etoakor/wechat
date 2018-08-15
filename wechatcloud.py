import itchat
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import numpy as np
import PIL.Image as Image
from os import path

signlist = []
itchat.auto_login()  # 登录微信
friends = itchat.get_friends(update=True)[0:]
for i in friends:
    signature = i['Signature'].strip().replace('span','').replace('class','').replace('emoji','').replace('\n', '')\
        .replace('\"','')  # 去除无用字符
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub('', signature)
    signlist.append(signature)
text = "".join(signlist)

# 分词
cut = jieba.cut(text,cut_all=True)
word = ",".join(cut)
print(word)

# 绘制词云
coloring = np.array(Image.open("/Users/zhangxianan/Desktop/tu/1.jpg"))    #电脑中自定义词云的图片
my_wordcloud = WordCloud(background_color="white", max_words=2000, max_font_size=70,
                         mask=coloring, random_state=48,font_path='STFANGSO.ttf',
                         scale=2).generate(word)  # 定义词云背景图颜色、尺寸、字体大小、电脑中字体选择,random_state 为每个单词返回一个PIL颜色
image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))  #绘图颜色
plt.imshow(my_wordcloud)   # 绘图内容
plt.axis("off")
plt.show()  # 显示图
d = path.dirname(__file__)   # project 当前目录
my_wordcloud.to_file(path.join(d, 'cloud.png'))