from math import dist
import DataReader
from random import shuffle
from copy import deepcopy

def random_population(list_of_points, population_size):
    population = []
    for x in range(population_size):
        list_copy = deepcopy(list_of_points)
        shuffle(list_copy)
        population.append(list_copy)
    return(population)

def calculated_fitness(number_of_points, chromosome, data):
    distance = dist(data[chromosome[0]],data[chromosome[number_of_points - 1]])
    for x in range(number_of_points - 1):
        distance += dist(data[chromosome[x]], data[chromosome[x+1]])
    return distance
res = calculated_fitness(5,[1,2,3,4,5],{1: [943, 15], 2: [1593, 627], 3: [736, 439], 4: [939, 1852], 5: [1623, 408]})
print(res)