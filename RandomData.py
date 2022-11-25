import random
def random_points(amount_of_points):
    points = []
    while(len(points)<=amount_of_points):
        point = [random.randint(0,2000),random.randint(0,2000)]
        if point not in points:
            points.append(point)
    return points

def gen_points_in_file(number_of_files, number_of_points):
    for x in range(number_of_files):
        file_name = "data"+str(x)+".txt"
        points = random_points(number_of_points)
        data = open(file_name, mode = 'w')
        point_index = 1

        data.write(str(number_of_points)+'\n')
        for point in points:
            strpoint = (' '.join( str(a) for a in point))
            data.write(str(point_index)+' ')
            data.write(strpoint)
            data.write('\n')
            point_index +=1
        data.close()

#gen_points_in_file(1,100)

