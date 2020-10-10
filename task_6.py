from itertools import count, cycle

y = []
for i in count(3):
    y.append(i)
    num = 0
    if i == 10:
        break

for j in cycle(y):
    if num == 2*len(y):
        break
    print(j)
    num += 1


# print(y)


