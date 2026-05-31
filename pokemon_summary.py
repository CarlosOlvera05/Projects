import requests
import json
#Save Only Important Data
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
data = response.json()

important_data = []
for item in data.get("abilities", []):
    
    ability_info = item.get("ability", {})
    abilities = {
        "ability_name": ability_info.get("name"),
    }
    important_data.append(abilities)
    important_data.append({"pokemon_name": data["name"]})
    important_data.append({"pokemon_height": data["height"]})
    important_data.append({"pokemon_weight": data["weight"]})
    
print(important_data)
with open("pokemon_summary.json", "w") as file:
    json.dump(important_data, file, indent=4)