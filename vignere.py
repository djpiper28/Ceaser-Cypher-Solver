import cipher
import subprocess
c = cipher
print("""$$\      $$\                 $$\                 $$\                                
$$$\    $$$ |                $$ |                $$ |                               
$$$$\  $$$$ | $$$$$$\   $$$$$$$ | $$$$$$\        $$$$$$$\  $$\   $$\                
$$\$$\$$ $$ | \____$$\ $$  __$$ |$$  __$$\       $$  __$$\ $$ |  $$ |               
$$ \$$$  $$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |      $$ |  $$ |$$ |  $$ |               
$$ |\$  /$$ |$$  __$$ |$$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |               
$$ | \_/ $$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\       $$$$$$$  |\$$$$$$$ |               
\__|     \__| \_______| \_______| \_______|      \_______/  \____$$ |               
                                                           $$\   $$ |               
                                                           \$$$$$$  |               
                                                            \______/                
      $$\                     $$\                                $$$$$$\   $$$$$$\  
      $$ |                    \__|                              $$  __$$\ $$  __$$\ 
 $$$$$$$ |      $$\  $$$$$$\  $$\  $$$$$$\   $$$$$$\   $$$$$$\  \__/  $$ |$$ /  $$ |
$$  __$$ |      \__|$$  __$$\ $$ |$$  __$$\ $$  __$$\ $$  __$$\  $$$$$$  | $$$$$$  |
$$ /  $$ |      $$\ $$ /  $$ |$$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|$$  ____/ $$  __$$< 
$$ |  $$ |      $$ |$$ |  $$ |$$ |$$ |  $$ |$$   ____|$$ |      $$ |      $$ /  $$ |
\$$$$$$$ |      $$ |$$$$$$$  |$$ |$$$$$$$  |\$$$$$$$\ $$ |      $$$$$$$$\ \$$$$$$  |
 \_______|      $$ |$$  ____/ \__|$$  ____/  \_______|\__|      \________| \______/ 
          $$\   $$ |$$ |          $$ |                                              
          \$$$$$$  |$$ |          $$ |                                              
           \______/ \__|          \__|                                              """)
while(1):
	todo=input("Type the any of the following:\n'solve' to solve a vignere [not finished]\n'encrypt' to encrypt a vignere\n").lower()
	while (todo!="solve" and todo!="encrypt" and todo!="e" and todo!="s"):
		todo=input("Type:\n'solve' to solve a vignere\n'encrypt' to encrypt a vignere\n").lower()
	if(todo=="encrypt" or todo=="e"):
		plaintext=c.makeOnlyAlpha(input("Insert cipher text here.\n").lower())#gets inputs and removes spaces and numbers
		key=c.makeOnlyAlpha(input("Please insert a key here.\n").lower())#gets the key and removes non-alphabetical characters
		while (key=="" or key==None):
			key=c.makeOnlyAlpha(input("Please insert a key here.\n").lower())#gets the key and removes non-alphabetical characters
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
		key=input("If the key is know please enter it.\n").lower()
		if(key==""):#Brute forces
			print("No key detected, ###### please use a key as no brute force option is available for vignere.")
			print("#####     Work In Progress Brute Forcer     #####")
			key = 0
			alloutputs=[]
			output="init"
			Continue = False
			while (cipher.dictionaryTest(output)==False or Continue==True):
				Continue=False
				output=[]
				currentletter=0
				i=0
				while (currentletter<len(ciphertext)):
					out=c.getnum(ciphertext[currentletter])-c.getnum(cipher.intToBase26(key[i]))
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
				output="".join(output)
				print("Dictionary search and frequency check")
				if(cipher.dictionaryTest(output)==True or cipher.freuqTest(output)==True):
					print(output+" could be a solution!")
					if(input("Press 'a' to continue looking for results").lower()=="a"):
						Continue=True
				key = 0+1
			print("".join(alloutputs))
		else:
			key=c.makeOnlyAlpha(key)
		currentletter=0#current letter of string
		i=0#current letter of key 0=index
		if(key!=None or key!=""):#Solves with key
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