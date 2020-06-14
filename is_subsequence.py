# s = "abc"
# t = "ahbgdc"

# def subSeq(i,s,t):
#     if s == t:
#         return True
#     if i == 0 :
#         return False
#     return ()

# Recursive Python program to check if a string is subsequence 
# of another string 

# Returns true if str1[] is a subsequence of str2[]. 
def isSubSequence(string1, string2,m,n): 
	# Base Cases 
	if m == 0: return True
	if n == 0: return False

	# If last characters of two strings are matching 
	if string1[m-1] == string2[n-1]: 
		return isSubSequence(string1, string2, m-1, n-1) 

	# If last characters are not matching 
	return isSubSequence(string1, string2, m, n-1) 

# Driver program to test the above function 
string1 = "gksrek"
string2 = "geeksforgeeks"

if isSubSequence(string1, string2,len(string1),len(string2)): 
	print("Yes")
else: 
	print("No")

def dp(s,t):
    m = 0 
    n = 0
    while m < len(s) and n < len(t):
        if s[m] == t[n]:
            m += 1
        n += 1
    return m == len(s)

    

print(dp("axc","ahbgdc"))
s = "abc"
t = "ahbgdc"
print(dp(s,t))

# This code is contributed by BHAVYA JAIN 
