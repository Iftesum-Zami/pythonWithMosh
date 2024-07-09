customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

# print(customer["birthdate"])
# this will give an error because "birthdate" doesn't exist in dictionary

print(customer["name"])
print(customer.get("name"))  # basically the same thing but .get() gives None instead of error
print(customer.get("birthdate", "01 January, 2000"))  # 2nd parameter is the default value if 1st doesn't exist

customer["name"] = "Jack Smith"  # updating
customer["birthdate"] = "01 January, 2000"  # add new key in the dictionary

