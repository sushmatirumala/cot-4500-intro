import numpy as np
a = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

for i in range(0,3):
    for j in range(0,3):
        if i == j:
            a[i][j] = 1

print(str(a).replace(' [', '').replace('[', '').replace(']', ''), "\n" )

for i in range(0,3):
    for j in range(0,3):
        if i != j:
            a[i][j] += 3

print(str(a).replace(' [', '').replace('[', '').replace(']', ''), "\n" )

a = np.delete(a, 2, 1)

print(str(a).replace(' [', '').replace('[', '').replace(']', ''),)
