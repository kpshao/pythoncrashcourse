filename = 'guest.txt'

with open(filename, 'w') as file_object:
    guest = input('Enter you name:')
    file_object.write(guest)