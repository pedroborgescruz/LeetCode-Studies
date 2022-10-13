"""
TWO SUM
-------
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
"""

def TwoSum_BruteForce(array, target):
    # O(nˆ2); not great, but works
    for i in range(len(array)):
        for j in range(1, len(array)):
            if (array[i] + array[j] == target):
                return [i, j]
            
"""
Optimal/Better solution to the problem. This function runs in O(n) time.
The big idea here is that we are constructing a hash table of complements
and indexes. We check if we can add any of the complements to our current 
value to add up to the target.
"""        
def TwoSum_OptimalSolution(array, target):

    compls = {}
    for i in range(len(array)):
        if ((target - array[i]) in compls):
            return [compls[target - array[i]], i]
        compls[array[i]] = i

def main():
    assert [0,1] == TwoSum_BruteForce([2,7,11,15], 9), "Wrong output"
    assert [0,1] == TwoSum_OptimalSolution([2,7,11,15], 9), "Wrong output"
    assert [2,3] == TwoSum_OptimalSolution([0,7,2,2], 4), "Wrong output"
    assert [1,2] == TwoSum_OptimalSolution([3,2,4], 6), "Wrong output"
    assert [0,1] == TwoSum_OptimalSolution([3,3], 6), "Wrong output"

main()
    