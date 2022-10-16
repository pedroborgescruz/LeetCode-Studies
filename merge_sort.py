# INTUITION: We want to divide and conquer. Divide the array until we have 
# one-element arrays and then, from the bottom up, rearrange array by comparing
# sorted smaller arrays

def mergeSort(arr):
    # we only want to divide if there is more than one element
    if len(arr) > 1:
        # partitioning array into two pieces
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        # recurse through arrays
        mergeSort(left_arr)
        mergeSort(right_arr)
        
        # merge step
        i = 0 # left_arr index
        j = 0 # right_arr index
        k = 0 # merged_arr index
        
        # compare elements from left_arr and right_arr until finished with all 
        # elements OR either one of the indexes is larger than array length
        while (i < len(left_arr) and j < len(right_arr)):
            if (left_arr[i] < right_arr[j]):
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        # if more elements in left_arr than right_arr, we can just put all of 
        # the remaining values in the merged array since they are already sorted
        while (i < len(left_arr)):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        # if more elements in right_arr than left_arr, we can just put all of 
        # the remaining values in the merged array since they are already sorted    
        while (j < len(right_arr)):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    
# Test Case
arr = [9,1,2,5,3,7,0,8,4,6,10]    
print(arr)
mergeSort(arr)
print(arr)