prices = [7, 1, 5, 3, 6, 4]

# Inefficient. 2 loops.
# maxprofit = 0
#
# for i in range(len(prices)-1):
#     for j in range(i+1,len(prices)):
#         if prices[j] - prices[i] > maxprofit:
#             maxprofit = prices[j] - prices[i]
# print(maxprofit)

# More efficient method
# def maxProfit(self, prices: List[int]) -> int:
#     maxprofit = 0
#
#     if len(prices) == 0:
#         return maxprofit
#
#     minprice = prices[0]
#     profit = []
#
#     for n in prices:
#         if n <= minprice:
#             minprice = n
#         else:
#             profit.append(n - minprice)
#             maxprofit = max(profit)
#     return maxprofit

# Cleaner solution:
def maxProfit(self, prices: List[int]) -> int:
    maxprofit = 0

    if len(prices) == 0:
        return maxprofit

    minprice = prices[0]

    for price in prices:
        minprice = min(price, minprice)
        maxprofit = max(price - minprice, maxprofit)
    return maxprofit