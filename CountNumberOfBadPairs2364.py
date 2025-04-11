def countBadPairs(nums):
    # Using brute force
    # result = 0
    # for  i in range(len(nums)-1):
    #     for j in range(i+1,len(nums)):
    #         if (j-i) != nums[j] - nums[i]:
    #             result += 1
    # return result

    # Using HashMap
    result = 0
    mp = {}
    for i in range(len(nums)):
        diff = nums[i] - i
        goodPairs = mp.get(diff,0)
        totalPairsInPast = i
        result += totalPairsInPast - goodPairs
        mp[diff] = goodPairs + 1
    return result
nums = [4,1,3,3]
print(countBadPairs(nums))
nums = [1,2,3,4,5]
print(countBadPairs(nums))
nums = [6,2,3,4,5]
print(countBadPairs(nums))