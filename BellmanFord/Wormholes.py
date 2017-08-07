__author__ = 'Binh Le'

def BellmanFord(Graph,N,M):
    Path = [-1]*N
    LDis = [1e9]*N
    LDis[0]=0
    for id in range(0,N):
        for i in range(0,M):
            u = Graph[i][0]
            v = Graph[i][1]
            w = Graph[i][2]
            if(((LDis[u]+w)<LDis[v]) and LDis[u]!=1e9):
                LDis[v] = (LDis[u]+w)
                Path[v] = u
    for i in range(0,M):
            u = Graph[i][0]
            v = Graph[i][1]
            w = Graph[i][2]
            if((LDis[u]+w)<LDis[v] and LDis[u]!=1e9):
                return 1
    return 0

if __name__ == '__main__':
    NTc = (int)(input().split()[0])
    Des = []
    for d in range(0,NTc):
        N,M = input().split()
        N,M = int(N),int(M)
        Graph = [[] for x in range(0,N)]
        for c in range(0,M):
            Inpath = [int(x) for x in input().split()]
            Graph[c].append(Inpath[0]) #u, v,w
            Graph[c].append(Inpath[1]) #u, v,w
            Graph[c].append(Inpath[2]) #u, v,w
        if(BellmanFord(Graph,N,M)==1):
            print("possible")
        else:
            print("not possible")
    pass