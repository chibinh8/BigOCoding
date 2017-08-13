__author__ = 'Binh Le'
import sys

def BinarySearch(LMarble,lo,hi,Target,Lpos):
    if lo <= hi:
              mid = int(lo + (hi-lo)/2)
              if ((LMarble[mid] == Target)):
                 return mid
              elif LMarble[mid] < Target:
                 return BinarySearch(LMarble,mid+1,hi,Target,Lpos)
              else:
                 return BinarySearch(LMarble,lo,mid-1,Target,Lpos)
    return -1
if __name__ == '__main__':
    LPri =[]
    cnt = 0
    Lpos = []
    NumTC = int(sys.stdin.readline().strip().split()[0])
    for tc in range(0,NumTC):
        cnt = 0
        N,PizaPrice = sys.stdin.readline().strip().split()
        N, PizaPrice = int(N),int(PizaPrice)
        LPri = [int(x) for x in sys.stdin.readline().strip().split()]
        LPri.sort()
        for id, c in enumerate(LPri):
                pos = BinarySearch(LPri,0,len(LPri)-1,PizaPrice-c,Lpos)
                if(pos!=-1 and Lpos.count(pos)!=0):
                    cnt +=1
                    Lpos.append(pos)

        print(cnt)
    pass