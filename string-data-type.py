# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    string-data-type.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jpinedo- <jpinedo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/02 10:04:19 by jpinedo-          #+#    #+#              #
#    Updated: 2025/04/02 10:08:09 by jpinedo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

myString = "this is a string."
print(myString)
print(type(myString))
print(myString + "is of the data type" + str(type(myString)))
print("---")

firstString = "Water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
print("---")

name = input("What is your name? ")
print("your name is: " + name)
print("---")

color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))
print("---")
