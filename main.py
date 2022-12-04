import Genetic
from DataReader import GetData
from SolvingProblem import solvingProblem
from Genetic import randomPopulation, calculatedFitness, crossOver, mutatedChromosome, newPopulation, setOfTournaments, tournamentsWinners
import time

filename = "berlin52.txt"

read_file = GetData(filename)
number_of_points = read_file[0]
list_of_points = list(read_file[1].keys())
data = read_file[1]

size_of_population = 200

first_population = randomPopulation(list_of_points,size_of_population)
time0 = time.time()
result = solvingProblem(number_of_points,data,first_population,size_of_population,size_of_population//10,0,list_of_points)
print(result, time.time()- time0)

