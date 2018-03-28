doors = [0] * 100
step = 1
i = 0

while step <= 100:
    while i <100:
        if doors[i] == 0:
            doors[i] = 1
        else:
            doors[i] = 0
        i = i + step

    i = step
    step += 1

print(doors)