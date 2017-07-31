__author__ = 'Binh Le'

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q
from heapq import *

def FindCostUV(u,v,InpathAdd):
    Mind = 20001
    for c in InpathAdd:
        if(c[0]==u and c[1]==v):
            if(Mind>int(c[2])):
              Mind = int(c[2])
    return Mind
def Dijkstra(Graph,Source,LDis):
    PQ = []
    Path = [-1]*len(Graph)
    heappush(PQ,[0,Source]) #Push source with Distance = 0
    LDis[Source]=0
    while(len(PQ)>0):
        #pop the top item from Heap
        PopItem = PQ.pop() #Item = [Distance, Node]
        d = PopItem[0]
        Node = PopItem[1]
        for Ele in Graph[Node]:
            if(Ele!=[] and max(d,Ele[1])<(LDis[Ele[0]])):
                LDis[Ele[0]] = max(d,Ele[1])
                heappush(PQ,[LDis[Ele[0]],Ele[0]])
                Path[Ele[0]] = Node
    return [LDis,Path]

if __name__ == '__main__':
    T = (int)(input().split()[0])
    S = T
    Des = []
    LDis = [1e9]*505
    Graph = [[] for x in range(0,505)]
    while(T>0):
        if(input().split()==[]):
            n,m = input().split()
            n = int(n)
            m = int(m)
            for c in range(0,m):
                Inpath = [int(x) for x in input().split()]
                Graph[Inpath[0]].append([Inpath[1],Inpath[2]]) #v,w
                Graph[Inpath[1]].append([Inpath[0],Inpath[2]]) #u,w
        Tcity = int(input().split()[0])
        [LDis,Path] = Dijkstra(Graph,Tcity,LDis)
        print("Case "+ str(S-T+1)+":")
        for c in range(0,n):
                MaxC = 0
                ind =c
                if(LDis[c]!=1e9):
                  print(LDis[c])
                else:
                  print("Impossible")
        T -=1
        LDis = [1e9]*505
        LDisMax = [-1]*505
        Graph = [[] for x in range(0,505)]
    pass