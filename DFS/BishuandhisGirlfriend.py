__author__ = 'USER'

from collections import deque

#Link: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/bishu-and-his-girlfriend/

def Handle(Arg, Arg1):
   StackRun  = []
   Path = []
   Visited = []
   Graph = []
   N = len(Arg)+1
   Distance = 0
   for c in range(0,N):
       Path.append(-1)
       Visited.append(False)
       Graph.append([])
   for c in range(0,N-1):
        Graph[int(Arg[c][0])-1].append(int(Arg[c][1]))
        Graph[int(Arg[c][1])-1].append(int(Arg[c][0]))
   StackRun.append(1)
   ParentNode = 1
   Visited[int(ParentNode)-1] = True
   print(Arg)
   while(len(StackRun)>0):
        print(StackRun)
        PopL = StackRun.pop()
        ParentNode = int(PopL)
        ListC = list(Graph[int(ParentNode)-1])
        for Ele in ListC:
          if(Visited[int(Ele)-1]==False):
              Visited[int(Ele)-1]=True
              Path[int(Ele)-1] = ParentNode
              if((int(Ele)>int(ParentNode))):
               StackRun.append(Ele)
   print(Path)
   return 0

if __name__ == '__main__':
    Arg = []
    Arg1 = []
    N = int(raw_input().split()[0])
    while(int(N-1)>0):
        ArgC = raw_input().split()
        Arg.append(ArgC)
        N -=1
    num = int(raw_input().split()[0])
    while(num>0):
        Arg1.append(raw_input().split())
        num -=1
    Handle(Arg, Arg1)
    pass