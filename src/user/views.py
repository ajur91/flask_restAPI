#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: views.py
# Project: user <<projectversion>>
# Author: Alberto Urbaez (info@albertourbaez.com)
# File Created: 2022-04-17 15:19:05
# -----
# Modified By: Alberto Urbaez (info@albertourbaez.com)
# Last Modified: 2022-04-17 18:15:16
# -----
# Copyright 2021 - 2022,  CA-TECH
###
from .. import log
from . import user
from flask import jsonify, request, Response
from bson import json_util
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
import pymongo

try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017
    )
    mongo.server_info()
    db = mongo.pythonmongodb
    log.green("cannot connet to DB")
except:
    log.red("ERROR -  cannot connet to DB")

@user.route('', methods=['POST'])
def create_user():
    # Receiving Data
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if username and email and password:
        hashed_password = generate_password_hash(password)
        id = db.users.insert(
            {'username': username, 'email': email, 'password': hashed_password})
        response = jsonify({
            '_id': str(id),
            'username': username,
            'password': password,
            'email': email
        })
        response.status_code = 201
        return response
    else:
        return not_found()

@user.route('', methods=['GET'])
def get_users():
    users = db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype="application/json")


@user.route('/<id>', methods=['GET'])
def get_user(id):
    print(id)
    user = db.users.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")


@user.route('/<id>', methods=['DELETE'])
def delete_user(id):
    db.users.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response


@user.route('/<_id>', methods=['PUT'])
def update_user(_id):
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    if username and email and password and _id:
        hashed_password = generate_password_hash(password)
        db.users.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'username': username, 'email': email, 'password': hashed_password}})
        response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
        return not_found()

@user.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response