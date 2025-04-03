# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    collections.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jpinedo- <jpinedo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/02 10:10:30 by jpinedo-          #+#    #+#              #
#    Updated: 2025/04/02 10:29:30 by jpinedo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

myFruitList = ["apple","banana","cherry"]
print(myFruitList)
print(type(myFruitList))
print("---")

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
print("---")

myFruitList[2] = "orange"
print("change cherry for orange on list ")
print(myFruitList)
print("---")

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print("a tuple can't be changed") 
print("---")

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
print("---")

myFavoriteFruitDictionary = {
	
	"Akua" : "apple",
	"Saanvi" : "banana",
	"Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print("---")

print("printing The favorite fruit of Akua, Saanvi and Paulo")
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
print("---")



