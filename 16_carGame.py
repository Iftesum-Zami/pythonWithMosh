# secret_word = input('Enter secret word: ')
#
# if secret_word.upper() == 'HELP':
#     print('start - to start the car')
#     print('stop - to stop the car')
#     print('quit - to exit')
#
#     while True:
#         command = input('Enter command: ')
#         if command.upper() == 'START':
#             print('car started')
#         elif command.upper() == 'STOP':
#             print('car stopped')
#         elif command.upper() == 'QUIT':
#             print('exit')
#             break
#         else:
#             print('invalid input')
# else:
#     print('invalid input')

command = ""
started = False
# stopped = False

while True:  # we don't have to use .lower(), because next command will return using the loop
    command = input("> ").lower()
    if command == "start":
        if started:  # started: car has already started
            print("car has already started !")
        else:
            started = True
            print("car started...")

    elif command == "stop":
        if not started:  # not started: car has already stopped
            print("car has already stopped !")
        else:
            started = False
            print("car stopped...")

    elif command == "help":
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')

    elif command == "quit":
        break
    else:
        print("Sorry, i don't understand that")
