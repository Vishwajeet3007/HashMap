from typing import List
def queryResults(limit,queries):
    ball_to_color = {}
    color_count = {}
    result = []
    for ball , color in queries:
        if ball in ball_to_color:
            old_color = ball_to_color[ball]
            if old_color == color:
                result.append(len(color_count))
                continue
            color_count[old_color] -= 1
            if color_count[old_color] == 0:
                del color_count[old_color]
        ball_to_color[ball] = color
        color_count[color]  = color_count.get(color,0) + 1
        result.append(len(color_count))
    return result
limit = 4
queries = [[1,4],[2,5],[1,3],[3,4]]
print(queryResults(limit,queries))
limit = 4
queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
print(queryResults(limit,queries))

