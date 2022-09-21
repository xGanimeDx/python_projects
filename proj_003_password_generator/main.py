import string
import secrets

length = input('Please enter the length of the passowrd: ')

while not length.isdigit():
    length = input('Please use an integer value as a length: ')

def generate_sequence(length):
    special = '!@#$%^&*()'
    total = string.ascii_letters + string.digits +  special
    password = ''.join(secrets.choice(total) for i in range(length))
    return password

print(generate_sequence(int(length)))
