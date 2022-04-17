#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: views.py
# Project: user <<projectversion>>
# Author: Alberto Urbaez (info@albertourbaez.com)
# File Created: 2022-04-17 15:19:05
# -----
# Modified By: Alberto Urbaez (info@albertourbaez.com)
# Last Modified: 2022-04-17 18:19:38
# -----
# Copyright 2021 - 2022,  CA-TECH
###

from flask import make_response, redirect, render_template, request
from src.app import create_app

app = create_app()

@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    response.set_cookie("user_ip", user_ip)
    return response


@app.route("/hello")
def hello():
    user_ip = request.cookies.get("user_ip")
    # return f'Hello World Platzi, tu IP este {user_ip}'
    return render_template("hello.html",user_ip=user_ip)





