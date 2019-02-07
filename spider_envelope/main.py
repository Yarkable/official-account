# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import requests
import json
from bs4 import BeautifulSoup

# 根据每一页url规律构造出url
def get_url(page):
    head = 'https://www1.szu.edu.cn/mailbox/list.asp?page='
    tail = '&leader=%CE%CA%CC%E2%CD%B6%CB%DF&tag='
    variable = str(page)
    url = head + variable + tail
    return url


def get_title(url):
    # 伪装成浏览器，防止封ip
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    # 进行认证，不然抓取到的不是真的页面
    # 如果访问不了可能是cookies过期了
    cookies = {
        'ASPSESSIONIDQAQSATRD': 'PMFKOKGDAPAHEJIMALKMOMNB',
        'ASPSESSIONIDSCQRBTRC': 'MKHHDMPDIODFAKJPEHFCJPPO',
        'ASPSESSIONIDQAQRBTQC': 'HMNFKDBAJAIDGGBLNGEKFEAL',
        'ASPSESSIONIDSARRBSRD': 'CNHPGNIAFOPDGAGAIJIBHHBC',
        'ASPSESSIONIDSCQSBSRD': 'PJIDPEKAFJIKIIEJHAPANAPL',
        'ASPSESSIONIDQCSTDRRC': 'BGKLGMLAPONIHGBJIFJLIDPE'
    }
    # 防止爬虫突然断掉，使其重复执行访问
    tries = 6
    while tries > 0:
        try: 
            rsp = requests.get(url, headers=headers, cookies=cookies)
            break
        except Exception as e:
            tries -= 1
            # print(e)
    # 防止中文乱码
    rsp.encoding = rsp.apparent_encoding
    data = rsp.text
    # 生成soup对象进行标签筛选
    soup = BeautifulSoup(data, 'lxml')
    soup_tag = soup.find_all('a', target="_blank" )
    title = []
    for item in soup_tag:
        name = item.text[1::]
        title.append(name)
    title.pop()
#     print(title)
    return title

def main():
    title_list = []
    for page in range(1, 140):
        link = get_url(page)
        titles = get_title(link)
        title_list += titles
        # print(title_list)
        
    # 写入txt文件中
    for title in title_list:
        with open('/home/kevin/title.txt', 'a') as f:
            f.write(title + '\n')

if __name__ == '__main__':
    main()
    