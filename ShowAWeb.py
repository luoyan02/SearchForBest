#!-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template


class Tutor:
    def __init__(self, name, email, homepage, phone):
        self.name = name
        self.email = email
        self.homepage = homepage
        self.phone = phone


tutor = Tutor(None, None, None, None)
SearchForBest = Flask(__name__)


@SearchForBest.route('/')
@SearchForBest.route('/visualize')
def tutor_info():
    content = {
        'tutor': tutor
    }
    return render_template("visualize.html", **content)


