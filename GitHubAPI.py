from github import Github
from github import GithubException
import matplotlib.pyplot as plt
import numpy as np

import getpass


username = raw_input("Github Username:")
pw = getpass.getpass()
g = Github(username, pw)

gitUser=raw_input("Please enter username of Github user you would like to see data on:")
# g1 = g.get_user(gitUser)


quantity=[]
label=['HTML','JavaScript','Java','C++','C','Python','C#','Other']
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
other=0

for repo in g.get_user(gitUser).get_repos():

    if repo.language == "HTML":
        count1+=1
    elif repo.language == "JavaScript":
        count2+=1
    elif repo.language == "Java":
        count3+=1
    elif repo.language == "C++":
        count4+=1
    elif repo.language == "C":
        count5+=1
    elif repo.language == "Python":
        count6+=1
    elif repo.language == "C#":
        count7+=1
    else:
        other+=1


quantity=[count1,count2,count3,count4,count5,count6,count7,other]



index = np.arange(len(label))
plt.bar(index, quantity)
plt.xlabel('Language', fontsize=10)
plt.ylabel('No of Repos', fontsize=10)
plt.xticks(index, label, fontsize=10, rotation=30)
plt.title('Interrogation of GitHub API')
plt.show()
