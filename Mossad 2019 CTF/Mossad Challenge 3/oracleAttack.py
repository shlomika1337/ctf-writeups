#!/usr/bin/python
import os
import sys
import binascii

encrypted_file = "intel.txt.enc"
unpadded_file = "unpadded.txt.enc"
decrypt_file = "decrypted.txt"

with open(encrypted_file , 'rb') as f:
	f.seek(39,0)
	f2 = open(unpadded_file , 'wb')
	while True:
		tmp = f.read(1)
		if not tmp:
			break
		f2.write(tmp)
		f.seek(4, 1)

file_stream = []
with open(unpadded_file, 'rb') as f:
	while True:
		tmp = f.read(16)
		if tmp == '':
			break
		file_stream += tmp
i = len(file_stream)-1
decryption = ''
with open(decrypt_file, 'wb') as f:
	while not (i==0):
		tmp1 = hex(ord(file_stream[i]))
		tmp2 = hex(ord(file_stream[i-1]))
		tmp1 = int(tmp1, 16)
		tmp2 = int(tmp2, 16)
		for j in xrange(0,256):
			tmp = hex(j).split('x')[-1]
			tmp = int(tmp,16)
			print tmp
			if tmp^tmp1 == tmp2:
				f.write(format(tmp, 'x'))
				break
		i=i-1
print decryption
