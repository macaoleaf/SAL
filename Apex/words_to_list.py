def words_to_list():
	# info for hugeTiger to modify
	# readFile = open('Barron.txt', encoding='gb18030', errors='ignore')
	readFile = open('Barron.txt', 'r')
	writeFile = open('words_to_list.txt', 'w')

	text = readFile.read()
	words = text.replace("\n", "").split()
	for word in words:
		writeFile.write(word + '\n')
	writeFile.close()
	readFile.close()


if __name__ == '__main__':
	words_to_list()