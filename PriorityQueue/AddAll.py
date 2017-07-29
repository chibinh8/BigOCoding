__author__ = 'Binh Le'
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

from heapq import *

PriQ =[]

def Handle(Arg):
    Arg = list(Arg)
    if(Arg!=[]):
        Ele = Arg.pop()
        #PaEle = heappop(PriQ)
        #heappush(PriQ,PaEle)
        PaEle = PriQ[len(PriQ)-1]
        heappush(PriQ,Ele+PaEle)
        Handle(Arg)
    else:
        c1 = PriQ[len(PriQ)-1]
        c2 = PriQ[len(PriQ)-2]
        heappush(PriQ,c1)
        heappush(PriQ,c2)
        heappush(PriQ,c2+c1)
        return 1

if __name__ == '__main__':
    PriQ = []
    InputC =[]
    while(int(raw_input().split()[0])!=0):
        Input = raw_input().split()
        for c in Input:
            InputC.append(int(c))
        InputC.sort()
        heappush(PriQ,0)
        Handle(list(InputC))
        Out = nsmallest(1,PriQ)[0]
        print(Out)
        PriQ = []
    pass