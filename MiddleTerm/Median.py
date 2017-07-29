__author__ = 'Binh Le'

if __name__ == '__main__':
    InputS =[]
    InputI = []
    N = int(raw_input().split()[0])
    if(N!=0):
        InputS = raw_input().split()
        for c in InputS:
            InputI.append(int(c))
        InputI.sort()
        print(InputI[(N-1)/2])
    pass