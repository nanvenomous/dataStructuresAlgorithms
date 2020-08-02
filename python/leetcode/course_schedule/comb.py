from itertools import combinations

x = int(input())

to_mix = list(range(x))
ans = list(combinations(to_mix, 2))

print(len(ans))
