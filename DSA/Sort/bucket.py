import math
'''
def insertion(lis):
    for i in range(1 , len(lis)):
        key = lis[i]
        j = i-1
        while j >= 0 and key < lis[j]:
            lis[j+1] = lis[j]
            j -= 1
        lis[j+1] = key

    return lis



def bucket(lis):
    numOfbucket = round(math.sqrt(len(lis)))
    maxNub = max(lis)
    arr = []

    for i in range(numOfbucket):
        arr.append([])
    for j in lis:
        index_b = math.ceil(j*numOfbucket/maxNub)
        arr[index_b-1].append(j)

    for i in range(numOfbucket):
        arr[i] = insertion(arr[i])

    k = 0
    for i in range(numOfbucket):
        for j in range(len(arr[i])):

            lis[k] = arr[i][j]
            k += 1
    return lis
            

clis = [5,3,6,8,9,10,12,15]

print(bucket(clis))
    '''


def insertionSort(li):
    n = len(li)
    
    for i in range(1 , n):
        key = li[i]
        j = i-1
        while  j >= 0 and li[j] > key:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = key

    return li


def bucket(lis):
    arr = []
    num_buck = round(math.sqrt(len(lis)))
    max_ele = max(lis)

    #create the bucket

    for i in range(num_buck):
        arr.append([])

# put arry element in diffrent buckets

    for j in lis:
        nub_ele = math.ceil(j*num_buck/max_ele)
        arr[nub_ele-1].append(j)

    
    # sort individual bucket
    for i in range(num_buck):
        arr[i] = insertionSort(arr[i])
    
    #concatinate the buckect
    k = 0
    for i in range(num_buck):
        for j in range(len(arr[i])):
            lis[k] = arr[i][j]
            k += 1
    return lis
    


        

    




lis = [5,9,1,5,6,7,91,0.2,12,15]
print(bucket(lis))