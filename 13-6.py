slov = dict()
ans = list()
for i in input().split():
    if i in list(slov.keys()):
        slov[i] += 1
    else:
        slov[i] = 1
    ans.append(slov[i])
print(*ans)