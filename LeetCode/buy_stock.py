def buy(prices)->int:
    # min_price = 0 # lowest price
    maxProfit = 0 # max profit
    buyDate = 0 #
    for i in range(len(prices)):
        currentProfit = prices[i] - prices[buyDate]

        maxProfit = max(currentProfit, maxProfit) # update the max profit

        if prices[i] < prices[buyDate]: # when today's price is smaller than the price of a previous day
            buyDate = i # update to the lastest lowest price's day

    return maxProfit

list1 = [10,5,3,7,23,45,7] # 42
print(f"Max Profit {buy(list1)}")


list2 = [10, 7, 7, 20, 8, 15, 20, 21, 23, 11] # 16
print(f"Max Profit {buy(list2)}")


print(f"Max Profit {buy([10,5,4,2])}") # 0

print(f'Max Profit: {buy([10,4,5,1,7,1])}') # 6

print(f'Max Profit: {buy([2,1,4])}') # 3