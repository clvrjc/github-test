import git

repo_dir = os.path.join(rw_dir, 'github-test')
file_name = os.path.join(repo_dir, 'index.html')

r = git.Repo.init(repo_dir)
# This function just creates an empty file ...
content = open(file_name, 'wb')
content.write("<html><head></head><body><h1>TEST</h1></body></html>")
content.close()
r.index.add([file_name])
r.index.commit("initial commit")
