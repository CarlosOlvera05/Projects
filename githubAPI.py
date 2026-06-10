import requests
import json

response = requests.get("https://api.github.com/users/CarlosOlvera05")
data = response.json()

carlos_data = []
carlos_data.append({"login": data["login"]})
carlos_data.append({"name": data["name"]})
carlos_data.append({"public_repos": data["public_repos"]})
carlos_data.append({"followers": data["followers"]})
carlos_data.append({"following": data["following"]})

print(f"Login: {data['login']}")
print(f"Name: {data['name']}")
print(f"Public Repositories: {data['public_repos']}")
print(f"Followers: {data['followers']}")
print(f"Following: {data['following']}")

with open("github_user_data.json", "w") as file:
    json.dump(carlos_data, file, indent=4)