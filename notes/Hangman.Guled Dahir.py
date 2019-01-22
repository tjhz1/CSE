import random
import string
wordbank = ["pencil", "computers", "hair", "poster", "clock", "agriculture", "work", "shirts", "pants", "catch"]

word = random.choice(wordbank)
print(word)

letter = list(string.ascii_letters)
letters_used = []
guesses = 8
word_letters = list(word)

guess = input("Guess a letter")
print("%s?? Really???" % word_letters)