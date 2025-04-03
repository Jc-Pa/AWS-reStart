# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    while-loop.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jpinedo- <jpinedo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/02 12:50:26 by jpinedo-          #+#    #+#              #
#    Updated: 2025/04/02 12:51:08 by jpinedo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random
number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. that is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format((guess)))
print("Thank you for playing!")