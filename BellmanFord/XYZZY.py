__author__ = 'Binh Le'

def BellmanFord(Graph,N,M,ActlNode):
    if(M>N):
        N=M
    Path = [-1]*N
    LDis = [-1e9]*N
    LDis[0]=100
    PathNega = []
    for id in range(0,N):
        for i in range(0,M):
            u = Graph[i][0]-1
            v = Graph[i][1]-1
            w = Graph[i][2]
            if(((LDis[u]+w)>LDis[v]) and LDis[u]!=-1e9):
                LDis[v] = (LDis[u]+w)
                Path[v] = u+1
    for i in range(0,M):
            u = Graph[i][0]-1
            v = Graph[i][1]-1
            w = Graph[i][2]
            if((LDis[u]+w)>LDis[v] and LDis[u]!=-1e9):
                PathNega.append(u)
    Idex = ActlNode-1
    while(Path[Idex]!=-1):
        u = Path[Idex]-1
        Idex = u
        if(LDis[u]<=0):
            return 0
        elif(PathNega.count(u)!=0):
            return 1
    if(Idex!=0):
        return 0
    return 1

if __name__ == '__main__':
    NNodeL = 0
    while(NNodeL!=-1):
        NNodeL = (input().split())
        if (len(NNodeL)==1 and int(NNodeL[0])==-1):
            break
        NNode = int(NNodeL[0])
        M = 0
        MaxNode = NNode
        Graph = []
        LWsave =[]
        if(MaxNode>1):
            for d in range(0,NNode):
                E = [int(x) for x in input().split()]
                if(len(E)==1):
                    Graph.append([d+1,0,E[0]])
                    LWsave.append([d+1,E[0]])
                elif(len(E)>2 and E[1]<=len(E)-2):
                    M += E[1]
                    Ec = E[2:]
                    if(E[1]>0):
                        for c in range(0,E[1]):
                            if(MaxNode<E[c+2]):
                                    MaxNode = E[c+2]
                            Graph.append([d+1,E[c+2],E[0]])
                    else:
                        Graph.append([d+1,0,E[0]])
                    LWsave.append([d+1,E[0]])
            if(BellmanFord(Graph,MaxNode,M,NNode)==1):
                print("winnable")
            else:
                print("hopeless")
        elif(MaxNode==1):
            print("winnable")
    pass