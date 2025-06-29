#Python script to fetch open pull requests from a Github Repository
#Print User id and Counts 

import requests

#Get URl of Github Respository
#Replace the url with the required one
url = "https://api.github.com/repos/kothaajay/Devops-Python-Scripts/pulls"

response = requests.get(url)
#Check if response is successful
if response.status_code == 200:
   pr = {}
   for user in response.json():
       user_name = user['user']['login']
       if user_name in pr:
           pr[user_name] += 1
       else:
           pr[user_name] = 1
   #Print User id and Counts
   for user, count in pr.items():
       print(f"User: {user}, Pull Requests: {count}")
else:
    print("Failed to fetch pull requests. Status code:", response.status_code)                           
