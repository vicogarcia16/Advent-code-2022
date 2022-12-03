#Input data

with open('data/1.in', 'r') as f:
    lines = f.readlines()

#* Part 1
max_calories = 0
for c in lines:
    if c != '\n':
        max_calories = max(max_calories, int(c))

print(max_calories)


#* Part 2
one, two, three = 0, 0, 0
cur_results = 0
max_calories = 0
for el in lines:
    if el != '\n':
        cur_results += int(el)
    else:
        if cur_results > three:
            if cur_results < two:
                three = cur_results
            elif cur_results < one:
                two, three = cur_results, two
            else:
                one, two, three = cur_results, one, two
        cur_results = 0

print(sum([one, two, three]))