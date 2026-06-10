import requests
import json

#Basic API call
response = requests.get("https://akabab.github.io/superhero-api/api/all.json")
data = response.json()

# print(type(data), type(data[0]))


with open("heroes.json", "w") as file:
    json.dump(data, file, indent=4)
    
#The structure is a list, each element is a dictionary

# data
# │
# ├── data[0] -> A-Bomb dictionary
# ├── data[1] -> Another hero dictionary
# ├── data[2] -> Another hero dictionary
# ...
# ├── Batman dictionary somewhere

# print(json.dumps(data, indent=4))


# data
# │
# ├── hero
# │      │
# │      ├── "name"
# │      ├── "powerstats"
# │      │         │
# │      │         ├── "intelligence"
# │      │         └── "strength"
# │      │
# │      ├── "biography"
# │      │         │
# │      │         ├── "fullName"
# │      │         └── "aliases"
# │      │
# │      └── "images"
# │                │
# │                ├── "xs"
# │                ├── "sm"
# │                └── "lg"

#Access nested data
#Directly access the name of the 60th hero in the list (Batman)
results = data[51]["name"]
print(results)

#Search the entire list with for loop
# for hero in data:
#     print(hero["name"], hero["id"])
    
# batman = None

#Search for specific data
for hero in data:
    if hero["name"] == "Batman":
        print(hero)
        #saving the entire dictionary to a variable
        batman = hero
        break

#Access nested data
# Bc elements are dictionaries
print(batman["id"])

print(batman["powerstats"]["intelligence"])

print(batman["biography"]["fullName"])

print(batman["appearance"]["height"])

print(batman["images"]["lg"])

for villian in data:
    if villian["name"] == "Joker":
        print(villian["biography"]["fullName"])
        print(villian["powerstats"]["intelligence"])
        print(villian["biography"]["alignment"])
        print(villian["images"]["lg"])
        break