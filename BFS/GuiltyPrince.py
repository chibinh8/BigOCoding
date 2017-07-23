__author__ = 'Binh Le'

from collections import deque

#Link: http://lightoj.com/volume_showproblem.php?problem=1012
#Note: The evaluate engine of Lightoj does not support Python :(
def IsDot(x,y,Graph,Dimen,Vis):
    if(x<0 or y<0 or x>=Dimen[1]or y>=Dimen[0]or Vis[x][y]==True):
        return []
    if(Graph[x][y]=="."):
       Point = []
       Point.append(x)
       Point.append(y)
       return Point
    else:
       return []
def FindEleAround(x,y,Graph,Dimen,Vis):
    ListEle = []
    Point = []
    if(x>=Dimen[1]or y>=Dimen[0]or Graph[x][y]=="#"):
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


def BFS(Arg,DimenIn):
   QueueRun  = deque()
   StartPoint = [-1,-1]
   Visited = [[False for x in range(DimenIn[0])] for y in range(DimenIn[1])]
   for c in range(0,DimenIn[1]):
       for d in range(0,DimenIn[0]):
           if(Arg[c][d]=="@"):
             StartPoint[0] = c
             StartPoint[1] = d
   QueueRun.append(StartPoint)
   Visited[StartPoint[0]][StartPoint[1]] = True
   Cnt = 1
   while(len(QueueRun)>0):
        PopL = QueueRun.popleft()
        ParentNode = PopL
        ListC = FindEleAround(ParentNode[0],ParentNode[1],Arg,DimenIn,Visited)
        if(ListC!=[]):
            for Ele in ListC:
              if(Visited[Ele[0]][Ele[1]]==False):
                  Visited[Ele[0]][Ele[1]]=True
                  QueueRun.append(Ele)
                  Cnt +=1
   return Cnt

if __name__ == '__main__':
    Arg = []
    N = int(raw_input().split()[0])
    while(int(N)>0):
        DimenS = raw_input().split()
        DimenIn = []
        DimenIn.append(int(DimenS[0]))
        DimenIn.append(int(DimenS[1]))
        for row in range(0,int(DimenIn[1])):
            ArgC = raw_input().split()
            Arg.extend(ArgC)
        print(BFS(Arg,DimenIn))
        Arg=[]
        DimenIn=[]
        N -=1
    pass