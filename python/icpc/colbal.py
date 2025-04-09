def count_collisions(n, m, red_balls, blue_balls):
    collisions = 0
    red_balls.sort(key=lambda x: x[0])
    blue_balls.sort(key=lambda x: x[1])

    i, j = 0, 0
    while i < n and j < m:
        xi, ui = red_balls[i]
        yi, vi = blue_balls[j]
        
        if xi / vi == yi / ui:
            collisions += 1
            i += 1
            j += 1
        elif xi / vi < yi / ui:
            i += 1
        else:
            j += 1

    return collisions
    #take bulk input 
n, m = map(int, input().split())
red_balls = [list(map(int, input().split())) for _ in range(n)]
blue_balls = [list(map(int, input().split())) for _ in range(m)]
print(count_collisions(n, m, red_balls, blue_balls))
