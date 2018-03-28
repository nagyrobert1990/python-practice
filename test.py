A = 0
B = 0
a = [5,6,7]
b = [3,6,10]
for i in range(0,len(a)):
    if a[i] > b[i]:
        A += 1
        print("hozzáad Ahoz",A)
    elif b[i] > a[i]:
        B += 1
        print("hozzáad Bhez",B)