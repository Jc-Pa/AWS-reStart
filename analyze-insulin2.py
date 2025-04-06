# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    analyze-insulin2.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jpinedo- <jpinedo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/06 21:42:53 by jpinedo-          #+#    #+#              #
#    Updated: 2025/04/06 23:40:53 by jpinedo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
	(!!!) Nota del autor: Este codigo intenta optimizar el trabajo de
	analyze-insulin.py para aquellos que tienen un poco de experiencia
	y quieren aprender a usar python
	No habra comentarios explicativos a menos que sea necesario
'''
# **************************************************************************** #
# Captura del archivo Input / Verificando que exite / sino detiene el programa
import os
# Captura los datos del archivo solo manteniendo las minusculas
import re
'''
	Importa la libreria os
	Para verificar si el archivo existe
	https://www.w3schools.com/python/module_os.asp
	-----------------
	Importa la libreria re
	Para usar expresiones regulares
	https://www.w3schools.com/python/python_regex.asp
'''
fileIn = input("Ingrese el nombre del archivo: ")
if os.path.exists(fileIn):
	#abrir archivo
	fileIn = open(fileIn, "r")
# Sino exite terminar el programa
else:
	print("El archivo no existe")
	exit(1)
# **************************************************************************** #
rFile = fileIn.readlines() # Lee las lineas archivo
seq = ""
# Gettin the sequence to a unique file clean preproinsulin-seq-clean.txt
i = 0
while i < len(rFile):
	seq = seq + "".join(c for c in re.split(r'[^a-z]', rFile[i]) if c.isalpha)
	i += 1
# Guardando el resultado en un nuevo archivo
with open("preproinsulin-seq-clean.txt", "w") as output:
	output.write(seq)
fileIn.close()
# **************************************************************************** #
# Captura de las diferencias entre los aminoacidos con el nuevo archivo
fileIn = open("preproinsulin-seq-clean.txt", "r")
rFile = fileIn.read() # Lee los caracteres del archivo
seq = ""
i = 0
while i < 110:
	seq = seq + rFile[i]
	if i == 23:
		with open("Isinsulin-seq-clean.txt", "w") as output:
			output.write(seq)
		seq = ""
	elif i == 53:
		with open("binsulin-seq-clean.txt", "w") as output:
			output.write(seq)
		seq = ""
	elif i == 88:
		with open("cinsulin-seq-clean.txt", "w") as output:
			output.write(seq)
		seq = ""
	elif i == 109:
		with open("ainsulin-seq-clean.txt", "w") as output:
			output.write(seq)
	i += 1
fileIn.close()
# **************************************************************************** #
'''
	Se abrio el archivo preproinsulin-seq-clean.txt
	lectura por caracteres
	usando el loop while para recorrer los caracteres
	creando los condicionales para crear los archivos correspondientes 
	guardando el resultado en los archivos nuevos
	---------------
	Todavia se puede agregar cambios EJM añadir el nombre o un identificador
	para cada archivo nuevo creado, dependiendo de las necesidades del usuario
	en base al archivo de entrada 
	EJM nombrePaciente_preproinsulin-seq.txt // nombrePaciente_Isinsulin-seq-clean.txt
	de esta forma llamar a este archivo como funcion para llamar a un mayor numero
	de archivos y automatizar la salida**
'''