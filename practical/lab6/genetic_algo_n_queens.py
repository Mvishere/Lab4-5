import random

# Configuration
N = 8                # Number of queens (size of the board)
POPULATION_SIZE = 100
MUTATION_RATE = 0.05
MAX_GENERATIONS = 1000

def generate_individual():
    """Generates a random chromosome (board configuration)."""
    return [random.randint(0, N - 1) for _ in range(N)]

def fitness(individual):
    """Counts the number of non-attacking pairs."""
    non_attacking = 0
    for i in range(N):
        for j in range(i + 1, N):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                non_attacking += 1
    return non_attacking

def selection(population, scores):
    """Selects two individuals using roulette wheel selection."""
    total_fitness = sum(scores)
    probs = [score / total_fitness for score in scores]
    parents = random.choices(population, weights=probs, k=2)
    return parents

def crossover(parent1, parent2):
    """Performs single-point crossover."""
    point = random.randint(1, N - 2)
    child = parent1[:point] + parent2[point:]
    return child

def mutate(individual):
    """Randomly mutate an individual with a given mutation rate."""
    if random.random() < MUTATION_RATE:
        i = random.randint(0, N - 1)
        individual[i] = random.randint(0, N - 1)
    return individual

def genetic_algorithm():
    population = [generate_individual() for _ in range(POPULATION_SIZE)]
    generation = 0

    while generation < MAX_GENERATIONS:
        scores = [fitness(ind) for ind in population]

        if max(scores) == (N * (N - 1)) // 2:
            solution = population[scores.index(max(scores))]
            print(f"Solution found in generation {generation}:")
            return solution

        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1, parent2 = selection(population, scores)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population
        generation += 1

    print("No solution found.")
    return None

if __name__ == "__main__":
    board = genetic_algorithm()
    print(board)