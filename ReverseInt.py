"""
REVERSE INT
-----------

Given an integer x, return x with its digits reversed. 
"""

def ReverseInt(x):
    rev = 0
    while (x != 0):
        pop = x % 10
        x //= 10
        rev = (rev * 10) + pop  
    
    return rev
    
def main():
    assert 321 == ReverseInt(123), "Wrong output"
    assert 123 == ReverseInt(321), "Wrong output"
    assert 1 == ReverseInt(1), "Wrong output"
    assert 23453 == ReverseInt(35432), "Wrong output"
    assert 21 == ReverseInt(120), "Wrong output"
    assert 1111 == ReverseInt(1111), "Wrong output"
    assert 0 == ReverseInt(0), "Wrong output"
    assert -321 == ReverseInt(-123), "Wrong output"

main()
    
