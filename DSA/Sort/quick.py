def partition(lis, low, high):
    p  = lis[high]
    i = low - 1

    for j in range(low, high):
        if lis[j] <= p:
            i += 1

            lis[i] , lis[j] = lis[j] , lis[i]

    lis[i+1], lis[high] = lis[high] , lis[i+1]
    return (i+1)


def quickSort(lis , low, high):
    if low < high:
        pi = partition(lis , low, high)
        
        quickSort (lis , low , pi - 1)
        quickSort(lis , pi+1 , high)
    


clis = [2,1,7,6,5,3,4,9,8]
quickSort(clis , 0 , 8)
print(clis)