import os
import string
import random
import sys

def generate_files(length_of_key, number_of_keys):
	file1 = open(r'keys/alice_keys.key', 'w')
	file2 = open(r'keys/bob_keys.key', 'w')
	for i in range(int(number_of_keys)):
		line = ''
		for k in range(int(length_of_key)):
			line += random.choice(string.ascii_letters + string.digits)
		line += '\n'
		file1.write(line)
		file2.write(line)


newFolder = r'keys'
if not os.path.exists(newFolder): os.makedirs(newFolder)
generate_files(sys.argv[1], sys.argv[2])