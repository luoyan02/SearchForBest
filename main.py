# -*- coding:utf-8 -*-
from utils import *

from ShowAWeb import SearchForBest
from ShowAWeb import tutor


if __name__ == '__main__':
    tutor_name = input("enter a tutor's name:")
    tutor_data = get_tutor_url(tutor_name)
    while tutor_data is None:
        print('please input the correct name!')
        tutor_name = input("enter a tutor's name:")
        tutor_data = get_tutor_url(tutor_name)
    pic_path = get_tutor_pic(tutor_data, tutor_name)
    info_peer = get_tutor_info(tutor_data, tutor_name)
    tutor.name = tutor_name
    tutor.email = info_peer['email']
    tutor.homepage = info_peer['homepage']
    tutor.phone = info_peer['phone']
    tutor.picpath = pic_path
    SearchForBest.run()

