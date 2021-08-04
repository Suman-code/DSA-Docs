li = [5,8,2,4,9,11,3,1]

def insertionSort(lis):
    n = len(lis)
    for i in range(1 , n):
        key = lis[i]
        j = i-1
        while  j >= 0 and lis[j] > key:
            lis[j+1] = lis[j]
            j -= 1
        lis[j+1] = key

    print(lis)

insertionSort(li)
