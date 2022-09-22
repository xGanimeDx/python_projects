import string
import secrets

usr_input = input('Please enter the length of the passowrd: ')

while not usr_input.isdigit():
    usr_input = input('Please use an integer value as a length: ')

def generate_sequence(length: int) -> str:
    special = '!@#$%^&*()'
    total = string.ascii_letters + string.digits +  special
    password = ''.join(secrets.choice(total) for i in range(length))
    return password

print(generate_sequence(int(usr_input)))
