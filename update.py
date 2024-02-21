import json

with open("data.json", "r") as file:
    data = json.load(file)

    data['umur'] = 15
    data['email'] = 'admin@admin.com'

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=3)