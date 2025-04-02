def numFactoredBT(arr):
    arr.sort()
    mp = {}
    mp[arr[0]] = 1

    for i in range(1,len(arr)):
        root = arr[i]
        mp[root] = 1
        for j in range(i):
            left_child = arr[j]
            if root % left_child == 0  and arr[i] // left_child in mp:
                mp[root] += mp[left_child] * mp[arr[i]//left_child]
    result = 0
  
    for num in mp:
        result = (result + mp[num])
    return result
arr = [2,4]
print(numFactoredBT(arr))
arr = [2,4,5,10]
print(numFactoredBT(arr))

