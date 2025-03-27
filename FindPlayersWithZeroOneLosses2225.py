def findWinner(matches):
    # first we find lost player with how many times lose
    lost_map = {}
    for winner , loser in matches:
        if loser in lost_map:
            lost_map[loser] += 1
        else:
            lost_map[loser] = 1
    
    never_lost = set()
    once_lost = []
    for i in range(len(matches)):
        winner = matches[i][0]
        loser = matches[i][1]

        if winner not in lost_map:
            never_lost.add(winner)
        if lost_map[loser] == 1:
            once_lost.append(loser)
    return [sorted(list(never_lost)) , sorted(once_lost)]
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(findWinner(matches))