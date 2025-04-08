# Python3.6
# Coding: utf-8
import json

def readJsonFile(fileName):
	data = ""
	try:
		with open('files/insulin.json') as json_file:
			data = json.load(json_file)
	except IOError:
		print("Could no read file")
	return data


