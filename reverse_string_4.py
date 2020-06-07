class Solution:
    def reverseString(self,s):
        n = len(s)
        for i in range(n//2):
            temp = s[i]
            s[i] = s[n-i-1]
            s[n-i-1] = temp
        return s

print(Solution().reverseString(["H","a","n","n","a","h"]))
# Output: ["h","a","n","n","a","H"]