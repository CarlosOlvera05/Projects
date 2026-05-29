import json

import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
data = response.json()
print(data)

filtered_list = []
print("Abilities:")
## access specific data in a loop
for item in data.get("abilities", []):
    # Dig into the nested 'ability' dictionary to grab the name
    ability_info = item.get("ability", {})
    
    abilities = {
        "ability_name": ability_info.get("name"),
        "pokemon_name": data.get("name"),
        "height": data.get("height"),
        "weight": data.get("weight")
    }
    filtered_list.append(abilities) 


#make prettier
with open("pokemon.json", "w") as file:
    json.dump(filtered_list, file, indent=4)