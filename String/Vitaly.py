__author__ = 'Binh Le'
import sys

def Handle(Arg, Arg1):
   MinTurn = 0
   Out = ""
   Index = -1
   for i, c in enumerate(Arg1):
       if(ord(c)-ord(Arg[i])>1):
            Out = chr(ord(c) -1)+Out[i:]
            Index = i
   if(Index!=-1):
     for i, c in enumerate(Arg1):
        if(i==Index):
            sys.stdout.write(Out)
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