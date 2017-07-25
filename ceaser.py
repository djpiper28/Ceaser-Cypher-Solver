import cipher
c = cipher
while 1:
    todo=input("Type the any of the following:\n'solve' to solve a ceaser \n'encrypt' to encrypt a vignere\n").lower()
    while (todo!="solve" and todo!="encrypt" and todo!="e" and todo!="s"):
        todo=input("Type:\n'solve' to solve a vignere\n'encrypt' to encrypt a ceaser\n").lower()
    if(todo=="solve" or todo=="s"):
        pt = input("plain ceaser cypher text\n").lower()#gets the cypher text in lower case
        pt = c.makeOnlyAlpha(pt)
        checks=0#initilisation
        p=0#initilisation  
        i=0#used in a while loop
        a=1#used in alphabet loop  
        shift=1#initilisation
        alloutputs=list()#initilisation
        while(a<26):
            output=""#initialisation
            while(i<len(pt)):
                #print(i, pt, len(pt), output)
                g=c.getnum(pt[i])#gets the number representation of g
                if(g+shift>26):
                    g=(g+shift)-26#performs shift of number over 26
                else:
                    g=g+shift#performs shift of numbers below 26
                output=output+str(c.getletter(g))#gets the letter for g and adds it to the list output
                i = i + 1#loop variable
            print(output)#ptints the output
            alloutputs.append(output)#adds the output to alloutputs
            shift=shift+1#increases the shift
            i=0#loop variable
            a = a + 1#loop variable
        z=0#initilisation
        print("\nPerforming dictionary searches now.")
        aa=0
        while(aa<len(alloutputs)):#loop to perform dictionary check for most likley solution
            if(c.dictionaryTest(alloutputs[aa])==True):
               print("\n\n'"+alloutputs[aa]+"' is likley to be the correct solution - dictionary search")
            aa=aa+1#loop thing
        aa=0#initilisation
        print("\nPerforming frequency checks now.")
        while(aa<len(alloutputs)):#loop to perform frequency check for most likley solution
            if(c.freqTest(alloutputs[aa])==True):
               print("\n\n'"+alloutputs[aa]+"' is likley to be the correct solution - freq analysis")
            aa=aa+1#loop thing
    elif(todo=="encrypt" or todo=="e"):
        pt=input("text to encrypt\n").lower()#gets the input text in lower case
        pt=cipher.makeOnlyAlpha(pt)
        shift=int(input("shift number\n"))#gets the integer shift number
        while(shift>26 or shift<1):
            shift=int(input("shift number\n"))#loop so that it is compatible
        i=0#used in a while loop
        output=[]#Initilisation
        while(i<len(pt)):#Encryption loop
            g=c.getnum(pt[i])#just so that I don't have to copy the code a lot more.
            if(g==None):#Checks for null
                print(g+" Errored, should not be None")
            elif(g+shift>26):#checks if the shift is greater value is greater than 26(highest it could be) then makes it smaller
                g=(g+shift)-26
                output.append(c.getletter(g))
            else:#Applies the shift and saves it to the array output
                g=g+shift
                output.append(c.getletter(g))
            i=i+1#loop thing
        print("".join(output))#joins the lsit/array output and prints it to the console
print("Error, 1!=1")