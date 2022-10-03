from pwn import *

conn = remote('challs.wreckctf.com', 31522)

print(conn.recvuntil(b'>', drop=True))
conn.sendline(b'2\n' + b'a')
ret = conn.recvline().decode()
unpadded = ret[ret.index("token:")+7:-1]

conn.recvuntil(b'>', drop=True)
conn.sendline(b'2\n' + b'a' * 16 + b'gary')
ret = conn.recvline().decode()

token = ret[ret.index("token:")+7+len(unpadded):-1]
print("token:", token)

conn.recvuntil(b'>', drop=True)
conn.sendline(b'1\n' + token.encode())

flag = conn.recvline().decode()
print(flag)

conn.close()
