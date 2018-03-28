numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

print(numbers)
n = len(numbers)
for i in range(n):
    for j in range(1, n-i):
        if numbers[j-1] > numbers[j]:
            (numbers[j-1], numbers[j]) = (numbers[j], numbers[j-1])

print ("Max:", (numbers[n-1]))