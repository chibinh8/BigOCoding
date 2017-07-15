__author__ = 'USER'

from collections import deque

#Link: https://www.hackerrank.com/challenges/bfsshortreach

def Handle(Arg):
   QueueRun  = deque()
   Path = []
   Visited = []
   Graph = []
   for c in range(0,int(Arg[0][0])):
       Path.append(-1)
       Visited.append(False)
       Graph.append([])
   for c in range(0,int(Arg[0][1])):
        Graph[int(Arg[c+1][0])-1].append(Arg[c+1][1])
        Graph[int(Arg[c+1][1])-1].append(Arg[c+1][0])
   QueueRun.extend(Arg[len(Arg)-1])
   Visited[0] = True
   ParentNode = Arg[len(Arg)-1]
   print(Graph)
   while(len(QueueRun)>0):
        PopL = QueueRun.popleft()
        ParentNode = PopL[0]
        print(PopL)
        if(len(PopL)>1):
         QueueRun.extend(PopL[1])
        ListC = list(Graph[int(ParentNode)-1])
        for Ele in ListC:
          if(Visited[int(Ele)-1]==False):
              Visited[int(Ele)-1]=True
              Path[int(Ele)-1] = ParentNode
              if((int(Ele)>int(ParentNode))):
               QueueRun.extend(Ele)
        print(QueueRun)
   print(Path)
   print(Visited)
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
        Arg=[]
        N -=1
    pass