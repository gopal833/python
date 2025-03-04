dict = {
    "production": "dev",
    "development": "prod",
    "testing": "dev"
}

new_dict = {}
for key, value in dict.items():
    if value not in new_dict:
        new_dict[value] = [key]
    else:
        new_dict[value].append(key)
print(new_dict) 