import RandomData

def GetData(file_name):
    data = {}
    points = open(file_name, mode='r')
    number_of_points = int(points.readline())
    for line in points.readlines():
        l = line.split()
        data[int(l[0])] = list(map(int,l[1:]))
    return number_of_points, data

text = GetData("data0.txt")
number_of_points = text[0]
list_of_points = list(text[1].keys())
data = text[1]