import random

options = ['rock', 'paper', 'scissors']
play = True

while play:
    user = input('Choose your figure (rock, paper, scissors): ')
    computer = random.choice(options)

    while user not in options:
        user = input('Please select right figure (rock, paper, scissors): ')

    print(f'User choice: {user}')
    print(f'Computer choice: {computer}')

    if user == computer:
        print('DRAW! No one win.')
    elif user == 'rock' and computer == 'scissors':
        print('WIN! You win.')
    elif user == 'paper' and computer == 'rock':
        print('WIN! You win.')
    elif user == 'scissors' and computer == 'paper':
        print('WIN! You win.')
    else:
        print('LOSE! Computer wins.')

    replay = input('Do you want to play again? Y or N ').upper()
    while replay not in ['Y', 'N']:
        replay = input('Please enter Y or N ')

    if replay == 'N':
        play = False
