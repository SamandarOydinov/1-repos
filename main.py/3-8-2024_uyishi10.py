import os
import json
os.system("cls")

dct = {

    11: 2,
    25: 12,
    32: 11,
    14: 20,
    51: 15,
    16: 14,
    37: 16,
    68: 19,
    29: 9,
    10: 17

}
value = list(dct.values())
key = []
for i in range(len(value)):
    key.append(0)
dct.clear()
for i in range(len(value)):
    dct[key[i]] = value[i]

print(json.dumps(dct, indent=2))