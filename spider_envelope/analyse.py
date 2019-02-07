# !/usr/bin/python3
# -*- coding: utf-8 -*-
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud
with open('/home/kevin/title.txt', 'r') as f:
    content = f.read()
tags = jieba.cut(content)
result = ' '.join(tags)
# 初始化图云的一些参数
stopWord = set(map(str.strip, open('/home/kevin/stopword.txt', 'r').readlines()))
# bg_img = plt.imread('/home/kevin/peiqi.png')
plt.imshow(bg_img)
plt.axis('off')
plt.show()
font = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
wc = WordCloud(
    background_color='white',  # 白色背景
    font_path=font,            # 中文字体，否则显示不了
    stopwords=stopWord,        # 设置停用词
    max_font_size= 200,        # 最大字体的尺寸
    random_state= 50,          # 随机状态的个数
    max_words= 100,            # 最多显示的词数
)
# 创建图云
wc.generate_from_text(result)
# 显示图云
plt.imshow(wc)
plt.axis('off')
plt.figure()
plt.show()
wc.to_file('/home/kevin/rst.png')