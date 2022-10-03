# p ^ q = x
# x ^ q = p

arr = "af a5 a8 ae b2 a5 a0 a7 bc b1 96 ba a1 a6 bc a5 ad 96 a8 ad ad 96 a4 b0 96 a4 ac a4 af bb a6 ab b4".split()
modifs = [144, 89]

for i in modifs:
	inc = 0
	for a in arr:
		arr[inc] = hex(int(a, base=16) ^ i)
		inc += 1
for i in arr:
	print(chr(int(i, base=16)), end="")
print()
