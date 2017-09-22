import os
from os import walk
import sys
from os import path
from hashlib import sha1 as hasher
	
	
s = input()
d = dict()
hasher = hasher()
for path, _, files in walk(s):	
	for f_names in files:
		if f_files[0] != '.' and f.files[0] != '~' :
			n = h1.update(path +'/' + f_names).hexdigest()
			if n not in d:
				d[n] = [1, path + '/' + f_names]
			else:
				d[n][0] = 2
				d[n][1] += ":" + path + '/' + f_names
for hsh in d:
	if d[hsh][0] == 2:
		print(d[hsh][1] + '\n')
				
				
			
		
	
	

