# Guess The Number v1.0.0

import random
Number = random.randint(1, 5)
while True:
    numberInput = int(input("Please, guess the number: "))
    if Number == numberInput:
        print('Congrats, your guessed is right....')
        break
    else:
        print('Try again, please')
        continue
