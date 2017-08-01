#!/usr/bin/python


from random import randint


listOfDicts = []
wordFrequency = {}


def readText(text):
	global wordFrequency
	global listOfDicts
	currDict = {"Preceding Word": ""}
	startOfWord = 0
	prevWord = ""
	shouldAdd = True
	currChar = 0
	index = 0
	while currChar != len(text):
		if text[currChar].isalnum() or (ord(text[currChar]) > 32 and ord(text[currChar]) < 48):
			startOfWord = currChar
			while text[currChar].isalnum() or (ord(text[currChar]) > 32 and ord(text[currChar]) < 48):
				currChar += 1
			if prevWord != "":
				while index != len(listOfDicts):
					currDict = listOfDicts[index]
					if currDict["Preceding Word"] == prevWord:
						shouldAdd = False
						break
					index += 1
				if shouldAdd:
					currDict = {"Preceding Word": prevWord}
					listOfDicts.append(currDict)
				shouldAdd = True
				currDict = listOfDicts[index]
				index = 0
				if currDict.has_key(text[startOfWord:currChar]):
					currDict[text[startOfWord:currChar]] += 1
				else:
					currDict[text[startOfWord:currChar]] = 1
				currDict = {"Preceding Word": ""}
			if wordFrequency.has_key(text[startOfWord:currChar]):
				wordFrequency[text[startOfWord:currChar]] += 1
			else:
				wordFrequency[text[startOfWord:currChar]] = 1
			prevWord = text[startOfWord:currChar]
		currChar += 1

def pickFromDict(dictionary):
	sumOfInts = 0
	for key in dictionary:
		if type(dictionary[key]) is int:
			sumOfInts += dictionary[key]
	r = randint(0, sumOfInts-1)
	sumOfInts = 0
	for key in dictionary:
		if type(dictionary[key]) is int:
			sumOfInts += dictionary[key]
			if r < sumOfInts:
				return key

def genMarkovChain(amountOfSentences):
	count = 0
	lastWordPlaced = "."
	outputText = ""
	while count != amountOfSentences:
		while '.' in lastWordPlaced:
			lastWordPlaced = pickFromDict(wordFrequency)
		outputText += lastWordPlaced.capitalize() + ' '
		while '.' not in lastWordPlaced:
			for currDict in listOfDicts:
				if currDict["Preceding Word"] == lastWordPlaced:
					lastWordPlaced = pickFromDict(currDict)
					outputText += lastWordPlaced + ' '
					break
		count += 1
	return outputText


readText(open("input.txt").read())
print genMarkovChain(7)

