__author__ = 'USER'

from collections import deque

#Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1610
def IsParentInList(Node,Grap,Path):
    FoundPath = list(Path)
    IsFound = False
    for c in reversed(list(Path)):
        for cd in list(Grap[c-1]):
            if(cd==Node and c!=Path[len(Path)-1]):
                IsFound = True
                return True,FoundPath
        FoundPath.pop()

    return False,Path

def Handle(Arg, Arg1):
   StackRun  = []
   Path = []
   Visited = []
   Graph = []
   N = Arg1[1]
   Path = []
   PathTrace = []
   for c in range(0,Arg1[0]):
       Path.append(-1)
       Visited.append(False)
       Graph.append([])
   for c in range(0,N):
        if(list(Graph[int(Arg[c][0])-1]).count(int(Arg[c][1]))==0):
         Graph[int(Arg[c][0])-1].append(int(Arg[c][1]))
   N=len(Graph)
   for cd in range(1,Arg1[0]+1) :
       if(Graph[cd-1]!=[]):
           StackRun.append(cd)
           ParentNode = cd
           Visited[ParentNode-1]=True
           while(len(StackRun)>0):
                PopL = StackRun.pop()
                ParentNode = int(PopL)
                IsPaLis = IsParentInList(ParentNode,Graph,PathTrace)
                IsPa = IsPaLis[0]
                if(IsPa==True):
                    PathTrace = IsPaLis[1]
                PathTrace.append(ParentNode)
                ListC = list(Graph[int(ParentNode)-1])
                for Ele in ListC:
                  if(Visited[int(Ele)-1]==False):
                      StackRun.append(Ele)
                      Visited[int(Ele)-1]=True
                      Path[int(Ele)-1] = ParentNode
                  if(PathTrace.count(Ele)==1):
                      return "SIM"
           StackRun = []
           PathTrace =[]
           for c in range(0,Arg1[0]):
               Visited[c] = False
               Path[c] =-1
   return  "NAO"

if __name__ == '__main__':
    Arg = []
    Arg1 = []
    N = int(raw_input().split()[0])
    while(int(N)>0):
        FirstAr = raw_input().split()
        NumofDoc = int(FirstAr[0])
        NumofDep = int(FirstAr[1])
        Arg1.append(NumofDoc)
        Arg1.append(NumofDep)
        for c in range(0,NumofDep):
            ArgC = raw_input().split()
            Arg.append(ArgC)
        print(Handle(Arg, Arg1))
        N -=1
        Arg1 =[]
        Arg =[]

    pass