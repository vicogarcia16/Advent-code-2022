with open("data/7.txt") as file:
    folders = {}
    paths = [] 
    lines = file.readlines()
    for line in lines:
        commands = line.rstrip().split()
        if commands[0] == "$":
            if commands[1] == "ls":
                continue
            elif commands[1] == "cd":
                if commands[2] == "..":
                    paths = paths[:-1]
                elif commands[2] == "/":
                    paths = ["/"]
                else:
                    paths.append(commands[2])
        else:
            if commands[0] != "dir":
                current_path = ""
               
                for folder in paths:
                    if folder != "/" and current_path != "/":
                        current_path += "/"
                
                    current_path += folder
                    folders[current_path] = folders.get(current_path, 0) + int(commands[0])


def part1():
    total = 0
    for item in folders.items():
        if item[1] < 100000:
            total += item[1]
    return total


def part2():
    space_needed = 30000000 - (70000000 - folders.get("/"))
    min_space_to_delete = float("inf")
    for item in folders.items():
        if item[1] >= space_needed:
            min_space_to_delete = min(min_space_to_delete, item[1])
    return min_space_to_delete


#* Part 1
print(part1())
#* Part 2
print(part2())