from itertools import combinations, permutations

a, b, c = 'SEND', 'MORE', 'MONEY'

for comb in combinations(range(10), 8):
    for perm in permutations(comb):
        d = dict(zip('SENDMORY', perm))
        f = lambda x: sum(d[e] * 10**i for i, e in enumerate(x[::-1]))
        if f(a) + f(b) == f(c):
            print(f"{f(a)} +   {f(b)} = {f(c)} ")