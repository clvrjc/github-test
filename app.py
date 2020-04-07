#Libraries to be import START
import random
from flask import Flask, request, g, session, render_template, redirect, url_for, flash
import os
import json
import time, string, random, re
from github import Github
from hashlib import sha1

GITHUB_USER = os.environ['GITHUB_USER']
GITHUB_PASSWORD = os.environ['GITHUB_PASSWORD']
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']

sample = 'sample'
print(sample)
m = sha1(sample.encode('utf-8'))
print(m.hexdigest())
#---------------------------------------------------------------------------------------------
#Using username and password to connect
#g = Github(GITHUB_USER, GITHUB_PASSWORD)
	
#or using an access token
g = Github(GITHUB_TOKEN)
	
#if it is Github enterprise with costum hostname
#g = Github(base_url="https://je-becerro.herokuapp.com//api/v3", login_or_token=GITHUB_TOKEN)
#-----------------------------------------------------------------------------------------------

repo = g.get_repo("clvrjc/github-test")
contents = repo.get_contents("requirements.txt")
print(contents)

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	
	return "ok"

@app.route('/create', methods=['GET','POST'])
def create():
	repo.create_file("sample.html", "html', branch="master")#master is a default branch
	
	return "file created"

@app.route('/update', methods=['GET','POST'])
def update():
	contents = repo.get_contents("sample.html", ref="master")
	repo.update_file(contents.path, "update sample.html", "content", contents.sha, branch="master")
	return "updated"

@app.route('/delete', methods=['GET','POST'])
def delete():
	contents = repo.get_contents("sample.html", ref="master")
	repo.delete_file(contents.path, "remove sample.html", contents.sha, branch="master")
	return "deleted"

if __name__ == "__main__":
	app.run()
 

