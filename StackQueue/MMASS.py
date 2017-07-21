__author__ = 'Binh Le'

def ValConve(c):
    if(c=="C"):
        return 12
    if(c=="O"):
        return 16
    if(c=="H"):
        return 1
    return 0

def IsVal(Arg):
    if((Arg=='(')or(Arg==')')or(Arg=='C')or(Arg=='O')or(Arg=='H')):
        return 0
    return 1

def IsLetter(Arg):
    if((Arg=='C')or(Arg=='O')or(Arg=='H')):
        return 1
    return 0

def Handle(Arg):
   Mass = 0
   StackMass = []
   MassTemp = 0
   OpenPar = False
   Temp = 0
   TempSum = 0
   for c in Arg:
      if(c=="("):
        StackMass.append(-1)
      elif(IsLetter(c)==1):
          StackMass.append(ValConve(c))
      elif(IsVal(c)==1):
          MassTemp = int(c)*StackMass.pop()
          StackMass.append(MassTemp)
      elif(c==")"):
        while(OpenPar==False):
            Temp = StackMass.pop()
            if(Temp==-1):
                OpenPar =True
                StackMass.append(TempSum)
            else:
                TempSum += Temp
        OpenPar = False
        TempSum =0
   while(len(StackMass)!=0):
       c = StackMass.pop()
       if(c!=-1):
           Mass +=c
   return Mass

if __name__ == '__main__':
    Arg = []
    Arg = raw_input()
    print(Handle(Arg))
    pass