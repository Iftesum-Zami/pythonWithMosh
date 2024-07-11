def greet_user(first_name, last_name):  # "name" is the 'parameter', can use many parameter as we need
    print(f"Hi {first_name} {last_name}!")
    print("Welcome abroad !")


print("Start")
greet_user("Iftesum", "Zami")  # "Zami", "Iftesum" is 'argument', which is the actual value
greet_user("Shahriar", "Salman")  # bonus: it will give an error if we pass 1 argument
print("Finish")
