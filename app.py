'''
open("./index.html", "x")
with open("index.html", "w") as file:
    f.write("<html><head></head><body><h1>TEST</h1></body></html>")
    f.close()
    
print("good")
'''
from git import Repo

repo_dir = 'github-test'
repo = Repo(repo_dir)
file_list = [
    'C:\Users\User\Downloads\templates\Blog\static\images\jear.jpg'
]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()
