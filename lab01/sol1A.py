u = input("[-]Generate serial from username:")
u = u.strip('\n')
specByte = 0xffffffff & ((ord(u[3])^0x1337)+ 0x5eeded)

for i in range(len(u)):
	# A routine that do some shifting and multiplying depending upon a keybyte from username
	a = ord(u[i])^specByte
	b = a
	c = 0x88233b2b
	c  = (0xffffffff00000000 & (b*c)) >> 32
	b =  b-c
	b =  b>>1
	b = 0xffffffff & (b+c)
	b = 0xffffffff & (b>>10)
	b = 0xffffffff & (b*0x539)
	a = a-b
	specByte += a
	specByte = 0xffffffff & specByte


print("[*]Generated Serial:"+str(specByte))

	
