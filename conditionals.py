# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    conditionals.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jpinedo- <jpinedo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/02 12:19:33 by jpinedo-          #+#    #+#              #
#    Updated: 2025/04/02 12:19:36 by jpinedo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

userReply = input("Do you need to ship a package? (Enter yes o no) ")
if userReply == "yes":
    print("we can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("how many copies would you like? (Enter a number) ")
    print  ("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
