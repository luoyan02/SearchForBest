#!-*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
from search_in_cnki import *


class Tutor:
    def __init__(self, name, email, homepage, phone, picpath, infopath):
        self.name = name
        self.email = email
        self.homepage = homepage
        self.phone = phone
        self.picpath = picpath
        self.infopath = infopath


tutor = Tutor(None, None, None, None, None, None)
SearchForBest = Flask(__name__)


@SearchForBest.route('/', methods=['GET', 'POST'])
@SearchForBest.route('/visualize', methods=['GET', 'POST'])
def tutor_info():
    if request.method == 'POST':
        search_in_cnki(tutor.name)
    content = {
        'tutor': tutor
    }
    return render_template("visualize.html", **content)


