with open("data/9.txt") as file:
    dir = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1),
    }

    moves = []
    for line in file:
        d, p = line.rstrip().split()
        moves.append((d, int(p)))

    def follow(head, tail):
        x, y = head[0] - tail[0], head[1] - tail[1]
        abs_x = abs(x)
        abs_y = abs(y)
        if abs_x > 1 or abs_y > 1:
            return (
                tail[0] + (0 if x == 0 else x // abs_x),
                tail[1] + (0 if y == 0 else y // abs_y)
            )
        return tail

    def solve(knots): 
        ropes = [(0, 0) for _ in range(knots)]
        tail_visited = {ropes[-1]} 
        for move in moves:
            vec = dir[move[0]]
            for _ in range(move[1]):
                H = ropes[0]
                ropes[0] = H[0] + vec[0], H[1] + vec[1]
                for x in range(1, knots):
                    ropes[x] = follow(ropes[x-1], ropes[x])
                tail_visited.add(ropes[-1])
        return len(tail_visited)

    #* Part 1
    print(solve(knots=2))
    #* Part 2
    print(solve(knots=10))
    