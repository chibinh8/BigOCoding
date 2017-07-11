__author__ = 'Binh Le'

def ValConve(c):
    if(c=="C"):
        return 12
    if(c=="O"):
        return 16
    if(c=="H"):
        return 1
    return 0

def Handle(Arg):
   MassInPa = 0
   Mass = 0
   OpenParentThe = False
   StackRecr = False
   StackLetter = []
   for c in Arg:
       if(c=="("):
          OpenParentThe = True
          StackLetter.append(c)
          if(MassInPa!=0 and (StackRecr==True)):
              Mass += MassInPa
              MassInPa =0
              StackRecr = False
       elif(c=="C" or c=="O" or c=="H"):
          if(OpenParentThe==True):
            StackLetter.append(c)
          else:
            Mass += ValConve(c)
       elif(c==")"):
          OpenParentThe = False
          while(StackRecr==False):
              ci = StackLetter.pop()
              if((ci>="2" and ci<="9")):
                MassInPa += int(ValConve(StackLetter.pop()))*(int(ci))
              elif(ci=="("):
                StackRecr = True
              else:
                MassInPa += int(ValConve(ci))
       elif(c>="2" and c<="9"):
           if(StackRecr==True):
             MassInPa = MassInPa*(int(c))
             if(c==Arg[len(Arg)-1]):
               Mass += MassInPa
           else:
             StackLetter.append(c)

           #   Mass += MassInPa*(int(c))
   return Mass

if __name__ == '__main__':
    Arg = []
    Arg = raw_input()
    print(Handle(Arg))
    pass