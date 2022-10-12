# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}


# 输入为导师的姓名，输出为导师详情页的源码信息，html格式
def get_tutor_url(tutorname):
    # 对自动化主页信息的爬取
    url = 'https://auto.ustc.edu.cn/25976/list.htm'
    response = requests.get(url=url, headers=headers)
    response.encoding = "utf-8"
    page_text = response.text
    # 利用bs4工具对爬取到的主页信息进行分析
    soup = BeautifulSoup(page_text, 'lxml')
    soup1 = soup.find('div', class_='left-mu02')
    soup2 = soup1.find('a', target='_blank', title=tutorname)
    if soup2==None:
        print('cannot find a tutor named' + tutorname)
        return None
    else:
        # 从主页源码上提取到各导师详情页的url
        path = soup2.get('href')
        fullpath = 'https://auto.ustc.edu.cn' + path
        # 利用得到的url再次发起请求对导师详情页的信息进行爬取
        tutor_data = requests.get(url=fullpath, headers=headers)  # 发起请求并获取响应数据
        tutor_data.encoding = 'utf-8'
        tutor_final_data = tutor_data.text
        # 在main中建立的文件夹下建立一个.html文件，用来存储导师详情页的源码信息
        filename = './' + tutorname + 'Libs' + '/' + 'url' + '.html'
        with open(filename, 'w', encoding="utf-8") as fp:
            fp.write(tutor_final_data)
            print(filename, '下载成功')
        return tutor_final_data


# 输入为 tutor_data: 导师详情页的信息，tutor_name: 导师姓名
def get_tutor_pic(tutor_data, tutor_name):
    # 从tutor_data中获得导师的照片的url
    soup = BeautifulSoup(tutor_data, 'lxml')
    soup1 = soup.find('div', id='right')
    soup2 = soup1.find('img')
    path = soup2.get('src')
    fullpath = "https://auto.ustc.edu.cn"+path
    # 对上方的url再次发起请求得到图片
    url = fullpath
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    img_data = response.content  # 此处需要采用二值的方式进行存储，因为此处存储的是图片
    img_path = './' + tutor_name + 'Libs' + '/portrait.jpg'
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_path, '下载成功')


# 输入tutor_data:导师详情页的源代码, tutor_name:导师姓名
# 输出一个字典类型的变量，存储的是导师的邮箱、电话、个人主页的信息
def get_tutor_info(tutor_data, tutor_name):
    soup = BeautifulSoup(tutor_data, 'lxml')
    soup1 = soup.find('div', class_="txt-01")
    info = str(soup1)
    info_peer = {}  # 建立一个字典变量，用于存储导师的邮箱、电话、个人主页的信息
    if info == None:
        print('cannot find any detailed information about' + tutor_name)
    else:
        info_list = info.split('<br/>')  # 用<br\>分割str字符串，并保存到列表
        value = []
        i = 0
        for info_key in info_list:  # 将分割好的数据存入数组
            if (i == 0):
                inter_key = info_key.split('>')
                info_key0 = inter_key[1]
                info_key0 = info_key0.strip()
                value.append(info_key0)
            else:
                value.append(info_key)  # 存入列表
            i += 1
        value.pop()
        for value_key in value:
            key_list = value_key.split(':')
            if ('mail' in key_list[0]) or ('邮' in key_list[0]):
                info_peer['email'] = key_list[1]
            elif ('tel' in key_list[0]) or ('电话' in key_list[0]):
                info_peer['phone'] = key_list[1]
            elif '主页' in key_list[0]:
                info_peer['homepage'] = key_list[1]
        info_path = './' + tutor_name + 'Libs' + '/info.txt'
        with open(info_path, 'w') as fp:
            fp.write(str(info_peer))
            print(info_path, '下载成功')
    return info_peer
