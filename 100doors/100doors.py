doors = [0] * 100
x = 0


for j in range(0,len(doors)):
    for i in range(x,len(doors),x+1):
        if doors[i] == 1:
            doors[i] = 0
        else:
            doors[i] = 1
    x = x+1
print (doors)