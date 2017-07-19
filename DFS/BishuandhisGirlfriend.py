__author__ = 'USER'

from collections import deque

#Link: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/bishu-and-his-girlfriend/
def FindFirstNode(Gra, ListGirl):
   ID =0
   for d in range(0,len(Gra)):
       for c in Gra[d]:
           if(ListGirl.count(str(c))>0):
             ID = int(c)
             return ID

def Handle(Arg, Arg1):
   StackRun  = []
   Path = []
   Visited = []
   Graph = []
   N = len(Arg)+1
   ListGirl = []
   Distance = 0
   ID = 0
   for c in Arg1:
       ListGirl.append(c[0])
   for c in range(0,N):
       Path.append(-1)
       Visited.append(False)
       Graph.append([])
   for c in range(0,N-1):
        Graph[int(Arg[c][0])-1].append(int(Arg[c][1]))
        Graph[int(Arg[c][1])-1].append(int(Arg[c][0]))
   ID = FindFirstNode(Graph, ListGirl)
   StackRun.append(1)
   ParentNode = 1
   Visited[int(ParentNode)-1] = True
   MinDist = 1
   Dist = 0
   PrevDist = 0
   while(len(StackRun)>0):
        PopL = StackRun.pop()
        ParentNode = int(PopL)
        ListC = list(Graph[int(ParentNode)-1])
        if(Dist<MinDist and Dist>=1 and Arg1.count(ParentNode)>0):
            ID = ParentNode
            MinDist = Dist
        if(ListGirl.count(str(ParentNode))>0):
            Dist = PrevDist
        else:
            Dist +=1
            PrevDist = Dist
        for Ele in ListC:
          if(Visited[int(Ele)-1]==False):
              Visited[int(Ele)-1]=True
              Path[int(Ele)-1] = ParentNode
              if((int(Ele)>int(ParentNode))):
               StackRun.append(Ele)
   print(ID)
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