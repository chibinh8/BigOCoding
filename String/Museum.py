__author__ = 'Binh Le'

def Handle(Arg):
   MinTurn = 0
   MaxTurn = ord("z") - ord("a") + 1
   Ccomp = 'a'
   for c in Arg:
    MinTurn += min(abs(ord(c)-ord(Ccomp)),MaxTurn-abs(ord(c)-ord(Ccomp)))
    Ccomp = c
   return MinTurn


if __name__ == '__main__':
    Arg = []
    Arg = raw_input()
    print(Handle(Arg))
    pass