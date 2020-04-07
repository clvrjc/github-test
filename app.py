#Libraries to be import START
import random
from flask import Flask, request, g, session, render_template, redirect, url_for, flash
import os
import json
import time, string, random, re
from github import Github

GITHUB_USER = os.environ['GITHUB_USER']
GITHUB_PASSWORD = os.environ['GITHUB_PASSWORD']
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']

#Using username and password to connect
#g = Github(GITHUB_USER, GITHUB_PASSWORD)
	
#or using an access token
g = Github(GITHUB_TOKEN)
	
#if it is Github enterprise with costum hostname
#g = Github(base_url="https://je-becerro.herokuapp.com//api/v3", login_or_token=GITHUB_TOKEN)

#Create a new file in the repository
repo = g.get_repo("clvrjc/github-test")
repo.create_file("test.txt", "comment", "content inside", branch="master")#master is a default branch
{'content': ContentFile(path="test.txt"), 'commit': Commit(sha="")}	

'''
#Update a file in the repository
repo = g.get_repo("clvrjc/github-test")
contents = repo.get_contents("test.txt", ref="master")
repo.update_file(contents.path, "another comment", "gwap ko insde and out", contents.sha, branch="master")
{'commit': Commit(sha=""), 'content': ContentFile(path="test.txt")}
'''

for repo in g.get_user().get_repos():
	#print(repo.name)
	repo.edit(has_wiki=False)
	# to see all the available attribbutes and methods
	#print(dir(repo))
	
	

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	#Update a file in the repository
	repo = g.get_repo("clvrjc/github-test")
	contents = repo.get_contents("test.txt", ref="master")
	repo.update_file(contents.path, "another comment", "gwap ko insde and out", contents.sha, branch="master")
	{'commit': Commit(sha=GITHUB-TOKEN), 'content': ContentFile(path="test.txt")}
	return "ok"

if __name__ == "__main__":
	app.run()
 

