# We cant find a seeded random number, but there is method that changes the ip such that 0x15 is passed to decrypt

arg = 0x1337d00d

s1 = 'Q}|u'+'`sfg'+'~sf{'+'}|a3'

s2 = 'Congratulations!'


for i in range(16):
	key = ord(s1[i])^ord(s2[i])

print("Key:"+str(0x1337d00d-key))

