import requests
import json

response = requests.get("https://api.github.com/users/carlosolvera05")

response = requests.get("https://api.github.com/users/carlosolvera05/repos")

data = response.json()

i = 0
counter = 0
while i < len(data):
    repo = data[i]
    counter += 1
    print(f"Repository {counter}: {repo['name']}")
    i += 1

max = 0
j = 0
while j < len(data):
    repo = data[j]
    if repo.get("stargazers_count", 0) > max:
        max = repo["stargazers_count"]
        most_starred_repo = repo["name"]
    j += 1
    

print(f"Most starred repository: {most_starred_repo} with {max} stars")
# print(json.dumps(data[0], indent=4))
# amount_of_stared_repos = data.get("starred_url", [])
# print(f"Amount of starred repositories: {len(amount_of_stared_repos)}")
# Debugging Trick

# Whenever you're unsure about the structure of the data you're working with, you can print it out in a readable format. This helps you understand how to access the information you need.
# # print(type(data))
# print(json.dumps(data, indent=4))
# print(data[0])