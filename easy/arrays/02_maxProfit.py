from typing import List
from typing import List
'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''

def maxProfit(prices):
    max_profit = 0
 
    # Iterate through the prices
    for i in range(len(prices) - 1):
        # If the price increases, add the difference to the profit
        if prices[i + 1] > prices[i]:
            max_profit += prices[i + 1] - prices[i]

    # we should just be returning the max_profit
    return f"the max profit is: {max_profit}"
 
 
# Test case 1: General case with ups and downs
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: the max profit is: 7
 
# Test case 2: Prices always increasing
# prices = [1, 2, 3, 4, 5]
# print(max_profit(prices))  # Output: 4
 
# # Test case 3: Prices always decreasing
# prices = [5, 4, 3, 2, 1]
# print(max_profit(prices))  # Output: 0
 
# # Test case 4: Empty array
# prices = []
# print(max_profit(prices))  # Output: 0
 
# # Test case 5: Single day
# prices = [5]
# print(max_profit(prices))  # Output: 0
 