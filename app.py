from github import Github
import os
GITHUB_USER = os.environ['GITHUB_USER']
GITHUB_PASSWORD = os.environ['GITHUB_PASSWORD']
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']



#Libraries to be import START
import random
from flask import Flask, request, g, session, render_template, redirect, url_for, flash
import os
import json
import time, string, random, re

#import Mongo#import Mongo.py
#from NLU import nlp
#from collections import Counter #install collections

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    # using username and password
    g = Github(GITHUB_USER, GITHUB_PASSWORD)

    # or using an access token
    g = Github(GITHUB_TOKEN)

    # Github Enterprise with custom hostname
    g = Github(base_url="https://je-becerro.herokuapp.com//api/v3", login_or_token=GITHUB_TOKEN)

    for repo in g.get_user().get_repos():
        print(repo.name)
        repo.edit(has_wiki=False)
        # to see all the available attributes and methods
        print(dir(repo))
	return 'ok'	
if __name__ == "__main__":
	app.run()
 

