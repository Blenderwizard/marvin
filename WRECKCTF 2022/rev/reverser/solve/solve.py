# (a + x) mod m = b
# x = (b - a) mod m

def rev_license(target):
	target = "9" + target
	r = len(target)
	s = [9]
	for i in range(1,r):
		s.append((int(target[i],16) - int(target[i - 1],16)) % 16)
		if (s[-1] < 0):
			s[-1] = s[-1] % 16
	return ''.join(f'{c:x}' for c in s[1:])

def check_license(license):
	characters = set('0123456789abcdef')
	s = [9]
	for c in license:
		if c not in characters:
			return False
		s.append((s[-1] + int(c, 16)) % 16)
	target = '51c49a1a00647b037f5f3d5c878eb656'
	return ''.join(f'{c:x}' for c in s[1:]) == target
		

print(rev_license('51c49a1a00647b037f5f3d5c878eb656'))
print(check_license(rev_license('51c49a1a00647b037f5f3d5c878eb656')))