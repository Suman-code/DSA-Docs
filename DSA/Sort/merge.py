

'''def merge(arr , l , m , r):
    n1 = m - l + 1
    n2 = r - m 
    
    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr[l+i]

    for j in range(0, n2):
        R[j] = arr[m+j]

    i = 0
    j=0
    k=0

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergesort(arr , l , r):
    if l < r:
        m = (l+(r-1))//2
        mergesort(arr , l , m)
        mergesort(arr , m+1 , r)
        merge(arr , l , m , r)
    return arr
        

clis = [2,5,1,6,10,23,4,9,7,6,12,18]
print(mergesort(clis, 0 ,12))
'''


def merge(lis, l , m , r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0 , n1):
        L[i] = lis[l+i]
            
    for j in range(0, n2):
        R[j] = lis[m+j]


    i = 0
    j = 0
    k = 0

    while i < n1 and j < n2:
        if L[i] < R[j]:
            




    



    

