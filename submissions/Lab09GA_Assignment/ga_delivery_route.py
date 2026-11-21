import random

# Distance matrix between locations A-G
locations = ["A", "B", "C", "D", "E", "F", "G"]

distance_matrix = [
    [0, 4, 8, 6, 7, 9, 5],
    [4, 0, 5, 7, 3, 8, 6],
    [8, 5, 0, 4, 6, 3, 7],
    [6, 7, 4, 0, 5, 6, 8],
    [7, 3, 6, 5, 0, 4, 6],
    [9, 8, 3, 6, 4, 0, 5],
    [5, 6, 7, 8, 6, 5, 0]
]

# GA configuration
POPULATION_SIZE = 100
GENERATIONS = 200
ELITE_SIZE = 2
MUTATION_RATE = 0.2
SEED = 42

random.seed(SEED)


# Calculate total route distance
def calculate_distance(route):
    complete_route = ["A"] + route + ["A"]
    total = 0

    for i in range(len(complete_route) - 1):
        from_index = locations.index(complete_route[i])
        to_index = locations.index(complete_route[i + 1])

        total += distance_matrix[from_index][to_index]

    return total


# Generate initial population
def create_population():
    population = []

    for _ in range(POPULATION_SIZE):
        route = random.sample(locations[1:], 6)
        population.append(route)

    return population


# Tournament selection
def selection(population):
    candidates = random.sample(population, 3)
    return min(candidates, key=calculate_distance)


# Order crossover (OX)
def crossover(parent1, parent2):
    size = len(parent1)

    start, end = sorted(random.sample(range(size), 2))

    child = [None] * size

    # Copy a section from parent 1
    child[start:end + 1] = parent1[start:end + 1]

    # Fill remaining positions using parent 2
    remaining = [city for city in parent2 if city not in child]

    index = 0

    for i in range(size):
        if child[i] is None:
            child[i] = remaining[index]
            index += 1

    return child


# Swap mutation
def mutation(route):
    route = route.copy()

    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(route)), 2)

        route[i], route[j] = route[j], route[i]

    return route


# Main genetic algorithm
def genetic_algorithm():

    population = create_population()

    for generation in range(GENERATIONS):

        # Sort routes by total distance
        population.sort(key=calculate_distance)

        # Preserve the best routes
        new_population = [
            route.copy()
            for route in population[:ELITE_SIZE]
        ]

        # Generate the remaining population
        while len(new_population) < POPULATION_SIZE:

            parent1 = selection(population)
            parent2 = selection(population)

            child = crossover(parent1, parent2)

            child = mutation(child)

            new_population.append(child)

        population = new_population

    # Find the best route
    best_route = min(population, key=calculate_distance)
    best_distance = calculate_distance(best_route)

    return best_route, best_distance


# Execute the algorithm
if __name__ == "__main__":

    best_route, best_distance = genetic_algorithm()

    complete_route = ["A"] + best_route + ["A"]

    print("GENETIC ALGORITHM - DELIVERY ROUTE OPTIMISATION")
    print("-----------------------------------------------")
    print("Best Route:", " -> ".join(complete_route))
    print("Total Distance:", best_distance, "km")