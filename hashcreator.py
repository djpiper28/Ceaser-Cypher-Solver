import cipher
import math
while 1:
	text = cipher.makeOnlyAlpha(input("Text to hash.\n"))
	while (text == None):
		text = cipher.makeOnlyAlpha(input("Text to hash.\n").lower())
	i=0#used in a loop
	output=[]
	while (i<len(text)):
		out = hash(cipher.getnum(text[i])+int(cipher.getnum(text[i])*(len(text)+(cipher.getnum(text[i])/2))*(i/cipher.getnum(text[i]))+i)+cipher.getnum(text[i]))
		while (out<1):
			out=out+(len(text)*(i+1))+2+len(text)
		while (out>26):
			out = out - 26	
		if(out==None):
			out=out+(len(text)*(i+1))+2
		output.append(cipher.getletter(out))
		i=i+1
	print("".join(output))
