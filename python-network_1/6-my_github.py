"""
 Python script that takes your GitHub credentials
   (username and password) and uses the GitHub API to display your id
"""
import sys 
import requests

url = 'https://api.github.com/user'
username = sys.argv[1]
password = sys.argv[2]
parameters = {"username":"Skibo555", "password":"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")

response = requests.get(url, auth=parameters)
try:
    print(response.json()['id'])
except:
    print('None')
