__author__ = 'USER'

def EvaluateInput(Arg):
    if(Arg==[]):
        return 0
    if(list(Arg).count(" ")!=0):
        return 0
    return 1
def Handle(Arg):
   for ChildList in Arg:
       if(EvaluateInput(ChildList)==1):
           Handle4OneInput(ChildList)

   return 1
def IsVal(Arg):
    if((Arg=='(')or(Arg==')')or(Arg=='+')or(Arg=='-')or(Arg=='*')or(Arg=='/')or(Arg=='^')):
        return 0
    return 1
def IsOperator(Arg):
    if((Arg=='+')or(Arg=='-')or(Arg=='*')or(Arg=='/')or(Arg=='^')):
        return 1
    return 0
def Handle4OneInput(Arg):
    StackVal = []
    StackOper =[]
    PrintStr = ""
    for c in Arg:
        if(IsVal(c)==1):
            StackVal.append(c)
        elif(IsOperator(c)==1):
            StackOper.append(c)
        elif(c==")"):
            a = ""
            b = ""
            if(len(StackVal)>=1):
             a = StackVal.pop()
             if(len(StackVal)>=1):
               b = StackVal.pop()
            if(len(StackOper)!=0):
                if(b!=""):
                    PrintStr +=b
                if(a!=""):
                    PrintStr +=a
                a=""
                b=""
                PrintStr +=StackOper.pop()
    print(PrintStr)

    return 0

if __name__ == '__main__':
    Arg = []
    N = int(raw_input().split()[0])
    while(N>0):
        Arg.append(raw_input())
        N -=1
    Handle(Arg)
    pass