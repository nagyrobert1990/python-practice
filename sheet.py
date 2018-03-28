points = ["122","143", "264","273", "314", "435","446", "556"]

route_maxxx = 0

way = [[] for i in range(len(points))]
temp_way = ""   # DEL ME
counter = 0
while counter < len(points):
    route = "001"
    for i in range(len(points)):
        if route[2] in points[i][0]:
            temp_way += points[i]+" > "   # DEL ME
            route_maxxx += int(points[i][1])
            route = points[i]
    counter += 1
    temp_way += "\n"

#print(temp_way,route_maxxx)


def join_list(lst):
    return ','.join(lst)

def grades():
    b = {16,32,96}
    return len(b)

if __name__ == "__main__":
    print(grades())
