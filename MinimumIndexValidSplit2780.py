from collections import Counter
def minimumIndex(nums):
    # # Using Brute Force
    # n = len(nums)
    # for i in range(n-1):
    #     left = nums[:i+1]
    #     right = nums[i+1:]

    #     left_count = Counter(left)
    #     right_count = Counter(right)
    #     for num in left_count:
    #         if left_count[num] > len(left) // 2 and right_count[num] > len(right) // 2:
    #             return i
    # return -1

    # T.C = O(n) S.C = O(1)
    n = len(nums)
    candidate , count = None , 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    total = nums.count(candidate)
    if total <= n // 2:
        return -1
    prefix = 0
    for i in range(n-1):
        if nums[i] == candidate:
            prefix += 1
        if prefix > ( i + 1) // 2 and (total - prefix) > (n - i - 1) // 2:
            return i
    return -1
nums = [1,2,2,2]
print(minimumIndex(nums))
nums = [2,1,3,1,1,1,7,1,2,1]
print(minimumIndex(nums))
nums = [3,3,3,3,7,2,2]
print(minimumIndex(nums))