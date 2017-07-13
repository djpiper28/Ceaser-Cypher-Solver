def getnum(s):
    s=str(s)
    if(s=='a'):
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
        return 'a'
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
    pt=input("text to encrypt\n").lower()#gets the input text in lower case
    shift=int(input("shift number\n"))#gets the integer shift number
    while(shift>26 or shift<1):
        shift=int(input("shift number\n"))#loop so that it is compatible
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
    ptt=pt.split(" ")
    pt="".join(ptt)  #plaintexttranslate (numbers and spaces to null)
    i=0#used in a while loop
    output=[]
    while(i<len(pt)):#encryption algarithm that i can't be bothered to annotate
        g=getnum(pt[i])
        if(g+shift>26):
            g=(g+shift)-26
        else:
            g=g+shift
        i=i+1
        output.append(getletter(g))
    print("".join(output))
