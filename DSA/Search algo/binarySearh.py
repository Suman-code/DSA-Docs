#creating a binary search
import math

def binarySearch(lis , value):

    start = 0
    end = len(lis) - 1
    mid = math.floor((start+end)/2)

    while not(lis[mid] == value) and start <= end:
        if value < lis[mid]:
            end = mid-1
        else:
            start = mid+1
        mid = math.floor((start+end)/2)

    if lis[mid] == value:

        return lis[mid]
        
    else:
        return -1
        



li  = [5,6,8,10,15,16,17,18,20,25,26,27,28,30]

print(binarySearch(li , 20))