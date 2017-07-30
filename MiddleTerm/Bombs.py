__author__ = 'Binh Le'

from sys import stdin, stdout
from collections import deque
import datetime
import time;
def IsDot(x,y,Graph,Dimen,Vis):
    Ind = x*Dimen[1]+y
    if(x<0 or y<0 or x>=Dimen[0]or y>=Dimen[1]or Vis[Ind]==True):
        return []
    if(Graph[Ind]==0 or Graph[Ind]==3):
       Point = []
       Point.append(x)
       Point.append(y)
       return Point
    else:
       return []

def BFS(Arg,DimenIn,Source,Desti,Path,Visited):
   QueueRun  = deque()
   LCo = [[0,1],[1,0],[-1,0],[0,-1]]
   StartPoint = [-1,-1]
   StartPoint[0] = Source[0]
   StartPoint[1] = Source[1]
   QueueRun.append(StartPoint)
   Visited[StartPoint[0]*DimenIn[1]+StartPoint[1]] = True
   Dlocaltime = time.time()
   while(len(QueueRun)>0):
        PopL = QueueRun.popleft()
        ParentNode = PopL
        for ind in range(0,4):
            Ele = IsDot(LCo[ind][0]+ParentNode[0],LCo[ind][1]+ParentNode[1],Arg,DimenIn,Visited)
            if(Ele!=[]):
                Ind = Ele[0]*DimenIn[1]+Ele[1]
                if(Visited[Ind]==False):
                    Visited[Ind]=True
                    QueueRun.append(Ele)
                    Path[Ind] = ParentNode[1]+ParentNode[0]*DimenIn[1]
   Dlocaltime1 = time.time()
   print(Dlocaltime1-Dlocaltime)
   return Path

def Handle(R,C,NumOfBomR,Source,Desti,Map, Path,Visited):
    cnt =0
    Map[int(Source[0])*C+int(Source[1])]=2
    Map[int(Desti[0])*C+int(Desti[1])]=3
    PathOut =  BFS(Map,[R,C],[int(Source[0]),int(Source[1])],[int(Desti[0]),int(Desti[1])],Path,Visited)
    Index = int(Desti[0])*C + int(Desti[1])
    while(PathOut[Index]!=-1):
        Index = PathOut[Index]
        cnt +=1
    return cnt
if __name__ == '__main__':
    ArgBom = []
    Visited = []
    Path = []
    Map = []
    while(1):
        R,C = stdin.readline().split()
        R = int(R)
        C = int(C)
        if(R==0 and C ==0 ):
            break
        else:
            Num = R*C
            Map = [0] *Num
            Visited = [False] *Num
            Path = [-1] *Num
            Clocaltime = time.time()
            NumOfBomR = int(stdin.readline().split()[0])
            for c in range(0,NumOfBomR):
                ArgBom = stdin.readline().split()
                for cd, item in enumerate(ArgBom):
                    if(cd>=2):
                        Map[int(ArgBom[0])*C+int(item)] = 1
            Source = stdin.readline().split()
            Desti = stdin.readline().split()
            print(Handle(R,C,NumOfBomR,Source,Desti,Map, Path,Visited))
        ArgBom = []

    pass