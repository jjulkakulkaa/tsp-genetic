import RandomData

def GetData(file_name):
    data = {}
    points = open(file_name, mode='r')
    number_of_points = int(points.readline())
    for line in points.readlines():
        l = line.split()
        data[int(l[0])] = list(map(int,l[1:]))
    return number_of_points, data

dupa = GetData("data0.txt")
example_list_of_points = list(dupa[1].keys())
example_data = dupa[1]