import random
word_bank = ["pencil", "computers", "hair", "poster", "clock", "agriculture", "work", "shirts", "pants", "catch"]

word = random.choice(word_bank)
print(word)
letters_used = []
guesses = 8
word_letters = list(word)
guess = input("Guess a letter")
while guesses > 0:

    output = []
    for letter in word:
        if letter in letters_used:
            output.append(letter)
        else:
            output.append("*")
    print(output)

    letter_used = input("guess a letter: ")
    letters_used.append(letter_used)

    guesses -= 1
