from pyblake2 import blake2b
from threading import Thread
import random
import time
import sys

STOP_TH = False
POW = ""
GINC = 0

class Th(Thread): # threads to calculate the pow
	def __init__ (self, num, _hash):
		sys.stdout.write("Making thread number " + str(num) + "n\n")
		sys.stdout.flush()
		Thread.__init__(self)
		self.num = num
		self._hash = _hash

	def run(self):
		global STOP_TH
		global POW
		global GINC
		hash_bytes = bytearray.fromhex(self._hash)
		test = False
		was = False
		inc = 0
		while not test:
				GINC += 1
				inc += 1
				random_bytes = bytearray((random.getrandbits(8) for i in range(8)))		# generate random array of bytes
				for r in range(0,256):
					random_bytes[7] =(random_bytes[7] + r) % 256						# iterate over the last byte of the random bytes
					h = blake2b(digest_size=8)
					h.update(random_bytes)
					h.update(hash_bytes)
					final = bytearray(h.digest())
					final.reverse()
					test = pow_threshold(final)
					if test: 
						STOP_TH = True
						was = True
						break
					elif STOP_TH:
						test = True
						break
			
		random_bytes.reverse()
		if was:
			POW = random_bytes.hex()

def pow_threshold(check):
	if check > b'\xFF\xFF\xFF\xC0\x00\x00\x00\x00': 
		return True
	return False

def pow_validate(pow, hash): # validates the pow/hash pair
	pow_data = bytearray.fromhex(pow)
	hash_data = bytearray.fromhex(hash)
	
	h = blake2b(digest_size=8)
	pow_data.reverse()
	h.update(pow_data)
	h.update(hash_data)
	final = bytearray(h.digest())
	final.reverse()
	
	return pow_threshold(final)
	
def pow_generate(_hash): # main flow

	tn = 12
	ths = []

	print(_hash)
	print("Starting proof of work calculation...")

	init = time.time()
	
	for i in range(tn):
		ths.append(Th(i, _hash))
		ths[i].start()

	for x in ths:
	     x.join()

	end = time.time()
	et = end - init

	print("work:")
	print(POW)
	print("iterations: " + str(GINC))
	print("execution time: " + str(et))
	print("rate: " + str(int(GINC/et)) + " iterations per second" )


#--------------------------------------------------------------------------#

#_hash = "718CC2121C3E641059BC1C2CFC45666C99E8AE922F7A807B7D07B62C995D79E2"

#pow_generate(_hash)


