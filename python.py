import os
from os import walk
import sys
from os import path
from hashlib import sha1 as hasher
	
	
def hashing(s1):
	h1= hasher()
	with open(s1, mode = 'rb') as f:
		while True:
			s2 = f.read(4096)
			if not s2:
				break
			h1.update(s2)
	return h1.digest()
	
	
def main():	
	s = sys.argv[1]
	h1 = hasher()
	way = []
	for path, _, files in walk(s):	
		for f in files:
			if f[0] != '.' and f[0] != '~' and not os.path.islink(f):
				way.append(os.path.join(path, f))
	d = {}
	for p in way:
		k = hashing(p)
		if k not in d:
			d[k] = [p]
        else:
			d[k].append(p)
	for hsh in d.values():
		if len(hsh) > 1:
			print(":".join(hsh))
if __name__ == "__main__":
	main()		
				
			
		
	
	

