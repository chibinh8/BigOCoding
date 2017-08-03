__author__ = 'Binh Le'

def BellmanFord(Graph,N,M):


    return 0

if __name__ == '__main__':
    NTc = (int)(input().split()[0])
    Des = []
    LDis = [1e9]*NTc
    Graph = [[] for x in range(0,NTc)]
    N,M = input().split()
    N,M = int(N),int(M)
    for d in range(0,NTc):
        for c in range(0,M):
            Inpath = [int(x) for x in input().split()]
            Graph[c].append(Inpath[0],[Inpath[1],Inpath[2]]) #u, v,w
            if(BellmanFord(Graph,N,M)==1):
                print("possible")
            else:
                print("not possible")
    pass