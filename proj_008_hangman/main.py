import string

usr_input_word = input("Enter a word: ").upper()

def hangman(word: str) -> None:
    alphabet = set(string.ascii_uppercase)
    word_letters = set(word)
    used_letters = set()
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives and you have used these letters", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in word")
        elif user_letter in used_letters:
            print("You already used it before")
        else:
            print("Invalid letter")

    if lives == 0:
        print("You lose. The word was", word)
    else:
        print("You guessed the word", word, "!")

hangman(usr_input_word)
