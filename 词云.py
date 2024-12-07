# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年10月25日
"""
import jieba
from jieba import lcut
import jieba.analyse
import wordcloud

c = wordcloud.WordCloud()
f = open("红迪.csv", "r", encoding='ANSI')
t = f.read()
f.close()
ls = lcut(t)
txt = "".join(ls)
# w = wordcloud.WordCloud(font_path="msyh.ttc",
#                         width=1000, height=700,
#                         background_color="white",
#                         max_words=20)
# w.generate(txt)
# w.to_file("py_wordcloud.png")
stop_words = ['嗨','好','但是','老实说','然而','ako','这正常吗','ko','大家好','你', '我', '的', '了', '们', '知道', '一个', '没有', '只是', '因为']
ciyun_words = ''

for word in txt:

    if word not in stop_words:
        ciyun_words += word

# 权重分析
tag = jieba.analyse.extract_tags(sentence=ciyun_words, topK=10, withWeight=True)
print(tag)


# 设置参数，创建WordCloud对象
wc = wordcloud.WordCloud(
    font_path='msyh.ttc',  # 中文
    background_color='white',  # 设置背景颜色为白色
    stopwords=stop_words,  # 设置禁用词，在生成的词云中不会出现set集合中的词

)
# 根据文本数据生成词云
wc.generate(ciyun_words)
# 保存词云文件
wc.to_file('img.jpg')