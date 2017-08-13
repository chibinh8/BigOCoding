__author__ = 'Binh Le'
import sys

def BinarySearch(LMarble,Target):
    lo =0
    hi = len(LMarble)-1
    pos=-1
    while lo <= hi:
          mid = int(lo + (hi-lo)/2)
          if LMarble[mid][0] == Target:
               pos = mid
               for cd in range(lo,mid):
                   if LMarble[cd][0] == Target:
                        return cd
               return pos
          elif LMarble[mid][0] < Target:
             lo = mid+1
          else:
             hi = mid-1
    return pos
if __name__ == '__main__':
    N=1
    Q =1
    LMarble = []
    LQuery = []
    numTC = 0
    while(N!=0 and Q!=0):
        N,Q = sys.stdin.readline().strip().split()
        N = int(N)
        Q = int(Q)
        if((N==0 and Q==0)):
            break
        LMarble = []
        LQuery = []
        for c in range(0,N):
            LMarble.append([int(sys.stdin.readline().strip().split()[0]),c])
        for c in range(0,Q):
            LQuery.append(int(sys.stdin.readline().strip().split()[0]))
        print("CASE# "+str(numTC+1)+":")
        LQuery.sort()
        for c in LQuery:
            pos = BinarySearch(LMarble,c)
            if(pos!=-1):
              print(str(c)+" found at "+str(pos+2))
            else:
              print(str(c)+" not found")

    pass