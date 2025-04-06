from collections import Counter
def minimumNumberOfPushes(word):
    # Using Brute Force
    # n = len(word)
    # presses = 0
    # for i in range(n):
    #     presses += (i // 8) + 1
    # return presses 

    # Using Hash Map
    freq = Counter(word)
    sorted_freq = sorted(freq.values(),reverse=True)
    presses = 0
    for i , count in enumerate(sorted_freq):
        presses += count * (i // 8 + 1)
    return presses

word = 'abcde'
print(minimumNumberOfPushes(word))
word = "xycdefghij"
print(minimumNumberOfPushes(word))
