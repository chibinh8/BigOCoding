__author__ = 'Binh Le'
import sys

def BinarySearch(LMarble,lo,hi,Target):
    while lo <= hi:
              mid = int(lo + (hi-lo)/2)
              if ((LMarble[mid] == Target)):
                 return mid
              elif LMarble[mid] < Target:
                 lo = mid+1
              else:
                 hi = mid -1
    return -1
if __name__ == '__main__':
    LPri =[]
    cnt = 0
    NumTC = int(sys.stdin.readline().rstrip().split()[0])
    for tc in range(0,NumTC):
        cnt = 0
        N,PizaPrice = map(int,sys.stdin.readline().rstrip().split())
        N, PizaPrice = int(N),int(PizaPrice)
        LPri = [int(x) for x in map(int,sys.stdin.readline().rstrip().split())]
        LPri.sort()
        for id, c in enumerate(LPri):
            pos = BinarySearch(LPri,id+1 ,len(LPri)-1,PizaPrice-c)
            if(pos!=-1):
                cnt +=1
        print(cnt)
    pass