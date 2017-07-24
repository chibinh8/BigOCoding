__author__ = 'USER'

from collections import deque

#Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1610


def Handle(Arg, Arg1):
   StackRun  = []
   Path = []
   Visited = []
   Graph = []
   N = Arg1[1]
   DepenCnt = 0
   PrevDepenCnt =0
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
           while(len(StackRun)>0):
                PopL = StackRun.pop()
                ParentNode = int(PopL)
                #print(ParentNode)
                ListC = list(Graph[int(ParentNode)-1])
                if(Visited[ParentNode-1]==True):
                    Indicate = False
                    for dc in ListC:
                        if(Visited[dc-1]==False):
                          Indicate = True
                    if(Indicate==False):
                      DepenCnt = PrevDepenCnt
                      if(DepenCnt>1):
                          print(DepenCnt)
                          return "SIM"
                else:
                    if(ListC!=[]):
                        DepenCnt +=1
                        PrevDepenCnt = DepenCnt
                        Visited[ParentNode-1]=True
                    else:
                        DepenCnt = PrevDepenCnt
                        if(DepenCnt>1):
                               print(DepenCnt)
                               return "SIM"
                for Ele in ListC:
                  if(Visited[int(Ele)-1]==False):
                      StackRun.append(Ele)

       if(DepenCnt>1):
           print(DepenCnt)
           return "SIM"
       DepenCnt = 0
       StackRun = []
       PrevDepenCnt =0
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