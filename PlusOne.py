"""
PLUS ONE
========
You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most
significant to least significant in left-to-right order. The large integer does
not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution(object):
    def plusOne(self, digits):
        if digits[len(digits)-1] < 9:
            # if the last digit is less than 9, we can just increment it 
            digits[len(digits)-1] += 1
        else:
            # if we enter here, that means we will have overflow happening and
            # we need to assess it
            for i in range(len(digits)):
                # go through the entire array starting from the LSB and check 
                # where the overflow can be corrected
                if (digits[len(digits)-1-i] != 9):
                    # if any element in different from 9, we can increment it
                    # by one unit safely without further overflow; do it
                    digits[len(digits)-1-i] += 1
                    return digits
                else:
                    # if the element is equal to 9, that means we cannot 
                    # increment it safely yet but this will have to be a 0;
                    # update it
                    digits[len(digits)-1-i] = 0
                    
            if digits[0] == 0:
                # if, after going through the loop, all elements were equal to
                # 9, this means our sum is equal to some base 10 number and 
                # we need to insert the number 1 in the array as the MSB; do it
                digits.insert(0,1)
                    
        return digits

        
        