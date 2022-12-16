import math
from decimal import Decimal
from numpy import Infinity, size 
# from DataReader import GetData
from copy import deepcopy
 
def TSP_greedy(data,choice,start_point,list_of_available_vertices):
    choice.append(start_point)
    list_of_available_vertices.remove(start_point)
    shortest = Infinity
    # distance = 0
    for v in list_of_available_vertices:
        distance = math.dist(data[start_point],data[v])
        if distance < shortest:
            shortest = distance
            next_point = v
    if len(list_of_available_vertices) == 0:
        return choice
    else:
        return TSP_greedy(data,choice,next_point,list_of_available_vertices)

def GreedyResults(number_of_points, data,finall_list,list_of_points):
    for x in range(1, number_of_points):
        list_of_available_vertices = deepcopy(list_of_points)
        part_of_sol = TSP_greedy(data,[],x,list_of_available_vertices)
        finall_list.append(part_of_sol)
    return finall_list

