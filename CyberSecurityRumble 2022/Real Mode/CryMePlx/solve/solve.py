from pwn import *

setchar = "{}_abcdefghijklmnopqrstubwxyz0123456789"
charset = 'abcdefghijklnmopqrstuvwxyz_}{ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

buffer = "a" * 25
flag = list(buffer)

for char in charset:
	buffer = char * 25
	p = remote('chall.rumble.host', 2734)
	cipher = p.recvline().decode()
	print(cipher)
	p.sendline(buffer.encode())
	attempt = p.recvline()[len("Encrypt this string:"):-1].decode()
	print(attempt)
	for i in range(0, len(cipher) - 2, 2):
		c = cipher[i] + cipher[i + 1]
		a = attempt[i] + attempt[i + 1]
		if c == a:
			flag[i // 2] = buffer[i // 2]
	p.close()

print("".join(flag))