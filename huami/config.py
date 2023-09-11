import os
from dotenv import load_dotenv

from flask import Flask, render_template, request, redirect, url_for, flash

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'VALLABLABLAINSCHALLA'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://huami:SICHERESPASSWORT@127.0.0.1:3306/huami'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ITEMS_PER_PAGE = 5

