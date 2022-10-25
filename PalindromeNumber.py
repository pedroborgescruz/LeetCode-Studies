"""
PALINDROME NUMBER
-----------------

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
"""

def isPalindrome(x: int) -> bool:
    # This solution converts the number to a string in order to check
    # if it is palindrome or not. O(log n) solution.
    x_string = str(x)
    left_to_count = len(x_string)
    low_i = 0
    high_i = len(x_string) - 1

    while (left_to_count > 1):
        if x_string[low_i] != x_string[high_i-low_i]:
            return False
        low_i += 1
        left_to_count -= 2

    return True

def isPalindrome_2(x: int) -> bool:
    # Creates a new number in reverse and compare it with
    # the input number. This solution runs in O(len(x)) (?) --> check
    if x < 0:
        return False
    
    revNum = 0
    inputNum = x
    while (inputNum != 0):
        pop = inputNum % 10
        inputNum //= 10
        revNum = (revNum * 10) + pop
    
    return (revNum == x)
    
def main():
    assert (True == isPalindrome(121)), "Wrong output"
    assert (False == isPalindrome(234)), "Wrong output"
    assert (False == isPalindrome(-121)), "Wrong output"
    assert (True == isPalindrome(1001)), "Wrong output"
    assert (True == isPalindrome_2(121)), "Wrong output"
    assert (False == isPalindrome_2(234)), "Wrong output"
    assert (False == isPalindrome_2(-121)), "Wrong output"
    assert (True == isPalindrome_2(1001)), "Wrong output"
    
main()