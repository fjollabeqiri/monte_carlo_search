import copy
import random


def calculate_bin_weight(solution):
    itemWeight = {
        1: 15,
        2: 10,
        3: 12,
        4: 3,
        5: 10
    }
    bins = [0, 0]
    for i in range(0, 5):
        bins[solution[i]] = bins[solution[i]] + itemWeight[i + 1]
    return bins


def isFeasible(solution):
    isFeasibleSolution = 0
    if len(solution) != 5:
        isFeasibleSolution = 1
    bins = calculate_bin_weight(solution)
    for binWeight in bins:
        if binWeight > 50:
            isFeasibleSolution = 1
            break
    return isFeasibleSolution


def mutate(solution):
    isFeasibleS = 1
    while isFeasibleS == 1:
        new_solution = solution.copy()
        randGene = random.randint(0, (len(solution) - 1))
        new_solution[randGene] = int(not (new_solution[randGene]))
        isFeasibleS = isFeasible(new_solution)
    return new_solution


def fitness(solution, bin_capacity, k):
    bin_weights = calculate_bin_weight(solution)
    fscore = 0
    for i in range(0, 2):
        fscore = pow((bin_weights[i] / int(bin_capacity)), k)/2
    return fscore


if __name__ == "__main__":
    max_iterations = 10

    initial_solution = [1, 0, 1, 0, 1]
    bin_capacity = 50
    k = 1
    probability = 0.5

    fitness_score = fitness(initial_solution, bin_capacity, k)
    print("Initial solution:")
    print(initial_solution)
    print("Initial solution fitness score: " + str(fitness_score) + "\n\n")

    last_solution_fitness = fitness_score
    last_solution = initial_solution
    best_solution = initial_solution
    best_solution_fitness = fitness_score

    # mutation and neighbour selection based on Monte-Carlo Search algorithm
    for i in range(0, max_iterations):
        print("-------------------------------------------")
        current_solution = mutate(last_solution)
        current_fitness = fitness(current_solution, bin_capacity, k)
        print("Solution " + str(i+1) + ": " + str(current_solution))
        print("Fitness score: " + str(current_fitness))
        if current_fitness >= last_solution_fitness:
            last_solution = current_solution
            last_solution_fitness = current_fitness
            best_solution = last_solution
            best_solution_fitness = last_solution_fitness
        else:
            rand = random.randint(0, 100)
            if rand <= probability * 100:
                last_solution = current_solution
                last_solution_fitness = current_fitness

        print("\nLast solution:\n" + str(last_solution))

        print("Fitness score: " + str(last_solution_fitness))
        print("-------------------------------------------")

        print("\nBest solution:\n" + str(best_solution))

        print("Best solution score:\n " + str(best_solution_fitness))
        print("-------------------------------------------")