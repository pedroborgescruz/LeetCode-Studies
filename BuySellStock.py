"""
BEST TIME TO BUY AND SELL STOCK
-------------------------------
You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.
"""

def BuySellStock(prices):
    """
    O(n) solution. 
    Intuition: we can scan the list and keep update the maxProfit as we find a
        currProfit greater than before. 
    """
    maxProfit = 0
    buy = prices[0]
    
    for i in range(1, len(prices)):
        currProfit = prices[i] - buy
        if (currProfit > maxProfit):
            maxProfit = currProfit
        buy = min(buy, prices[i])
        
    return maxProfit
    
def main():
    assert (5 == BuySellStock([7,1,5,3,6,4])), "Wrong output"
    assert (0 == BuySellStock([7,6,4,3,1])), "Wrong output"
    assert (3 == BuySellStock([0,0,0,1,3])), "Wrong output"
    assert (21 == BuySellStock([10,4,3,24,1])), "Wrong output"

main()