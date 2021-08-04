li = [2,6,5,8,10,1,3,4]

'''def selectionSort(arr):
    size = len(arr)
    for i in range(size):
        min_indx = i
        for j in range(i+1 , size):
            if arr[min_indx] > arr[j]:
                min_indx = j

        arr[i] , arr[min_indx] = arr[min_indx] , arr[i]
    print(arr)
        

selectionSort(lis)'''
        



'''def selectionSort(lis):
    n = len(lis)
    for i in range(n):
        min = i
        for j in range(i+1 , n):
            if lis[min] > lis[j]:
                min = j

        lis[min] , lis[i]  = lis[i] , lis[min]
    
    print(lis)



selectionSort(li)'''

def selectionSort(lis):
    n = len(lis)
    for i in range(n):
        min = i
        for j in range(i+1 , n):

            if lis[min] > lis[j]:
                min = j

        lis[min] , lis[i] = lis[i] , lis[min]
    print(lis)
            
        
selectionSort(li)