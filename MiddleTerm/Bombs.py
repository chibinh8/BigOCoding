__author__ = 'Binh Le'
from collections import deque

def IsDot(x,y,Graph,Dimen,Vis):
    if(x<0 or y<0 or x>=Dimen[0]or y>=Dimen[1]or Vis[x][y]==True):
        return []
    if(Graph[x][y]==0 or Graph[x][y]==3):
       Point = []
       Point.append(x)
       Point.append(y)
       return Point
    else:
       return []
def FindEleAround(x,y,Graph,Dimen,Vis):
    ListEle = []
    Point = []
    if(x>=Dimen[1]or y>=Dimen[0]or Graph[x][y]==1):
        return []
    Point = IsDot(x,y+1,Graph,Dimen,Vis)
    if(Point!=[]):
        ListEle.append(Point)
        Point=[]
    Point = IsDot(x+1,y,Graph,Dimen,Vis)
    if(Point!=[]):
        ListEle.append(Point)
        Point=[]
    Point = IsDot(x-1,y,Graph,Dimen,Vis)
    if(Point!=[]):
        ListEle.append(Point)
        Point=[]
    Point = IsDot(x,y-1,Graph,Dimen,Vis)
    if(Point!=[]):
        ListEle.append(Point)
        Point=[]
    return ListEle

def BFS(Arg,DimenIn,Source,Desti,Path,Visited):
   QueueRun  = deque()
   StartPoint = [-1,-1]
   StartPoint[0] = Source[0]
   StartPoint[1] = Source[1]
   QueueRun.append(StartPoint)
   Visited[StartPoint[0]][StartPoint[1]] = True
   while(len(QueueRun)>0):
        PopL = QueueRun.popleft()
        ParentNode = PopL
        ListC = FindEleAround(ParentNode[0],ParentNode[1],Arg,DimenIn,Visited)
        if(ListC!=[]):
            for Ele in ListC:
              if(Visited[Ele[0]][Ele[1]]==False):
                  Visited[Ele[0]][Ele[1]]=True
                  QueueRun.append(Ele)
                  Path[Ele[1]+Ele[0]*DimenIn[1]] = ParentNode[1]+ParentNode[0]*DimenIn[1]
              elif(Ele[0]==Desti[0] and Ele[1]==Desti[1]):
                  return Path
   return Path

def Handle(R,C,NumOfBomR,Source,Desti,Map, Path,Visited):
    cnt =0
    Map[int(Source[0])][int(Source[1])]=2
    Map[int(Desti[0])][int(Desti[1])]=3
    PathOut =  BFS(Map,[C,R],[int(Source[0]),int(Source[1])],[int(Desti[0]),int(Desti[1])],Path,Visited)
    Index = int(Desti[0])*R + int(Desti[1])
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
        InputS = input().split()
        R = int(InputS[0])
        C = int(InputS[1])
        if(R==0 and C ==0 ):
            break
        else:
            for cr in range(0,R):
                Map.append([])
                Visited.append([])
                for cl in range(0,C):
                    Map[cr].append(0)
                    Path.append(-1)
                    Visited[cr].append(False)
            NumOfBomR = int(input().split()[0])
            for c in range(0,NumOfBomR):
                ArgBom = (input().split())
                for cd, item in enumerate(ArgBom):
                    if(cd>=2):
                        Map[int(ArgBom[0])][int(cd)] = 1
            Source = input().split()
            Desti = input().split()
            print(Handle(R,C,NumOfBomR,Source,Desti,Map, Path,Visited))
        ArgBom = []

    pass