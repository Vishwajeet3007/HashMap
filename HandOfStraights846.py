from collections import Counter
def isNStraightsHand(hand,groupSize):
    if len(hand) % groupSize != 0:
        return False
    count = Counter(hand)
    for num in sorted(count):
        freq = count[num]
        if freq > 0:
            for i in range(groupSize):
                next_num = num + i
                if count[next_num] < freq:
                    return False
                count[next_num] -= freq
    return True
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(isNStraightsHand(hand,groupSize))
hand = [1,2,3,4,5]
groupSize = 4
print(isNStraightsHand(hand,groupSize))