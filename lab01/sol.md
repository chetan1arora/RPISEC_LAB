# Solutions for lab01 RPISEC/MBE

lab1A => Found Account creation facility:
It asks for name and serial number,
If serial number check passes, it will print something like you are authorized
Thought the serial is a char string, but was not able to find something on stack that points to a string
Tracing the program was difficult, due to ptrace call , also there was a timer for program running.

strcspn(Ist argument is provided username, IInd one is 0x8048d03) Used to strip '\n' or '\a'
At the address, it is 0a => '\n' so finding the length of line

strnlen(string, 0x20(32)) // Found that the username length should be greater than 5.

Then it was some routine, that make a key from username[3] and make serial from the username.

Finally made a serial code generator.

lab1B => Asks for password

Using ja instructions after sub x, const

If it takes jump, it uses rand argument to decrypt function, well we can bruteforce.

Otherwise, we can see that ja works only if CF=0 & ZF=0, using the CF flag, giving negative argument we can give any argument to decrypt function, also, it is a xor decryption, we just need to give the key


lab1C => Not a crackme




