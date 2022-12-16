import TSPGreedy
import time
import sys
sys.setrecursionlimit(10**6)

# def GetTxtData(file_name):
#     data = []
#     points_in_file = open(file_name, mode='r')
#     data.append(list(map(int,points_in_file.readline().split())))
#     for x in points_in_file.readlines():
#         point = list(map(int, x.split()))
#         data.append(point[1:])
#     return data

def SolvingProblem(data):
    solution = TSPGreedy.TSP_greedy(data[1:],[],0,TSPGreedy.list_of_available_vertices(data),0)
    return solution

def ChceckingTime(data):
    t0 = time.time()
    solution = SolvingProblem(data)
    print(solution)
    t1 = time.time() - t0
    print(t1)


