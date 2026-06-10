import requests
import json

class GitHubAPI:
    def __init__(self, username):
        self.username = username
        self.base_url = "https://api.github.com"
    
    def get_user_data(self):
        response = requests.get(f"{self.base_url}/users/{self.username}")
        data = response.json()
        with open("github_user_data.json", "w") as file:
            json.dump(data, file, indent=4)
        return response.json()
    
    def get_repositories(self):
        response = requests.get(f"{self.base_url}/users/{self.username}/repos")
        data = response.json()
        with open("github_user_.json", "w") as file:
            json.dump(data, file, indent=4)
        return response.json()