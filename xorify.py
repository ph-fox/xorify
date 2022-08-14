
text ="label"
from_string = []
for char in text:
	from_string.append(ord(char))

from_int = []
for num in from_string:
	from_int.append(num^13)

text = ""
for char in from_int:
	text+=str(chr(char))

print(text)

