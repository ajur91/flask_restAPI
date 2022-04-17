#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: __init__.py
# Project: app <<projectversion>>
# Author: Alberto Urbaez (info@albertourbaez.com)
# File Created: 2022-04-16 17:01:11
# -----
# Modified By: Alberto Urbaez (info@albertourbaez.com)
# Last Modified: 2022-04-17 17:15:15
# -----
# Copyright 2021 - 2022,  CA-TECH
###
from flask import Flask
from .config import Config
from .user import user


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(user)
    
    app.secret_key = 'myawesomesecretkey'
    app.config['MONGO_URI'] = 'mongodb://localhost/pythonmongodb'
    
    return app