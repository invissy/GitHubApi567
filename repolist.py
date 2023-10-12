import requests
import json

def repolist(id):
    req = requests.get("https://api.github.com/users/" + id + "/repos")
    repos = req.json()
    for i in range(0,len(repos)):
        req = requests.get("https://api.github.com/repos/" + id + "/" + repos[i]['name'] + "/commits")
        commits = req.json()
        print("Repo:", repos[i]['name'], "Number of commits:", len(commits))

repolist("ColleenQue")