#!/usr/bin/python
# -*- coding:utf-8 -*-
import re


def find_related_sentence():
	# info for hugeTiger to modify
	# readFile = open('联邦党人文集【英文版】.txt', encoding='gb18030', errors='ignore')
	readFile = open('联邦党人文集【英文版】.txt', 'r')
	writeFile = open('sentences.txt', 'w')
	sentenceNo = 100
	word = "judgment"

	# DO NOT change these codes
	text = readFile.read()
	parser = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!|\;)\s', text)

	count = 0
	for sentence in parser:
		if word.lower() in sentence.lower() and count < sentenceNo:
			writeFile.write("No. " + str(count + 1) + ": " + sentence + '\n')
			count += 1

	writeFile.close()
	readFile.close()


if __name__ == '__main__':
	find_related_sentence()