print('Guess a number between 1 to 10, you have 3 chances')

# i = 0
# while i < 3:
#     guess = int(input('Guess: '))
#     if guess == 9:
#         print('You won!')
#         break
#     i = i + 1
#     if i == 3:
#         print('Sorry, you failed!')

# ----- above code also works -----

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count = guess_count + 1
    if guess == secret_number:
        print('You won!')
        break
else:  # this else part is for 'while loop' not for 'if'
    print('Sorry, you failed!')
