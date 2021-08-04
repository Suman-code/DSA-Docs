cousLis = [2,6,5,8,10,1,3,4]
'''
def bubbleSort(givenList):
    size = len(givenList)
    for i in range(size-1):
        for j in range(size-1-i):
            if givenList[j] > givenList[j+1]:
                givenList[j] , givenList[j+1] = givenList[j+1] , givenList[j]
        
    print(cousLis)


#bubbleSort(cousLis)


#time complaxity is O(n2)

'''

def bubbleSort(lis):
    n = len(lis)
    for i in range(n-1):
        for j in range(n-i-1):
            if lis[j] > lis[j+1]:
                lis[j] , lis[j+1]  = lis[j+1] , lis[j]
            
    print(lis)

bubbleSort(cousLis)