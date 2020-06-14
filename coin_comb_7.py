# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

def coinComb(arr,m,n):
    dp = [0] * (n+1)
    dp[0] = 1
    for coin in arr:
        for x in range(coin,n+1):
            dp[x] += dp[x-coin]
    return dp[n]
arr = [1,2,3]
m = len(arr)    
print(coinComb(arr,m,4))