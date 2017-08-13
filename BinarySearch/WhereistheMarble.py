__author__ = 'Binh Le'
import sys

def BinarySearch(LMarble,lo,hi,Target):
    if lo <= hi:
          mid = int(lo + (hi-lo)/2)
          if ((mid==0 and LMarble[mid] == Target) or(LMarble[mid] == Target and LMarble[mid-1]<LMarble[mid])):
             return mid
          elif LMarble[mid] < Target:
             return BinarySearch(LMarble,mid+1,hi,Target)
          else:
             return BinarySearch(LMarble,lo,mid-1,Target)
    return -1
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
            LMarble.append(int(sys.stdin.readline().strip().split()[0]))
        for c in range(0,Q):
            LQuery.append(int(sys.stdin.readline().strip().split()[0]))
        numTC +=1
        print("CASE# "+str(numTC)+":")
        LMarble.sort()
        for c in LQuery:
            lo =0
            hi = len(LMarble)-1
            pos = BinarySearch(LMarble,lo,hi,c)
            if(pos!=-1):
              print(str(c)+" found at "+str(pos+1))
            else:
              print(str(c)+" not found")

    pass