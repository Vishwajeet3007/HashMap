def goodPairs(nums):
    n = len(nums)

    # using Brute Force
    count = 0
    # for i in range(n-1):
    #     for j in range(i+1,n):
    #         if nums[i] == nums[j]:
    #             count += 1

    # using hash map
    mp = {}
    for num in nums:
        if num in mp:
            count += mp[num]
            mp[num] += 1
        else:
            mp[num] = 1
    return count
nums = [1,2,3,1,1,3]
print(goodPairs(nums))

nums = [1,1,1,1]
print(goodPairs(nums))

nums = [1,2,3]
print(goodPairs(nums))
