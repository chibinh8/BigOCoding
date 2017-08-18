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

    pass