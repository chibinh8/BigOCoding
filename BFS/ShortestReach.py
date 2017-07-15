__author__ = 'USER'

#Link: https://www.hackerrank.com/challenges/bfsshortreach

def Handle(Arg):
   QueueRun = []
   Path = []
   Visited = []
   Graph = []
   for c in range(0,int(Arg[0][0])):
       Path.append(-1)
       Visited = "false"
       Graph.append([])
   for c in range(0,int(Arg[0][1])):
        Graph[int(Arg[c+1][0])].append(Arg[c+1][1])
        print(Arg[c+1][1])
   print(Graph)
   return 0

if __name__ == '__main__':
    Arg = []
    N = int(raw_input().split()[0])
    while(int(N)>0):
        ArgC = raw_input().split()
        Arg.append(ArgC)
        num = int(ArgC[1])+1
        while(num>0):
            Arg.append(raw_input().split())
            num -=1
        Handle(Arg)
        N -=1
    pass