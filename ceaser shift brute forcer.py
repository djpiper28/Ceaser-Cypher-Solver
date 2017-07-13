def dictionaryTest(text,i):
    dictionary=['queen','stuff','dank','nice','very','car','train','plane','kek','the','how','she','it','when','what','is','it','and','like','game','danny','tom','thomas','if','code','man']
    #above is the dictionary which has words
    words=0#counts the amount of words
    a=0
    while(a<len(dictionary)):
        aa=0
        while(text==dictionary[a]):
            while(text[aa]==dictionary[a+aa]):
                z=z+1
                aa=aa+1
        if(z==len(dictionary[a])):
           words=words+1
           print(dictionary[a])
    if(words>(i/10)):
        return True
    else:
        return False
def freqTest(text):
    test=0
    a=0#a-z is counting the amount of these letter
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    i=0
    j=0
    k=0
    l=0
    m=0
    n=0
    o=0
    p=0
    q=0
    r=0
    s=0
    t=0
    u=0
    v=0
    w=0
    x=0
    y=0
    z=0   
    while(test<len(text)):#if...=="a"... checks for letters and updates the count
        if(text[test]=="a"):
           a=a+1
        elif(text[test]=="b"):
           b=b+1
        elif(text[test]=="d"):
           d=d+1
        elif(text[test]=="c"):
           c=c+1
        elif(text[test]=="e"):
           e=e+1
        elif(text[test]=="f"):
           f=f+1
        elif(text[test]=="g"):
           g=g+1
        elif(text[test]=="h"):
           h=h+1
        elif(text[test]=="i"):
           i=i+1
        elif(text[test]=="j"):
           j=j+1
        elif(text[test]=="k"):
           k=k+1
        elif(text[test]=="l"):
           l=l+1
        elif(text[test]=="m"):
           m=m+1
        elif(text[test]=="n"):
           n=n+1
        elif(text[test]=="o"):
           o=o+1
        elif(text[test]=="p"):
           p=p+1
        elif(text[test]=="q"):
           q=q+1
        elif(text[test]=="r"):
           r=r+1
        elif(text[test]=="s"):
           s=s+1
        elif(text[test]=="t"):
           t=t+1
        elif(text[test]=="u"):
           u=u+1
        elif(text[test]=="v"):
           v=v+1
        elif(text[test]=="w"):
           w=w+1
        elif(text[test]=="x"):
           x=x+1            
        elif(text[test]=="y"):
           y=y+1                  
        elif(text[test]=="z"):
           z=z+1
        a=0
        test = test + 1
    if(max(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)==e):
        return True
    else:
        return False
def getnum(s):
    s=str(s)
    if(s=='a'):#a-z of letters tells you the number representation of the letter
        return 1
    elif(s=='b'):
        return 2
    elif(s=='c'):
        return 3
    elif(s=='d'):
        return 4
    elif(s=='e'):
        return 5
    elif(s=='f'):
        return 6
    elif(s=='g'):
        return 7
    elif(s=='h'):
        return 8
    elif(s=='i'):
        return 9
    elif(s=='j'):
        return 10
    elif(s=='k'):
        return 11
    elif(s=='l'):
        return 12
    elif(s=='m'):
        return 13
    elif(s=='n'):
        return 14
    elif(s=='o'):
        return 15
    elif(s=='p'):
        return 16
    elif(s=='q'):
        return 17
    elif(s=='r'):
        return 18
    elif(s=='s'):
        return 19
    elif(s=='t'):
        return 20
    elif(s=='u'):
        return 21
    elif(s=='v'):
        return 22
    elif(s=='w'):
        return 23
    elif(s=='x'):
        return 24
    elif(s=='y'):
        return 25
    elif(s=='z'):
        return 26
def getletter(s):
    s=int(s)
    if(s==1):
        return 'a'#a-z gets the letter the number represents
    elif(s==2):
        return 'b'
    elif(s==3):
        return 'c'
    elif(s==4):
        return 'd'
    elif(s==5):
        return 'e'
    elif(s==6):
        return 'f'
    elif(s==7):
        return 'g'
    elif(s==8):
        return 'h'
    elif(s==9):
        return 'i'
    elif(s==10):
        return 'j'
    elif(s==11):
        return 'k'
    elif(s==12):
        return 'l'
    elif(s==13):
        return 'm'
    elif(s==14):
        return 'n'
    elif(s==15):
        return 'o'
    elif(s==16):
        return 'p'
    elif(s==17):
        return 'q'
    elif(s==18):
        return 'r'
    elif(s==19):
        return 's'
    elif(s==20):
        return 't'
    elif(s==21):
        return 'u'
    elif(s==22):
        return 'v'
    elif(s==23):
        return 'w'
    elif(s==24):
        return 'x'
    elif(s==25):
        return 'y'
    elif(s==26):
        return 'z'
while(1):
    pt = input("plain ceaser cypher text\n").lower()#gets the cypher text in lower case
    checks=0#initilisation
    p=0#initilisation
    ptt=pt.split(" ")
    ptt=pt.split("1")
    ptt=pt.split("2")
    ptt=pt.split("3")
    ptt=pt.split("4")
    ptt=pt.split("5")
    ptt=pt.split("6")
    ptt=pt.split("7")
    ptt=pt.split("8")
    ptt=pt.split("9")
    ptt=pt.split("0")
    pt="".join(ptt)  #plaintexttranslate (spaces and numbers to null)
    i=0#used in a while loop
    a=1#used in alphabet loop  
    shift=1#initilisation
    alloutputs=list()#initilisation
    while(a<26):
        output=""#initialisation
        while(i<len(pt)):
            #print(i, pt, len(pt), output)
            g=getnum(pt[i])#gets the number representation of g
            if(g+shift>26):
                g=(g+shift)-26#performs shift of number over 26
            else:
                g=g+shift#performs shift of numbers below 26
            output=output+str(getletter(g))#gets the letter for g and adds it to the list output
            i = i + 1#loop variable
        print(output)#ptints the output
        alloutputs.append(output)#adds the output to alloutputs
        shift=shift+1#increases the shift
        i=0#loop variable
        a = a + 1#loop variable
    z=0#initilisation
    print(alloutputs)#prints a possible solution
    aa=0#initilisation
    while(aa<len(alloutputs)):#loop to perform frequency check for most likley solution
        if(freqTest(alloutputs[aa])==True):
           print("\n\n"+alloutputs[aa]+"\nis likley to be the correct solution - freq analysis")
        aa=aa+1#initilisation
    while(aa<len(alloutputs)):#loop to perform dictionary check for most likley solution
        if(dictionaryTest(alloutputs[aa],len(alloutputs))==True):
           print("\n\n"+alloutputs[aa]+"\nis likley to be the correct solution - dictionary search")
        aa=aa+1#initilisation
