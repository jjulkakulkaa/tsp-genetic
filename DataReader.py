import RandomData

def GetData(file_name):
    data = []
    points = open(file_name, mode='r')
    for x in points.readlines():
        point = x.split()
        for y in point:
            y = int(y)
        print(point)

GetData("berlin52.txt")