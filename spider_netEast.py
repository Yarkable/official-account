# -*- coding: utf-8 -*-
import os
import json
import requests
from bs4 import BeautifulSoup



# 加入请求头防止反爬虫
headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}


def mkdir(path):
	fold = os.path.exists(path)
	if not fold:
		os.mkdir(path)
	return path


def get_rsp(url):
	rsp = requests.get(url, headers = headers).text
	# 将获取到的 HTML 文本转化成 soup 对象
	soup = BeautifulSoup(rsp, 'lxml')
	# 匹配出歌曲 id 所在部分的文档树
	soup_name = soup.find('ul', class_ = "f-hide")
	# 找出其中所有的 a 元素，进行下一步筛选
	data = soup_name.find_all('a')
	return data


# singers = []
# aut = json.loads(soup.find('textarea').text)
# for item in aut:
# 	artists = item['artists']
# 	for author in artists:
# 		singers.append(author['name'].replace('\xeb', ''))

# print(singers)


def get_info():
	song_id = []
	song_name = []
	# 访问 BillBoard 榜单页面
	url = 'https://music.163.com/discover/toplist?id=60198'
	for item in get_rsp(url):
		# 对 id 属性值进行切片，获取真正的 id
	    ID = item.get('href')[9:]
	    # 歌曲名就在 a 标签的文本中
	    name = item.text
	    song_id.append(ID)
	    song_name.append(name)
	# 用 tuple 返回 id 和 name 列表
	return song_id, song_name


def download(id):
	# 构建 url ，进行 HTTP 请求
	url = 'http://music.163.com/api/song/enhance/player/url'
	params = {
		'id' : id,
		'ids' : '[' + id + ']',
		'br' : '3200000'
	}
	# 捕捉异常，防止获取不到下载 url
	try:
		down_page = requests.get(url, headers = headers, params = params).json()
		down = requests.get(down_page['data'][0]['url'], headers = headers)
		print('Downloading->' + down.url)
	# 如果出异常就直接退出
	except:
		return None

	return down.content


def main():
	# 初始化参数
	ids = get_info()[0]
	names = get_info()[1]
	path = mkdir('G:/netEast_songs/')
	flag = 0
	for page in ids:
		content = download(page)
		with open(path + '%s.mp3' % names[flag].replace('*', 'I'), 'wb') as f:
			# 如果内容是空的就不写入，直接跳过
			if content:
				f.write(content)
			else:
				pass
		print('\nSucceeded!')
		print('=====================================================================================================================')
		flag += 1

if __name__ == '__main__':
	main()



