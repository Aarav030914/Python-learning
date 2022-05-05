tup = ('A', 'A', 'B', 'B', 'A', 'C', 'C')
d = {}
for i in range(len(tup)):
    d[tup[i]] = []
for j in range(len(tup)):
    d[tup[j]].append(j)
print(d)

