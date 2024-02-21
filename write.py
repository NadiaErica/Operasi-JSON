import json

data = {
   "nama": "Nadia Erica",
   "umur": 15,
   "alamat": "lesanpuro",
   "hobi": ["mendengarkan musik"]

}

with open('data.json', 'w') as file:
        json.dump(data, file, indent=6) 