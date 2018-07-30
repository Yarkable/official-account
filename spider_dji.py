#-*- coding: utf-8 -*-
import requests
import json
import os
import time

def get_links(offset):
	url = 'https://www.skypixel.com/api/v2/users/robomas-_user/works'
	# 设置请求头和请求参数
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
	params = {
	'lang': 'zh-CN', 
	'platform': 'web', 
	'device': 'desktop',
	'limit': 20,
	'offset': offset
	}
	response = requests.get(url, headers = headers, params = params)
	response.encoding = response.apparent_encoding
	return response.text


def mkdir(path):
	# 创文件夹存放文件
	folder = os.path.exists(path)
	if not folder:
		os.mkdir(path)
	return path


def get_detail():
	# 用link列表装视频链接
	link = []
	titles = []
	# 遍历json列表，爬取
	for offset in range(0, 160, 20):
		data = json.loads(get_links(offset))
		detail = data['data']['items']
		for lists in detail:
			title = lists['title']
			if('华南理工大学' in title or '哈尔滨工业大学' in title or '中国矿业大学' in title or '东北大学' in title or '哈工大' in title or '深圳大学' in title or'电子科技大学' in title):
				link.append('http:' + lists['cdn_url']['large'])
				titles.append(title)
	return link, titles


def main():
	# 初始化参数，获取链接列表和标题列表
	links = get_detail()[0]
	titles = get_detail()[1]
	flag = 0
	RM = mkdir('G:/RM2018_videos/')

	for i in links:
		# 写txt文件
		content = titles[flag] + '\n' + links[flag]
		with open(RM + 'dji_.txt', 'a') as f:
			f.write(content + '\n\n')
		# 写入视频文件
		print('Downloading No.%s video ....' % str(flag + 1))
		page = requests.get(links[flag]).content
		with open(RM + titles[flag] + '.mp4', 'wb') as f:
			f.write(page)
		print('No.%s video has been downloaded!' % str(flag + 1))
		flag += 1

if __name__ == '__main__':
	main()
