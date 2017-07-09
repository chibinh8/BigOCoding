import Queue
def Handle(Listso, ListSo1):
   ListStack = []
   #Que = Queue.Queue()
   MinTemp = 1
   LenList = len(ListSo1)-1
   popele = 0
   if(Listso[0]==0 or len(ListSo1)==0):
       return "no"
   for Index in range(0,LenList+1):
      if(int(ListSo1[Index])>MinTemp):
          if(len(ListStack)!=0):
            popele = ListStack.pop()
            if(int(popele)==MinTemp):
              #Que.put(popele)
              pass
            else:
              ListStack.append(int(popele))
              ListStack.append(int(ListSo1[Index]))
          else:
              ListStack.append(int(ListSo1[Index]))
      else:
          if(len(ListStack)!=0):
            popele = ListStack.pop()
            if(popele==MinTemp):
              #Que.put(popele)
              pass
            else:
              ListStack.append(popele)
          else:
            if(popele!=0):
             ListStack.append(popele)
            #Que.put(ListSo1[LenList-Index])
          MinTemp = MinTemp +1
   if(len(ListStack)!=0):
       popele = ListStack.pop()
       while((len(ListStack)!=0)):
          if(popele==MinTemp):
             # Que.put(popele)
              popele = ListStack.pop()
              MinTemp = MinTemp+1
          else:
              return "no"
   return "yes"


if __name__ == '__main__':
    Listso = raw_input().split()
    Listso1 = raw_input().split()
    print(Handle(Listso,Listso1))
    pass