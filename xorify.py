def xorify(text, num):
	converted = ''.join([chr(x) for x in ([ord(x)^int(num) for x in text])])
	print(converted)

xorify('label',13)
