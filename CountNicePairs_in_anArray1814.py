from collections import defaultdict
def countNicePairs(nums):
    count = 0
    diff_count = defaultdict(int)
    mod = 10**9+7
    for num in nums:
        reverse_num = int(str(num)[::-1])
        diff = num - reverse_num
        count = ( count + diff_count[diff]) % mod
        diff_count[diff] += 1
    return count
nums = [42,11,1,97]
print(countNicePairs(nums))
nums = [13,10,35,24,76]
print(countNicePairs(nums))
nums = [1, 2, 3, 4, 5]
print(countNicePairs(nums))