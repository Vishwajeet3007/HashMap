from collections import defaultdict
def canPairs(arr,k):
    remainder_freq = defaultdict(int)
    for num in arr:
        rem = num % k
        remainder_freq[rem] += 1
    for rem in remainder_freq:
        if rem == 0:
            if remainder_freq[rem] % 2 != 0:
                return False
            elif k - rem in remainder_freq:
                if remainder_freq[rem] != remainder_freq[k-rem]:
                    return False
            else:
                return False
    return True
arr = [9, 5, 7, 3]
k = 6
print(canPairs(arr,k))
arr = [4, 4]
k = 4
print(canPairs(arr,k))
arr= [4, 4, 4] 
k = 4
print(canPairs(arr,k))