
text = "label"

msg_int = []
for char in text:
	msg_int.append(ord(char)^13)

text = ""
for integers in msg_int:
	text+=chr(integers)
	
print(text)
