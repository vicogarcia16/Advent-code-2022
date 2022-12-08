def get_unique_window(ln):
    with open("data/6.txt") as file:
        inp = file.readline().rstrip()
        window = {}

        l, r = 0, 0

        while r < len(inp):
            window[inp[r]] = window.setdefault(inp[r], 0) + 1
            while (window[inp[r]] > 1):
                window[inp[l]] -= 1
                l += 1
            if r - l + 1 == ln:
                return r + 1

            r += 1

#* Part 1
print(get_unique_window(4))
#* Part 2 
print(get_unique_window(14))