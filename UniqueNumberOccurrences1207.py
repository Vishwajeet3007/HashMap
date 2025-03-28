def isUniqueOccurence(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1 
    return len(set(freq.values())) == len(freq)
arr = [1,3,4,3,2,2,3,4,4,4]  
print(isUniqueOccurence(arr))