import requests
import json

response = requests.get("https://api.github.com/users/carlosolvera05")
data = response.json()

followers =  data["followers"]
following = data["following"]

follow_ratio = followers/following if following != 0 else "N/A"

print(f"follow_ratio: {follow_ratio}")

