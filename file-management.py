import json

example = '{ "nama":"Buchori", "umur":22, "Kota":"New York"}'
#parse example
result = json.loads(example)
print(example)

import pickle
exDictionary = {1:"5", 2:"4", 3:"hello"}
picOut = open("")