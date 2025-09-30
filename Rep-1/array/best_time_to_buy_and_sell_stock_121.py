prices = [7,2,1,5,6,4,8]

prices = [8,5,4,3,2,1]


buy = prices[0]
profit = 0
for val in prices:
    if val < buy:
        buy = val
    elif val - buy > profit:
        profit = val - buy

print(profit)