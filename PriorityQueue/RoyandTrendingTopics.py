__author__ = 'Binh Le'
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

from heapq import *

def Handle(Arg):
    Arg = list(Arg)
    PriQ = []
    for c in Arg:
      NewS = c[2]*50 + c[3]*5 +c[4]*10 +c[5]*20
      DeltaSco = NewS -c[1]
      heappush(PriQ,[DeltaSco,c[0],NewS])
    LTọp = nlargest(5,PriQ)
    for c in LTọp:
      print(str(c[1]) + " "+ str(c[2]))
    return 1

if __name__ == '__main__':
    InputC =[]
    N = int(input().split()[0])
    for d in range(0,N):
        InputC.append([int(x) for x in input().split()])
    Handle(InputC)
    pass