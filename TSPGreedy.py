import math
from decimal import Decimal
from numpy import Infinity, size
import RandomData   

def list_of_available_vertices(data):
    available = []
    for x in range(data[0][0]):
        available.append(x)
    return available

def TSP_greedy(points,choice,start_point,available_vertices,final_distance):
    choice.append(start_point+1)
    available_vertices.remove(start_point)
    shortest = Infinity
    distance = 0
    for v in available_vertices:
        distance = math.dist(points[start_point],points[v])
        if distance < shortest:
            shortest = distance
            next_point = v
    if distance != 0:
        final_distance += shortest
    if len(choice) == len(points):
        final_distance = final_distance + math.dist(points[start_point],points[0])
        choice.append(1)
        return choice, final_distance
    else:
        return TSP_greedy(points,choice,next_point,available_vertices,final_distance)

    