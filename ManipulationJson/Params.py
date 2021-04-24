import json

dictionary = {
  "GOKU" : ["Son Goku", "Sayijin", "Dragon Ball"],
  "ICHIGO" : ["Ichigo Kurosaki", "Hollow, Quincy, Humano, FullBringer", "Dragon Ball"],
  "Naruto" : ["Naruto Uzumaki", "Humano(Ninja)", "Naruto"]
}

with open("db1.json", "w") as json_file:
    json.dump(dictionary, json_file)