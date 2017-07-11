__author__ = 'Binh Le'
import sys

def Handle(Arg, Arg1):
   MinTurn = 0
   SpecialCase = False
   Out = ""
   Index = -1
   Len = len(Arg)-1
   for i, c in enumerate(reversed(Arg1)):
       if((ord(c)-ord(Arg[Len-i])>=1)and (i>(0))or((i<(len(Arg)-1))and((ord(c)-ord(Arg[Len-i])>1)))):
            if((c=="Z")and(Arg[Len-i]=="y")):
                Out = "Z"+ Out[i:]
                SpecialCase = True
            else:
                Out = chr(ord(Arg1[i])-1)+Out[i:]
            Index = i
            break
   Index = len(Arg)- Index
   if(Index!=-1):
     for i, c in enumerate(Arg1):
        if(i==Index):
             sys.stdout.write(Out)
        else:
            if(SpecialCase==True and (i>(Index+1))):
                sys.stdout.write("a")
            else:
                sys.stdout.write(c)
   else:
     print("No such string")
   return 0


if __name__ == '__main__':
    Arg = []
    Arg = raw_input()
    Arg1 = raw_input()
    Handle(Arg,Arg1)
    pass