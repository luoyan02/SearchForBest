# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os

if __name__ == "__main__":
    # 建立一个文件夹专门存储导师详情页的信息
    if not os.path.exists('./tutorLibs'):
        os.mkdir('./tutorLibs')
    # 指定url
    url = 'https://auto.ustc.edu.cn/25976/list.htm'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
    }
    # 发起请求并获取响应数据
    response = requests.get(url=url, headers=headers)
    response.encoding = "utf-8"
    page_text = response.text
    # 利用属性进行定位
    soup = BeautifulSoup(page_text, 'lxml')
    soup1 = soup.find('div', class_='left-mu02')
    soup2 = soup1.find_all('a', target='_blank')
    # 将soup2中页面详情页的链接和导师的姓名截取下来
    linklist = []  # 建立一个列表，用于存入详情页的连接
    namelist = []  # 建立一个列表，用于存入导师的姓名
    for x in soup2:
        link = x.get('href')  # 提取链接
        name = x.get('title')  # 提取名称
        linklist.append(link)  # 存入列表
        namelist.append(name)  # 存入列表
    # 遍历链表中每个链接，再次进行url请求，将导师详情页中的数据存入文档
    i = 0
    for path in linklist:
        FullPath = 'https://auto.ustc.edu.cn'+path  # 拼接得到详情页的完整url
        tutor_data = requests.get(url=FullPath, headers=headers)  # 发起请求并获取响应数据
        # 以源代码的形式存储
        tutor_data.encoding = 'utf-8'
        tutor_final_data = tutor_data.text
        # 生成导师信息的名称
        tutor_name = namelist[i]
        i += 1
        TutorPath = './tutorLibs'+'/'+tutor_name+'.html'
        # 为每一个导师详情页的信息建立一个html文件并存储在tutorLibs文件夹下
        with open(TutorPath, 'w', encoding="utf-8") as fp:
            fp.write(tutor_final_data)
            print(tutor_name, '下载成功')
