import requests
import json

#List All Pokémon Abilities
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
data = response.json()

available_abilities = []
for item in data.get("abilities", []):
    
    ability_info = item.get("ability", {})
    abilities = {
        "ability_name": ability_info.get("name"),
    }
    available_abilities.append(abilities)

print(available_abilities)
with open("pokemon_abilities.json", "w") as file:
    json.dump(available_abilities, file, indent=4)