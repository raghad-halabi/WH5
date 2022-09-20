sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
deleted_keys = ["name", "salary"]
for key in deleted_keys:
    del sample_dict[key]
print(sample_dict)
