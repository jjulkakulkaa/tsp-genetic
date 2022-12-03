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
def solvingProblem(number_of_points,data,first_population,population_size,best_solutions_amount,iterations):
    tournaments = setOfTournaments(first_population,population_size)
    winners = tournamentsWinners(data,number_of_points,tournaments)
    newpopulation = newPopulation(number_of_points, data,winners[0:best_solutions_amount],winners[0:(population_size-best_solutions_amount)])
    d_new = deepcopy(newpopulation)
    if iterations <= 5:
        solvingProblem(number_of_points,data, d_new, population_size,best_solutions_amount,iterations+1)
    return [d_new[0], calculatedFitness(number_of_points,d_new[0],data)]

size_of_population = 250
rand_first = randomPopulation(DataReader.list_of_points,size_of_population)
rand_first.append(res_for_GA)
RES = solvingProblem(DataReader.number_of_points,DataReader.data, rand_first ,size_of_population,size_of_population//10,0)
print(RES)
print(dist([0,0],[0,3])+ dist([0,3],[0,6])+ dist([0,6],[4,6])+ dist([4,6],[4,4])+dist([4,4],[10,3])+ dist([10,3],[4,2])+ dist([4,2],[4,0])+ dist([4,0],[0,0]))
#trzeba zrobic wprowadzanie wynikow algorytmu zachlannego do pocztkowej populacji bo sa smieci "rand first"