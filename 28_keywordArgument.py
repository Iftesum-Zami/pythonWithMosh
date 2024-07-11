def greet_user(first_name, last_name):  # "name" is the 'parameter', can use many parameter as we need
    print(f"Hi {first_name} {last_name}!")
    print("Welcome abroad !")


print("Start")
greet_user("Iftesum", "Zami")  # the arguments will be assigned correspondingly with parameters
greet_user(last_name="Salman", first_name="Shahriar")  # if we give argument a keyword, then sequence doesn't matter
# Bonus: keyword Argument will be better to use if we are using multiple numerical values

print("Finish")
