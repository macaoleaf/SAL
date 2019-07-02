#!/usr/bin/python
# -*- coding:utf-8 -*-
# import docx
from random import randint


def disordering_wordlist():
	# info for hugeTiger to modify
	#readFile = open('111.csv', encoding='gb18030', errors='ignore')
	readFile = open('111.csv', 'r')
	# readMode = ""
	writeFile = open('wordlist.csv', 'w')
	# writeMode = ""
	#readDict = open('Barron.txt', encoding='gb18030', errors='ignore')
	readDict = open('Barron.txt', 'r')
	wordNo = 1000

	# DO NOT change these codes
	dictionary = readDict.read()
	niceWords = dictionary.replace("\n", "").split()

	words = readFile.read()
	eachWord = words.split('\n')
	randPool = len(eachWord) - 1 # no. of words

	if wordNo > randPool:
		print("Words Overflow. There are only " + str(randPool) + " words in the given list!")
	else:
		count = 0
		indexList = []
		index = -1

		while count < wordNo:
			while index < 0 or indexList.count(index) <> 0:
				index = randint(0, randPool)
			indexList.append(index)
			word = eachWord[index].split(",")[0]
			if niceWords.count(word) <> 0:
				writeFile.write(word + '\n')
			count += 1

	writeFile.close()
	readDict.close()
	readFile.close()


if __name__ == '__main__':
    disordering_wordlist()