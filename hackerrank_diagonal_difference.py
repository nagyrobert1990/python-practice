import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

a_1 = 0
a_2 = 0
for i in range(n):
    a_1 += a[i][i]
    a_2 += a[i][n-1-i]
print(abs(a_1 - a_2))