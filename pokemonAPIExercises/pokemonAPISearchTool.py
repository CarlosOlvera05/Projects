import requests
import json
#Mini Search Tool for Pokémon API
#

pokemon_name = input("Enter the name of the Pokémon you want to search for: ").lower()
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
data = response.json()
print(f"Name: {data['name']}")
print(f"Height: {data['height']}")
print(f"Weight: {data['weight']}")
    
    