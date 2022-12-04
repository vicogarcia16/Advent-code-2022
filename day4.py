part1 = 0
part2 = 0
#* Input Data
with open("data/4.in") as file:
    for line in file:
        cords = line.rstrip().split(",")
        x1, y1 = list(map(int, cords[0].split("-")))
        x2, y2 = list(map(int, cords[1].split("-")))
        if (x1 <= x2 and y2 <= y1) or \
                (x2 <= x1 and y1 <= y2):
            part1 += 1

        if (x2 <= y1 and y2 >= x1) or \
                (x1 <= y2 and y1 >= x2):
            part2 += 1
#* Part 1
print(part1)
#* Part 2
print(part2)