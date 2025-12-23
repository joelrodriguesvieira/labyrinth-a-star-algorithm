import math
import random
import matplotlib.pyplot as plt

class SimulatedAnnealing:
    def __init__(self, cities, initial_temp=1000, cooling_rate=0.995, stopping_temp=1e-8, max_iter=100000):
        self.cities = cities
        self.num = len(cities)
        self.temperature = initial_temp
        self.cooling_rate = cooling_rate
        self.stopping_temp = stopping_temp
        self.max_iter = max_iter

        self.current_solution = list(range(self.num))
        random.shuffle(self.current_solution)
        self.best_solution = list(self.current_solution)
        self.current_cost = self.calc_cost(self.current_solution)
        self.best_cost = self.current_cost
        self.history = [self.best_cost]

    def calc_cost(self, solution):
        cost = 0
        for i in range(self.num):
            a = solution[i]
            b = solution[(i + 1) % self.num]
            cost += self.cities[a][b]
        return cost

    def swap(self, route):
        i, j = random.sample(range(self.num), 2)
        route[i], route[j] = route[j], route[i]

    def run(self):
        iteration = 0
        while self.temperature > self.stopping_temp and iteration < self.max_iter:
            new_solution = list(self.current_solution)
            self.swap(new_solution)
            new_cost = self.calc_cost(new_solution)

            delta = new_cost - self.current_cost

            if delta < 0 or random.random() < math.exp(-delta / self.temperature):
                self.current_solution = new_solution
                self.current_cost = new_cost

                if new_cost < self.best_cost:
                    self.best_solution = list(new_solution)
                    self.best_cost = new_cost

            self.temperature *= self.cooling_rate
            self.history.append(self.best_cost)
            iteration += 1

            if iteration % 1000 == 0:
                print(f"Iteração {iteration}, Melhor custo: {self.best_cost:.2f}, Temp: {self.temperature:.5f}")

        return self.best_solution, self.best_cost, self.history


# Reaproveitando seu carregamento:
cities = load_tsp_from_string(tsp_data)

sa = SimulatedAnnealing(cities, initial_temp=1000, cooling_rate=0.995, stopping_temp=1e-8, max_iter=100000)
best_solution, best_cost, history = sa.run()

print(f"Melhor rota encontrada tem custo {best_cost:.2f}")

# Visualizar evolução
plt.plot(history)
plt.xlabel("Iteração")
plt.ylabel("Custo da melhor rota")
plt.title("Evolução do custo com Simulated Annealing")
plt.grid()
plt.show()
