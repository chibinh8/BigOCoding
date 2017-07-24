__author__ = 'USER'

from collections import deque

#Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1610


def Handle(Arg, Arg1):
   StackRun  = []
   Path = []
   Visited = []
   Graph = []
   N = Arg1[1]
   for c in range(0,Arg1[0]):
       Path.append(-1)
       Visited.append(False)
       Graph.append([])
   for c in range(0,N):
        Graph[int(Arg[c][0])-1].append(int(Arg[c][1]))
   for cd in range(1,Arg1[0]+1) :
       if(Graph[cd-1]!=[]):
           StackRun.append(cd)
           ParentNode = cd
           Visited[ParentNode-1]=True
           while(len(StackRun)>0):
                PopL = StackRun.pop()
                ParentNode = int(PopL)
                ListC = list(Graph[int(ParentNode)-1])
                for Ele in ListC:
                  if(Visited[int(Ele)-1]==False):
                      StackRun.append(Ele)
                      Visited[int(Ele)-1]=True
                  else:
                      return "SIM"
           StackRun = []
           for c in range(0,Arg1[0]):
               Visited[c] = False
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