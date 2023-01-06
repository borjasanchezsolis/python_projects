command = ''
started = False
while command != 'quit':
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('its already started')
        else:
            started = True
            print('the car started')
    elif command == 'stop':
        if not started:
            print('its already stopped')
        else:
            started = False
            print('the car stopped')
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit the game
        """)
    elif command == 'quit':
        break
    else:
        print('I dont understand')



