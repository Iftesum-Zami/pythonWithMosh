weight = input("Enter weight: ")
unit = input("(L)bs or (k)g: ")

# if unit == 'L' or 'l':   # 1 pound = 0.45 kg
#     lb_to_kg = float(weight) * 0.45
#     print(f'You are {lb_to_kg} kilos')
#
# elif unit == 'K' or 'k':
#     kg_to_lb = float(weight) * 2.205  # 1 kg = 2.205 pound
#     print(f'You are {kg_to_lb} pounds')

# ----- why above code didn't work? -----

if unit.upper() == 'L':  # 1 pound = 0.45 kg
    lb_to_kg = float(weight) * 0.45
    print(f'You are {lb_to_kg} kilos')

elif unit.upper() == 'K':
    kg_to_lb = float(weight) * 2.205  # 1 kg = 2.205 pound
    print(f'You are {kg_to_lb} pounds')

else:
    print('invalid input')
