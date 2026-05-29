from fastapi import FastAPI
import requests

response = requests.get("https://catfact.ninja/fact")

apiData = response.json()
print(response.json())

#save as a json file
with open("catfact.json", "w") as file:
    file.write(str(apiData))