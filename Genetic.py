from math import dist
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

example_population = randomPopulation(DataReader.example_list_of_points,4)
#print(example_population)


#fitness to długość trasy
def calculatedFitness(number_of_points, chromosome, data):
    distance = dist(data[chromosome[0]],data[chromosome[number_of_points - 1]])
    for x in range(number_of_points - 1):
        distance += dist(data[chromosome[x]], data[chromosome[x+1]])
    return distance
ex_fitness = calculatedFitness(10,example_population[2],DataReader.example_data)
#print(ex_fitness)

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

ex_mutation = mutatedChromosome(10,example_population[3])
#print(ex_mutation)

#wybor turniejowy tworzenie turzniejow o losowej dlugosci, z kazdego wybrany zawodnik z najlepszym fitnessem
def setOfTournaments(population):
    populationcopy = deepcopy(population)
    #tworzenie turniejow
    tournaments = []
    while len(populationcopy) > 0:
        tournament_size = randint(1,len(populationcopy))
        tournament = []
        for x in range(tournament_size):
            rndIndex = randint(0,(len(populationcopy)-1))
            tournament.append(populationcopy[rndIndex])
            del populationcopy[rndIndex]
        tournaments.append(tournament)
    return tournaments

ex_tournaments = setOfTournaments(example_population)
#print(ex_tournaments)

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
ex_winners = tournamentsWinners(DataReader.example_data, 10, ex_tournaments)
print(ex_winners)        
