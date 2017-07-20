import cipher
import math
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
while 1:
	text = cipher.makeOnlyAlpha(input("Text to hash.\n").lower())
	while (text == None):
		text = cipher.makeOnlyAlpha(input("Text to hash.\n").lower())
	i=0#used in a loop
	output=[]
	while (i<len(text)):
		out = math.ceil(16+hash(cipher.getnum(text[i])+int(math.sin(cipher.getnum(text[i]))*(len(text)+(cipher.getnum(text[i])/2))*(i/cipher.getnum(text[i]))+i)+cipher.getnum(text[i])*((i+5)*len(text)**2)))
		while (out<1):
			out=out+(len(text)*(i+1))**2+len(text)+2*(cipher.getnum(text[0]**2))
		while (out>26):
			if(out<=100):
				out = out - 26	
			elif(out>100 and out<500):
				out=out-50
			else:
				out=out-100
		if(out==None):
			out=out+(len(text)*(i+1))+2
		output.append(cipher.getletter(out))
		i=i+1
	print("\n"+"".join(output))
