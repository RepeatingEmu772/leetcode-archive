def maxProfit(prices):
    max_profit = 0
    
    #edge case, only 1 day or 2 day prices given 

    left = 0
    right = 1

    while right < len(prices):
        current_profit = prices[right]-prices[left]
        print(f"left: {left}, right: {right}")
        if prices[left] < prices[right]:
            max_profit = max_profit if max_profit > current_profit else current_profit
        else:
            left = right
        right += 1
    return max_profit

def maxProfit_n2(prices):
    profit = 0
    
    for i in range(len(prices)):
        for j in range(len(prices)):
            if profit < prices[j] - prices [i] and i < j:
                profit = prices [j] - prices[i]

    return profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))