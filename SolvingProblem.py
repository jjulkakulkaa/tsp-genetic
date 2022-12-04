import DataReader
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
    if iterations <= 100:
        solvingProblem(number_of_points,data, newpopulationcopy, population_size,best_solutions_amount,iterations+1,list_of_points)
    resutls = []
    for solution in newpopulationcopy:
        resutls.append([solution, calculatedFitness(number_of_points, solution, data)])
    sorted_results = sorted(resutls, key=lambda x:x[1])        
    return sorted_results[0]

