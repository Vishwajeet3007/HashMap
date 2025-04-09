from collections import Counter
def canArrange(arr,k):
    rem_count = Counter([((num % k) + k) % k for num in arr])
    for r in rem_count:
        if r == 0:
            if rem_count[r] % 2 != 0:
                return False
        elif 2 * r == k:
            if rem_count[r] % 2 != 0:
                return False
        else:
            if rem_count[r] != rem_count[k-r]:
                return False
    return True
arr = [1,2,3,4,5,10,6,7,8,9]
k = 5
print(canArrange(arr,k))
arr = [1,2,3,4,5,6]
k = 10
print(canArrange(arr,k))
