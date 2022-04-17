#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: __init__.py
# Project: user <<projectversion>>
# Author: Alberto Urbaez (info@albertourbaez.com)
# File Created: 2022-04-17 15:17:14
# -----
# Modified By: Alberto Urbaez (info@albertourbaez.com)
# Last Modified: 2022-04-17 15:20:20
# -----
# Copyright 2021 - 2022,  CA-TECH
###

from flask import Blueprint

user = Blueprint("user", __name__, url_prefix="/user")

from . import views