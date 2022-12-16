from DataReader import GetData
from SolvingProblem import solvingProblem
from Genetic import randomPopulation, calculatedFitness, crossOver, mutatedChromosome, newPopulation, setOfTournaments, tournamentsWinners
import time
import TSPGreedy

filename = "berlin52.txt"

read_file = GetData(filename)
number_of_points = read_file[0]
list_of_points = list(read_file[1].keys())
data = read_file[1]

size_of_population = 2000
time_limit = 20


greedy_results = TSPGreedy.GreedyResults(number_of_points,data, [],list_of_points)

first_population = randomPopulation(list_of_points,size_of_population - len(greedy_results)) + greedy_results
result = solvingProblem(number_of_points,data,first_population,size_of_population,size_of_population//100,time_limit,list_of_points,time.time())
print(result)

