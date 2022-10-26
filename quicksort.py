"""
QUICKSORT ALGORITHM
===================
Pedro Cruz
"""

def quickSort(A, lo, hi):
    # Recurse until we run out of elements in our sub-arrays
    if (lo < hi):
        # Partition sub-array and return the place where pivot was inserted
        pivotIndex = partition(A, lo, hi)
        # Recurse on "small" region
        quickSort(A, lo, pivotIndex-1)
        # Recurse on "large" region
        quickSort(A, pivotIndex+1, hi)
        
# Function to find the partition position
def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]
    # Pointer for greater element
    i = low
      
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
  
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            i = i + 1
  
    # Swap the pivot element with 
    # the greater element specified by i
    (array[i], array[high]) = (array[high], array[i])
  
    # Return the position from where partition is done
    return i
  
    
a = [3,2,1,4,100,100000,39594,2]
quickSort(a, 0, len(a)-1)
print(a)
