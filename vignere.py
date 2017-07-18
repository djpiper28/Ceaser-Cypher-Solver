import cipher
c=cipher
while(1):
	todo=input("Type the any of the following:\n'solve' to solve a vignere [not finished]\n'encrypt' to encrypt a vignere\n").lower()
	while (todo!="solve" and todo!="encrypt" and todo!="e" and todo!="s"):
		todo=input("Type:\n'solve' to solve a vignere\n'encrypt' to encrypt a vignere\n").lower()
	if(todo=="encrypt" or todo=="e"):
		plaintext=c.makeOnlyAlpha(input("Insert cipher text here.\n").lower())#gets inputs and removes spaces and numbers
		key=c.makeOnlyAlpha(input("Please insert a key here.\n").lower())
		currentletter=0#current letter of string
		i=0#current letter of key
		output=[]
		while (currentletter<len(plaintext)):
			out=c.getnum(plaintext[currentletter])+c.getnum(key[i])
			if(out>26):
				out=out-26
			output.append(str(c.getletter(out)))#encrypts the current letter and 
			i=i+1
			if(i>=len(key)):
				i=0
			currentletter=currentletter+1
		print("\n"+"".join(output)+"\n")
	elif(todo=="solve" or todo=="s"):
		ciphertext=input("Insert cipher text here.\n")
		ciphertext=c.makeOnlyAlpha(ciphertext)
		key=input("If the key is know please enter it.").lower()
		if(key==""):
			print("\nSolving without the key\n")
		else:
			key=c.makeOnlyAlpha(key)
		currentletter=0#current letter of string
		i=0#current letter of key 0=index
		if(key!=None):
			output=[]
			while (currentletter<len(ciphertext)):
				out=c.getnum(ciphertext[currentletter])-c.getnum(key[i])
				if(out<1):
					out=26+out
				elif(out>26):
					out=out-26
				output.append(str(c.getletter(out)))			
				i=i+1
				if(i>=len(key)):
					i=0
				currentletter=currentletter+1
			print("".join(output))
		else:
			print("No key detected please use a key, no brute force option is available for vignere.")		