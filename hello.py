# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 15:13:59 2021

@author: ViniciusFraga
"""
import os 

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index!"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return "name/<string:name>"

if __name__ == "__main__":
    app.run()
    
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)