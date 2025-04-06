# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    analyze-insulin.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jpinedo- <jpinedo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/03 11:20:31 by jpinedo-          #+#    #+#              #
#    Updated: 2025/04/06 23:43:02 by jpinedo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
(!!!) Nota del autor: el codigo no esta optimizado
	es una secuencia para aprender a usar python
	desarrollando el Lab de AWS:
	"Preparación para el análisis de insulina con Python" como punto de partida
	Se trata de usar las funciones más basicas sin importar librerias
	Para no complicar el entendimiento del código

AWS Lab 10 - Analisis de insulina con python
	Luego de copiar el codigo de la insulina en el archivo preproinsulin-seq.txt
	Se procede a limpiar el texto para obtener la secuencia de aminoacidos
	Se eliminan los caracteres no deseados y se guarda en un nuevo archivo 
	prepoinsulin-seq-clean.txt
'''
# **************************************************************************** #
#Limpieza de texto
#(!!!)Verifica de que el archivo preproinsulin-seq.txt este en la misma carpeta
# Abre el archivo
fileIn = open("preproinsulin-seq.txt", "r")
'''
	fileIn -> archivo de entrada (variable a usar) 
	open -> comando para abrir el archivo
		open ("nombre_archivo", "modo") 
	modo -> puede ser "r" para leer, "w" para escribir, "a" para agregar 
'''
lines = fileIn.readlines() # Lee la primera linea
seq = "" # Inicializa la secuencia (variable a usar)
i = 0 # Inicializa el contador
while i < len(lines):
		# Lee el archivo len(tamaño) len(lines) tamaño de la lista 
	lines[i] = lines[i].replace(" ", "") # Elimina los espacios
	lines[i] = lines[i].replace("\n", "") # Elimina saltos de linea
	lines[i] = lines[i].replace("\t", "") # Elimina tabulaciones
	if lines[i].islower(): # Si la linea es SOLO minuscula
		seq += "".join(c for c in lines[i] if c.isalpha()) 
			# Captura solo letras minusculas
	# Guarda el resultado en un nuevo archivo
	with open('preproinsulin-seq-clean.txt', 'w') as output:
		output.write(seq)
	'''
		with open -> abre el archivo en modo escritura
		output -> variable para escribir en el archivo
		output.write -> escribe en el archivo (nombre_archivo)
		igual que el open, se utiliza los mismo modos
			https://www.w3schools.com/python/python_file_handling.asp
			https://www.w3schools.com/python/python_file_open.asp
			https://www.w3schools.com/python/ref_func_open.asp
	'''
	i += 1 # Incrementa el contador
#fin del while
fileIn.close() # Cerrar el archivo abierto de lectura
#Fin de la limpieza de texto
'''
	Se ha abierto el archivo preproinsulin-seq.txt
	elimnando los espacios en blanco, saltos de linea y tabulaciones
		https://www.w3schools.com/python/python_strings_methods.asp
		https://www.w3schools.com/python/python_ref_string.asp
	Capturadodo solo las letras minusculas
	(!!!) La lectura depende del formato del archivo ORIGEN es la unica  mayuscula
		Si se agrega una mayuscula en la secuencia, el programa no la detectara
		Es posible evitar el problema usando: import re
			seq = "".join(c for c in re.split(r'[^a-z]', fline[i]) if c.isalpha)
		Esta linea se encarga de eliminar los caracteres no deseados
		Capturando solo las letras minusculas pero depende de una libreria 
		Especificamente de la libreria re, 
			provee funciones para trabajar con expresiones regulares
				https://docs.python.org/3/library/re.html
				https://www.w3schools.com/python/python_regex.asp
	Se ha creado el archivo preproinsulin-seq-clean.txt
	Se ha cerrado el archivo preproinsulin-seq.txt
	Fin de la limpieza de texto
'''
# **************************************************************************** #
'''
Tenemos la secuencia de aminoacidos en el archivo preproinsulin-seq-clean.txt
Ahora nos toca obtener la secuencia de insulina
crear 4 archivos diferentes
	1. Isinsulin-seq-clean.txt
	2. binsulin-seq-clean.txt
	3. cinsulin-seq-clean.txt
	4. ainsulin-seq-clean.txt
Que tendran 24, 30, 35 y 21 caracteres respectivamente
'''
i = 0 # Inicializa el contador
fileIn = open("preproinsulin-seq-clean.txt", "r") # Lee el archivo
# Como el archivo tiene 110 caracteres una sola linea y solo minusculas
# Iremos leyendo cada caracter desde el punto inicial al final del loop 
# y guarndando en una variable para guardarlo en el archivo correspondiente
seq = fileIn.read() # Lee el archivo
data = "" # Inicializa la secuencia (variable a usar)
while i < 24:
	data += seq[i] # Guarda los 24 primeros caracteres
	i += 1 # Incrementa el contador
	with open('Isinsulin-seq-clean.txt', 'w') as output:
		output.write(data)
# Fin del primer archivo
# Hemos creado el primer archivo, las siguentes lineas de codigo son iguales
# Solo varia el nombre del archivo y el rango de caracteres
# Por ese motivo se dejara de comentar el codigo en los proximos archivos
data = "" # Limpia la variable
while i < 54:
	data += seq[i]
	i += 1
	with open('binsulin-seq-clean.txt', 'w') as output:
		output.write(data)
data = "" # Limpia la variable
while i < 89:
	data += seq[i]
	i += 1
	with open('cinsulin-seq-clean.txt', 'w') as output:
		output.write(data)
data = "" # Limpia la variable
while i < 110:
	data += seq[i]
	i += 1
	with open('ainsulin-seq-clean.txt', 'w') as output:
		output.write(data)
fileIn.close() # Cerrar el archivo
# Fin de la secuencia de insulina
'''
 De esta forma hemos automatizado el proceso de limpieza de texto
 la captura de la secuencia de aminoacidos
 y la separacion de la secuencia de insulina
 Si tenemos 20 archivos diferentes con el mismo formato
 Podemos cargarlos archivos y luego limpiarlos y tener la secuencia de aminoacidos
 Hay formas de mejorar el codigo
	EJM 
		1. Usar funciones para evitar repetir el mismo codigo
		2. Usar un bucle for para recorrer el archivo
		3. Usar una libreria para trabajar con expresiones regulares
Y formas de mejorar la automatizacion
	EJM
		1. Usar input para que el usuario ingrese el nombre del archivo
		2. Dar formato al nombre del archivo de salida, para diferenciar los archivos
		3. Tener una lista con los nombres de los archivos de entrada, capturarla y limpiarla usando los puntos anteriores
Todo depende de la necesidad del usuario y de lo que quieras aprender.
---
Se ha creado el archivo <analyze-insulin2.py>, donde se autmatiza el proceso de entrad y se mejora la logica
Aun tiene cuarto para mejorar, no esta explicado paso por paso, pero tien enotas en los puntos importantes
'''
