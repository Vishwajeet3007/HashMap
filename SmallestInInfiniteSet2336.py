class smallestInfiniteSet:
    def __init__(self):
        self.current = 1
        self.a_set = set()

    def popSmallest(self):
        if self.a_set:
            curr_min = min(self.a_set)
            self.a_set.remove(curr_min)
            return curr_min
        else:
            self.current += 1
            return self.current - 1
    def addBack(self,num):
        if self.current > num :
            self.a_set.add(num)
# Creating an instance of SmallestInfiniteSet
smallestInfiniteSet = smallestInfiniteSet()

# Popping the smallest element (should be 1)
print(smallestInfiniteSet.popSmallest())  # Output: 1

# Popping the smallest element again (should be 2)
print(smallestInfiniteSet.popSmallest())  # Output: 2

# Adding back 1 to the set
smallestInfiniteSet.addBack(1)

# Popping the smallest element (should be 1 again)
print(smallestInfiniteSet.popSmallest())  # Output: 1

# Popping the next smallest element (should be 3)
print(smallestInfiniteSet.popSmallest())  # Output: 3

# Adding back 2 to the set
smallestInfiniteSet.addBack(2)

# Popping the smallest element (should be 2)
print(smallestInfiniteSet.popSmallest())  # Output: 2
