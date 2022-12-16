first_population = randomPopulation(list_of_points,size_of_population)
result = solvingProblem(number_of_points,data,first_population,size_of_population,size_of_population//100,time_limit,list_of_points,time.time())
print(result)