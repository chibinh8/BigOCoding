__author__ = 'Binh Le'
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

from heapq import *

if __name__ == '__main__':
    q = []
    N = int(raw_input().split()[0])
    Input = raw_input().split()
    for c in Input:
        InputC = int(c)
        heappush(q,InputC)
        if(len(q)<3):
            print(-1)
        else:
            List = nlargest(3,q)
            print(List[0]*List[1]*List[2])
    pass