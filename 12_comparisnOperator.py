name = input('Input your name having 3 to 10 letters: ')

if len(name) < 3:
    print('name must be at least 3 letters')
elif len(name) > 10:
    print('name must be a maximum of 10 letters')
else:
    print('name looks good')
