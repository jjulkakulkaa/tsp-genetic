import DataReader
import Genetic
import time
import sys
from copy import deepcopy
from math import dist
from mainGreedy import res_for_GA
sys.setrecursionlimit(10000)
from Genetic import randomPopulation, calculatedFitness, crossOver, mutatedChromosome, newPopulation, setOfTournaments, tournamentsWinners
STOP = 0
def solvingProblem(number_of_points,data,first_population,population_size,best_solutions_amount,iterations,list_of_points):
    tournaments = setOfTournaments(first_population,population_size)
    winners = tournamentsWinners(data,number_of_points,tournaments)
    newpopulation = newPopulation(number_of_points, data,winners,winners[0:best_solutions_amount], population_size, list_of_points)
    newpopulationcopy = deepcopy(newpopulation)
    if iterations <= 1000:
        solvingProblem(number_of_points,data, newpopulationcopy, population_size,best_solutions_amount,iterations+1,list_of_points)
    resutls = []
    for solution in newpopulationcopy:
        resutls.append([solution, calculatedFitness(number_of_points, solution, data)])
    sorted_results = sorted(resutls, key=lambda x:x[1])        
    return sorted_results[0]

size_of_population = 200
rand_first = randomPopulation(DataReader.list_of_points,size_of_population)
# rand_first.append(res_for_GA)
RES = solvingProblem(DataReader.number_of_points,DataReader.data, rand_first ,size_of_population,size_of_population//10,0,DataReader.list_of_points)
print(RES)
# print(dist([0,0],[0,3])+ dist([0,3],[0,6])+ dist([0,6],[4,6])+ dist([4,6],[4,4])+dist([4,4],[10,3])+ dist([10,3],[4,2])+ dist([4,2],[4,0])+ dist([4,0],[0,0]))
#trzeba zrobic wprowadzanie wynikow algorytmu zachlannego do pocztkowej populacji bo sa smieci "rand first"