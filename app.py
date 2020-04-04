from github import Github
import os
GITHUB_USER = os.environ['GITHUB_USER']
GITHUB_PASSWORD = os.environ['GITHUB_PASSWORD']
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']

# using username and password
g = Github(GITHUB_USER, GITHUB_PASSWORD)

# or using an access token
g = Github(GITHUB_TOKEN)

# Github Enterprise with custom hostname
g = Github(base_url="https://clvrjc/api/v3", login_or_token=GITHUB_TOKEN)

for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))
