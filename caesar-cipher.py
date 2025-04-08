# Python3.6
# Coding: utf-8

# Sumado de caracteres
def getDoubleAlphabet(alphabet):
	doubleAlphabet = alphabet + alphabet
	return doubleAlphabet
# Peticion de mensaje a encriptar
def getMessage():
	StringToEncrypt = input("Please enter a message to encrypt: ")
	return StringToEncrypt
# Clave de cifrado
def getCipherKey():
	shiftAmount = input("Please enter a Key (whole number from 1-25): ")
	return shiftAmount
# Algoritmo de cifrado
def encryptMessage(message, cipherKey, alphabet):
	encryptedMessage = ""
	uppercaseMessage = ""
	uppercaseMessage = message.upper()
	for currentCharacter in uppercaseMessage:
		position = alphabet.find(currentCharacter)
		newPosition = position + int(cipherKey)
		if currentCharacter in alphabet:
			encryptedMessage = encryptedMessage + alphabet[newPosition]
		else:
			encryptedMessage = encryptedMessage + currentCharacter
	return encryptedMessage
# Algoritmo de descifrado
def decryptMessage(message, cipherKey, alphabet):
	decryptKey = -1 * int(cipherKey)
	return encryptMessage(message, decryptKey, alphabet)
# Funcion principal
def runCaesarCipherProgram():
	myAlphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	print(f'Alphabet: {myAlphabet}')
	myAlphabet2 = getDoubleAlphabet(myAlphabet)
	print(f'Alphabet2: {myAlphabet2}')
	myMessage = getMessage()
	print(myMessage)
	myCipherKey = getCipherKey()
	print(myCipherKey)
	myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
	print(f'Encrypted Message: {myEncryptedMessage}')
	myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
	print(f'Decrypted Message: {myDecryptedMessage}')
runCaesarCipherProgram()