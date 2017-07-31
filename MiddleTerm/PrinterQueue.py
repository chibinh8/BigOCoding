__author__ = 'Binh Le'
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

from heapq import *

def Handle(Arg,QIndex):
    Arg1 = Arg.copy()
    cnt = 0
    while(1):
        C = Arg.pop(0)
        if(Arg==[]):
            return cnt+1
        if(C<max(Arg)and QIndex!=0):
            Arg.append(C)
            QIndex -=1
        elif(C<max(Arg)):
            Arg.append(C)
            QIndex = len(Arg)-1
        elif(C>=max(Arg) and QIndex==0):
            return cnt+1
        else:
            QIndex -=1
            cnt +=1
    return cnt

if __name__ == '__main__':
    InputC =[]
    N = int(input().split()[0])
    for c in range(0,N):
        NumTest, QIndex = input().split()
        NumTest = int(NumTest)
        QIndex = int(QIndex)
        InputC = ([int(x) for x in input().split()])
        print(Handle(InputC,QIndex))
    pass