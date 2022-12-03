from math import dist
import math
import DataReader
from random import shuffle, randint, random
from copy import deepcopy

#tworzy podana liczbe losowych populacji z danych wejsciowych
def randomPopulation(list_of_points, population_size):
    population = []
    for x in range(population_size):
        list_copy = deepcopy(list_of_points)
        shuffle(list_copy)
        population.append(list_copy)
    return(population)

#fitness to długość trasy
def calculatedFitness(number_of_points, chromosome, data):
    distance = dist(data[chromosome[0]],data[chromosome[number_of_points - 1]])
    for x in range(number_of_points - 1):
        distance += dist(data[chromosome[x]], data[chromosome[x+1]])
    return distance

#mutacja to zamiana dwoch losowo wybranych punktow w 1 chromosomie
def mutatedChromosome(number_of_points, chromosome):
    while True:
        position1 = randint(0,number_of_points-1)
        position2 = randint(0,number_of_points-1)
        if position1 != position2:
            tmp = chromosome[position1]
            chromosome[position1] = chromosome[position2]
            chromosome[position2] = tmp
            break
    return chromosome

#wybor turniejowy tworzenie turzniejow o losowej dlugosci, z kazdego wybrany zawodnik z najlepszym fitnessem
def setOfTournaments(population, population_size):
    populationcopy = deepcopy(population)
    #tworzenie turniejow
    tournaments = []
    while len(tournaments) < population_size:
        tournament_size = randint(1, len(populationcopy) - 1)
        tournament = []
        for x in range(tournament_size):
            rndIndex = randint(0, (len(populationcopy) - 1))
            tournament.append(populationcopy[rndIndex])
        tournaments.append(tournament)
    return tournaments

def tournamentsWinners(data ,number_of_points, set_of_tournaments):
    winners = []
    for tournament in set_of_tournaments:
        scores = {}
        player_id = 0
        for player in tournament:
            scores[player_id]= calculatedFitness(number_of_points,player, data)
            player_id += 1
            #{(indeks gracza w turnieju, wynik funkcji fitness )}
        sorted_scores = sorted(scores.items(), key=lambda x:x[1])
        winner = sorted_scores[0] #winner[0] to player_id wygranego winner[1] to wartosc fitnessu
        winners.append(tournament[winner[0]])
        #dodanie zwyciezcy( listy z odwiedzonymi punktami np.[1,3,4,5,2]) ktora wygrala turniej czyli miala najmniejszy fitness
    return winners   

#krzyzowanie elementow ktore zostaly wybrane turniejami
def crossOver(number_of_points, parent1, parent2):
    child = parent1[0:number_of_points//2]
    for point in parent2:
        if point not in child:
            child.append(point)
    return child

def newPopulation(number_of_points,data, best_solutions, tournament_winners):
    new_population = []
    for solution in best_solutions:
        mutated_sol = mutatedChromosome(number_of_points, solution)
        mutated_sol_fitness = calculatedFitness(number_of_points, mutated_sol,data)
        non_mutaded_fitness = calculatedFitness(number_of_points, solution,data)
        if(mutated_sol_fitness < non_mutaded_fitness):
            new_population.append([mutated_sol,mutated_sol_fitness])
        else:
            new_population.append([solution,non_mutaded_fitness])
    partly_new_population = []
    for winner in tournament_winners: # mozna potem dawac krok zeby nie krzyzowac wszystkich zwyciezcow tylko czesc np co drugi zwyciezca
        crossed_winner = crossOver(number_of_points,winner,tournament_winners[randint(0,len(tournament_winners)-1)])
        partly_new_population.append(crossed_winner) # dodajemy zkrossowanego winnera z jakims randomowym z winnerow tez
    for chromosome in partly_new_population:
        if (1==1): # z prawdopodobienstwem 100 % zmutuje i doda do populacji
            mutated_chromosome = mutatedChromosome(number_of_points,chromosome)
            new_population.append([mutated_chromosome, calculatedFitness(number_of_points,mutated_chromosome,data)])
        else:
            new_population.append([chromosome, calculatedFitness(number_of_points,chromosome,data)])
    sorted_new_population = sorted(new_population, key=lambda x:x[1])
    result = []
    for x in sorted_new_population:
        result.append(x[0])
    return result

# wstepna populacja bedzie paroma wynikami algorytmu zachlanmnego
