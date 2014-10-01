#!/usr/bin/python

import string
import sys


cipher_to_alphabet = {} #the dictionary for the ciphertext to alphabet matching
cipher_text = sys.stdin.readline() #input from stdin
key = 'BLUE' #hardcoded key
input = [i for i in key+' '+ string.ascii_uppercase[::-1]] #list of cipher alphabet without removing the duplicates
alphabet = string.ascii_uppercase+' ' #alphabet in correct order with the space character(doesn't affect space complexity much one could do away with it all together but makes code readable)
cipher_text_length = len(cipher_text)


#*********to delete duplicates from the intermediate*********
def count_and_del(input_list, char):
	count = 0
	i = 0
	while i < len(input_list):
		if input_list[i] == char:
			count += 1
			if count == 2:
				del input[i]
				break
		i += 1
			

for i in range(0, len(input)):
	if(len(input) == 27): #since length of our alphabet is 27 this saves needless iterations 
		break

	x = count_and_del(input, input[i])
	

#********** this creates a mapping between the cipher_alphabet and the regular order alphabet ******
for i in range(0,27):
	cipher_to_alphabet[input[i]] = alphabet[i]

plain_text = ['' for i in range(0,cipher_text_length)] # creates a plain text string of length same as the cipher text

#******finally the actual decryption*****
for i in range(0, cipher_text_length):
	if cipher_text[i] == '\n':
		continue
	plain_text[i] = cipher_to_alphabet[cipher_text[i]]
	
sys.stdout.write(''.join(plain_text)+"\n") 	
