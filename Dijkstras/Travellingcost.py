__author__ = 'Binh Le'

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q
from heapq import *

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
            if(Ele!=[] and d+Ele[1]<(LDis[Ele[0]])):
                LDis[Ele[0]] = d+Ele[1]
                heappush(PQ,[LDis[Ele[0]],Ele[0]])
                Path[Ele[0]] = Node
    return [LDis,Path]

if __name__ == '__main__':
    N = (int)(input().split()[0])
    Des = []
    LDis = [1e9]*505
    Graph = [[] for x in range(0,505)]
    for c in range(0,N):
        Graph.append([])
        Inpath = [int(x) for x in input().split()]
        Graph[Inpath[0]].append([Inpath[1],Inpath[2]]) #v,w
        Graph[Inpath[1]].append([Inpath[0],Inpath[2]]) #u,w
    Source = (int)(input().split()[0])
    NDes = (int)(input().split()[0])
    for c in range(0,NDes):
        Des.append((int)(input().split()[0]))
    [LDis,Path] = Dijkstra(Graph,Source,LDis)
    for v in Des:
        if(LDis[v]!=1e9):
            print(LDis[v])
        else:
            print("NO PATH")
    pass