import random
def random_points(how_many_points):
    points = [[int(how_many_points)]]
    while(len(points)<=how_many_points):
        point = [random.randint(0,2000),random.randint(0,2000)]
        if point not in points:
            points.append(point)
    return points

def gen_points_in_file(how_many_files, how_many_points):
    for x in range(how_many_files):
        file_name = "data"+str(x)+".txt"
        points = random_points(how_many_points)
        data = open(file_name, mode = 'w')
        point_index = 1

        for point in points:
            strpoint = (' '.join( str(a) for a in point))
            data.write(str(point_index)+' ')
            data.write(strpoint)
            data.write('\n')

            point_index +=1
        data.close()

#gen_points_in_file(1,100)

