# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    categorize-values.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jpinedo- <jpinedo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/02 11:26:32 by jpinedo-          #+#    #+#              #
#    Updated: 2025/04/02 11:26:36 by jpinedo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

myMixtedTypeList = [45, 290578, 1.02, True, "My dog is oon the bed.", "45"]
for item in myMixtedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
