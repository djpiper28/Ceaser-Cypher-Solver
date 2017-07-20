import math
print("cipher.py loaded, made by djpiper28.")
false = False
true = True
def contains(string, keyword):
    string = string.lower()
    if keyword in string: 
        print("In the string '"+string+"' the keyword '"+keyword+"' was found")
        return True
    else:
        return False
def dictionaryTest(text):#i is the length of the entire plain text, text is a list to check
    dictionary=['there','when','computers','explosion','encryption','dad','other','github','piper','father','ibm','international','hello','kind','sir','you','queen','stuff','dank','nice','very','car','train','plane','kek','the','how','she','it','when','what','is','it','and','like','game','danny','tom','thomas','if','code','man']
    #above is the dictionary which has words
    words=0#counts the amount of words
    a=0
    while(a<len(dictionary)):
        if(contains(text,dictionary[a])==True and len(dictionary[a])>3):
            words=words+1
        a=a+1
    if(words>=(len(text)/10)):
        return True
    else:
        return False
def intToBase26(integer):####################################################TO-FIX
    assert (1==1), "This method is broken"
    integer=math.ceil(integer)#incase someone doesn't know what an integer is
    if(integer<=26):
        return getletter(integer)#gets the letter for the int
    elif(integer>0):
        a = integer/26
        a = str(a).split(".")#splits of the decimal point
        print(a)
        out = getletter(len("z"*int(a[0]))) + (getletter( int( float("0."+a[1])*26) ))#gets a float of 0.a[1] then *26 to get an int then makes it an int and gets the letter
    else:
        print("oops")
        #assert (integer<0), "Error positive ints only please!"
    return str(out)
def freqTest(text):
    text = str(text)
    test = 0#Used in a loop
    aToZCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#sets the value for all of the letters to 0, each letter is a part of this array.
    while(test<len(text)):#if...=="a"... checks for letters and updates the count
        i=0
        while(i<len(aToZCount)-1):
            if(text[test]==getletter(i+1)):
                a = int(aToZCount[i]) + 1
                aToZCount[i] = a
            i=i+1
        test = test + 1
    if(max(aToZCount)==aToZCount[4]):
        return True
    else:
        return False
def getnum(s):
    s=str(s).lower()
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
        print("Error "+a+" is not a valid letter for method getLetter()")
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
    things = [" ",",",".",";",":","^","$"]#speeds up proccess by checking for common things here
    for x in things:
        pt="".join(pt.split(x))
    pt="".join(pt)  #plaintexttranslate (spaces and numbers to null(code above))
    if(pt.isalpha()==True):
        return pt
    else:
        i=0
        while(i<len(pt)):
            if(pt[i].isalpha()==False):    
                pt="".join(pt.split(pt[i]))
            i = i + 1
    return pt
