from pwn import *

conn = remote('challs.wreckctf.com', 31239)
conn.recvuntil(b'>', drop=True)
conn.sendline(b'2')
tofind = conn.recvline().decode()[9:-1]
flag = list('a'*len(tofind))
setchar = "{}_abcdefghijklmnopqrstubwxyz0123456789"
step = 0
def do(conn, flag, step, tofind, setchar):
    try:
        i = 0
        while i < len(setchar):
            conn.recvuntil(b'>', drop=True)
            conn.sendline(b'1\n' + (setchar[i]*len(tofind)).encode())
            ret = conn.recvline().decode()[30:-1]
            for j in range(len(ret)):
                if ret[j] == tofind[j]:
                    flag[j] = setchar[i]
            print(tofind)
            print("".join(flag))
            i += 1
        conn.close()
        return

    except EOFError:
        conn = remote('challs.wreckctf.com', 31239)
        do(conn, flag, step, tofind, setchar)

do(conn, flag, step, tofind, setchar)