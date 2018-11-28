from github import Github
from github import GithubException
import matplotlib.pyplot as plt
import numpy as np
import getpass
import json



username = raw_input("Please enter your Github Username:")
pw = getpass.getpass()
g = Github(username, pw)
gitUser="NYCSwan"


def computation(g):



    userChildren = []


    for followers in g.get_user(gitUser).get_followers():
        followerChildren = []
        follower = (followers.login)
        for repo in g.get_user(follower).get_repos():
            repoChildren = []
            followerRepoName = (repo.name)
            try:
                for file in repo.get_contents(""):
                    fileName = file.name
                    fileDict = {"name": fileName,"children": []}
                    repoChildren.append(fileDict)
            except:
                pass
            repoDict= {"name": followerRepoName, "children": repoChildren}
            followerChildren.append(repoDict)

        followerDict = {"name": follower, "children": followerChildren}
        userChildren.append(followerDict)




    dataDict = { "name": gitUser, "children": userChildren}


    with open('Data.json', 'w') as outfile:
        json.dump(dataDict, outfile)





computation(g)
