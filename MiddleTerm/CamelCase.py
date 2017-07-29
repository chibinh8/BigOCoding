__author__ = 'Binh Le'

if __name__ == '__main__':
    InputS = raw_input()
    cnt =0
    cntletter = 0
    for i, c in enumerate(InputS):
        if(c.isupper()and i<len(InputS)-1):
           if(InputS[i+1].islower()):
               cnt +=1
    if(len(InputS)==1 or (InputS[0].islower() and InputS[0].isupper())):
        print(0)
    else:
        print(cnt+1)
    pass