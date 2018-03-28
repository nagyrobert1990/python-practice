doors = [0] * 100

for j in range(0,len(doors)):
    for i in range(j,len(doors),j+1):
        if doors[i] == 1:
            doors[i] = 0
        else:
            doors[i] = 1
print (doors)