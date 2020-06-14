# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

def sortColors(arr):
    l = c = 0
    r = len(arr) - 1
    while c<=r:
        if arr[c] == 0 :
            arr[l],arr[c] = arr[c],arr[l]
            c += 1
            l += 1
        elif arr[c] == 2 :
            arr[r],arr[c] = arr[c],arr[r]
            r -= 1
        else:
            c += 1
    return arr
print(sortColors([2,0,2,1,1,0]))