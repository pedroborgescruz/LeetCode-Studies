from heapq import merge
from turtle import right


def mergeSort(array):
    if (len(array) > 1):
        # partition
        left_arr = array[:len(array)//2]
        right_arr = array[len(array)//2:]
        
        mergeSort(left_arr)
        mergeSort(right_arr)
        
        # merge
        i = 0 # left_arr pointer
        j = 0 # right_arr pointer
        k = 0 # array pointer
        
        while (i < len(left_arr) and j < len(right_arr)):
            if left_arr[i] < right_arr[j]:
                array[k] = left_arr[i]
                i += 1
            else:
                array[k] = right_arr[j]
                j += 1
            k += 1
            
        while (i < len(left_arr)):
            array[k] = left_arr[i]
            i += 1
            k += 1
            
        while (j < len(right_arr)):
            array[k] = right_arr[j]
            j += 1
            k += 1
        
array = [2,3,2,1,2,3,4,2,4,456,2345,2442,13,5,4,32,3,45,34]
print(array)
mergeSort(array)
print(array)