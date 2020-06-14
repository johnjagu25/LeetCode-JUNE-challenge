# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

def coinComb(arr,m,n):
    dp = [[0 for i in range(m)] for j in range(n+1)]
    for i in range(m):
        dp[0][i] = 1
    for i in range(1,n+1):
        for j in range(0,m):
            # excluding coin
            x =  dp[i][j-1] if j >= 0 else 0
            # including coin
            y =  dp[i-arr[j]][j] if i >= arr[j] else 0
            dp[i][j] = x + y
    return (dp[n][m-1])
arr = [1,2,3]
m = len(arr)    
print(coinComb(arr,m,4))