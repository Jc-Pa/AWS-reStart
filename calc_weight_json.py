# Python3.6
# Coding: utf-8

import jsonFileHandler

data = jsonFileHandler.readJsonFile('files/insulin.json')
# data = json.loads(data)
if data != "":
	bInsulin = data['molecules']['bInsulin']	
	aInsulin = data['molecules']['aInsulin']
	insulin = bInsulin + aInsulin
	molecularWeightInsulinActual = data['molecularWeightInsulinActual']
	print("bInsulin: " + bInsulin)
	print("aInsulin: " + aInsulin)
	print("molecularWeightInsulinActual: " + str(molecularWeightInsulinActual))

	# Calculating the molecular weight of insulin
	# Geting  list of the amino acids (AA) weights
	aaWeights = data['weights']
	# Count the number of each amino acids
	aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in \
			['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']})
	# Multiply the coun by the weights
	molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in \
			['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']}.values())
	print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
	print("Percent error: "+ str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual) * 100))
else:
	print("Error. Exiting program")

