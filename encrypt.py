import sys

def encrypt(key, file_name, dst_file):
	if not key:
		print "missing key"
		return -1
		
	plain = open(file_name, 'r')
	plain_message = plain.read()
	plain.close()
	i = 0
	crypt_message = ''
	for letter in plain_message:
		m = ord(letter)
		k = ord(key[i % len(key)])
		crypt_message += chr(m ^ k)
		i += 1

	if not dst_file:
		dst_file = "output.file"
	cript_file = open(dst_file,'w')
	cript_file.write(crypt_message)
	cript_file.close()
	print "Success"

def get_key(key_file):
	keys = open(key_file, 'r')
	key = ''
	rest_of_keys = keys.read()
	keys.close()

	first_key = True
	keys_remaining = ''
	for letter in rest_of_keys:
		if not first_key:
			keys_remaining += letter
		else:
			key += letter
		if letter == '\n':
			first_key = False
	fkeys = open(key_file, 'w')
	fkeys.write(keys_remaining)

	return key

encrypt(get_key(sys.argv[2]), sys.argv[1], sys.argv[3])