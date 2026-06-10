import requests
import json
reponse = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
data = reponse.json()
print(data)

extract_list = []
extract_list.append(data["name"])
extract_list.append(data["height"])
extract_list.append(data["weight"])
extract_list.append(data["base_experience"])


with open("pokemon1.json", "w") as file:
    json.dump(extract_list, file, indent=4)