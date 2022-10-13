# -*- coding:utf-8 -*-
from utils import *
from search_in_cnki import *
from ShowAWeb import SearchForBest
from ShowAWeb import tutor

import os


if __name__ == '__main__':
    tutor_name = input("enter a tutor's name")
    # 为用户想要查找的导师建立一个文件夹
    filepath = './'+tutor_name+'Libs'
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    # 从主页获取导师详情页的源码信息，以html格式存储
    tutor_data = get_tutor_url(tutor_name)
    # 获取详情页上导师照片信息
    get_tutor_pic(tutor_data, tutor_name)
    # 获取详情页上导师邮箱、联系方式、个人主页等基本信息
    info_peer = get_tutor_info(tutor_data, tutor_name)
    # 在cnki上搜索导师论文数据的信息
    search_in_cnki(tutor_name)
    tutor.name = tutor_name
    tutor.email = info_peer['email']
    tutor.homepage = info_peer['homepage']
    tutor.phone = info_peer['phone']
    SearchForBest.run()
