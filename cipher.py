print("cipher.py loaded, made by djpiper28.")
false = False
true = True
def contains(string, keyword):
    string = string.lower()
    if keyword in string: 
        print("In the string "+string+" the keyword "+keyword+" was found")
        return True
    else:
        return False
def dictionaryTest(text):#i is the length of the entire plain text, text is a list to check
    dictionary=['when','computers','explosion','encryption','dad','other','github','piper','father','ibm','international','hello','kind','sir','you','queen','stuff','dank','nice','very','car','train','plane','kek','the','how','she','it','when','what','is','it','and','like','game','danny','tom','thomas','if','code','man']
    #above is the dictionary which has words
    words=0#counts the amount of words
    a=0
    while(a<len(dictionary)):
        if(contains(text,dictionary[a])==True):
            words=words+1
        a=a+1
    if(words>=1):
        return True
    else:
        return False
def freqTest(text):
    text = str(text)
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
        test = test + 1
    if(max(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)==e):
        return True
    else:
        return False
def getnum(s):
    s=str(s).lower()
    assert (s.isalpha()==True), s+" Was not a letter in the alphabet!"
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
    elif(s.isalpha()==False):
        return 999
def getletter(s):
    if(s==None or s<=0 or s>26):
        return ''
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
def makeOnlyAlpha(pt):
    things = [" ","1","2","3","4","5","6","7","8","9","0","'","."]
    for x in things:
        pt="".join(pt.split(x))
    pt="".join(pt)  #plaintexttranslate (spaces and numbers to null(code above))
    if(pt.isalpha()==True):
        return pt
    else:
        print("Unrecognised letters detected, removing these now.")
        i=0
        while(i<len(pt)):
            if(pt[i].isalpha()==false):
                pt[i]=""
            i = i + 1