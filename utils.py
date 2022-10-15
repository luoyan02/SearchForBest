# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from ShowAWeb import tutor
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}


# input tutor's name, output the source code of tutor's detailed page
def get_tutor_url(tutorname):
    # get infomation from homepage of automation department of USTC
    url = 'https://auto.ustc.edu.cn/25976/list.htm'
    response = requests.get(url=url, headers=headers)
    response.encoding = "utf-8"
    page_text = response.text
    # analyze the data using bs4
    soup = BeautifulSoup(page_text, 'lxml')
    soup1 = soup.find('div', class_='left-mu02')
    soup2 = soup1.find('a', target='_blank', title=tutorname)
    if soup2 is None:
        print('cannot find a tutor named ' + tutorname)
        return None
    else:
        filepath = './' + tutorname + 'Libs'
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        # url:tutor's detailed page
        path = soup2.get('href')
        fullpath = 'https://auto.ustc.edu.cn' + path
        # get information from tutor's detailed page
        tutor.infopath = fullpath
        tutor_data = requests.get(url=fullpath, headers=headers)  # 发起请求并获取响应数据
        tutor_data.encoding = 'utf-8'
        tutor_final_data = tutor_data.text
        # store to local
        filename = './' + tutorname + 'Libs' + '/' + 'url' + '.html'
        with open(filename, 'w', encoding="utf-8") as fp:
            fp.write(tutor_final_data)
            print(filename, '下载成功')
        return tutor_final_data


# input source code of tutor's detailed page and tutor's name
# output tutor's picture
def get_tutor_pic(tutor_data, tutor_name):
    # get the url of tutor's picture
    soup = BeautifulSoup(tutor_data, 'lxml')
    soup1 = soup.find('div', id='right')
    soup2 = soup1.find('img')
    path = soup2.get('src')
    fullpath = "https://auto.ustc.edu.cn"+path
    url = fullpath
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    img_data = response.content  # 此处需要采用二值的方式进行存储，因为此处存储的是图片
    img_path = './' + tutor_name + 'Libs' + '/portrait.jpg'
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_path, '下载成功')
    return fullpath


# input source code of tutor's detailed page and tutor's name
# output tutor's email\homepage\phone number  saved in a dictionary
def get_tutor_info(tutor_data, tutor_name):
    soup = BeautifulSoup(tutor_data, 'lxml')
    soup1 = soup.find('div', class_="txt-01")
    info = str(soup1)
    info_peer = {}
    if info == None:
        print('cannot find any detailed information about' + tutor_name)
    else:
        info_list = info.split('<br/>')  # use <br\> to split the string
        value = []
        i = 0
        for info_key in info_list:
            if (i == 0):
                inter_key = info_key.split('>')
                info_key0 = inter_key[1]
                info_key0 = info_key0.strip()
                value.append(info_key0)
            else:
                value.append(info_key)
            i += 1
        value.pop()
        info_peer['email'], info_peer['phone'], info_peer['homepage'], info_peer['homepage_link'] = '', '', '', ''
        for value_key in value:
            key_list = value_key.split(':')
            if len(key_list) == 1:
                key_list = value_key.split('：')
            if ('mail' in key_list[0]) or ('邮' in key_list[0]):
                info_peer['email'] = key_list[1]
            elif ('tel' in key_list[0]) or ('电话' in key_list[0]):
                info_peer['phone'] = key_list[1]
            elif '主页' in key_list[0]:
                info_peer['homepage'] = key_list[1]
        info_path = './' + tutor_name + 'Libs' + '/info.txt'
        with open(info_path, 'w') as fp:
            fp.write(str(info_peer))
            print(info_path, 'download successfully')
    return info_peer
