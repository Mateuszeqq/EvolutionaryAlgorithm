import random
import copy
from Modules.Population import Population
from Services.ChromosomeService import ChromosomeService
from Modules.Chromosome import Chromosome
from Services.GenService import GenService


class EvolutionAlgorithmService:
    def __init__(self, mu, lmbd, demands, transponders, wavelengths):
        self.mu = mu
        self.lmbd = lmbd
        self.demands = demands
        self.transponders = transponders
        self.wavelengths = wavelengths

    def initiate(self, population):
        chromo_serv = ChromosomeService()
        for i in range(self.mu):
            demands = copy.deepcopy(self.demands)
            chromosome = chromo_serv.create_chromosome(demands, self.transponders, self.wavelengths)
            population.add_chromo(chromosome)

    def clear_wavelengths(self, gen):
        for vector in gen.vectors:
            wl = vector.wavelength
            path = vector.path
            for link in path.links:
                link.wavelen_used.remove(wl)

    def mutation(self, population, m_chance, transpoders, wavelengths):
        # Each gene is mutated with the probability m_chance
        new_population = Population()
        gen_service = GenService()
        for chromosome in population:
            new_chromosome = Chromosome()
            for gen in chromosome.gens:
                demand = gen.demand
                if random.uniform(0, 1) < m_chance:
                    # Create new gene and replace the old one
                    self.clear_wavelengths(gen)
                    new_gen = gen_service.create_gen(demand, transpoders, wavelengths)
                else:
                    new_gen = gen
                new_chromosome.gens.append(new_gen)
            new_population.add_chromo(new_chromosome)
        return new_population

    def crossing(self, population, c_chance):
        new_population = Population()
        # Create new chromosome -> selection of random genes from previously defined pair of chromosomes
        for i in range(self.lmbd):
            pair = random.sample(population.chromosomes, 2)
            chromosome_1, chromosome_2 = copy.deepcopy(pair[0]), copy.deepcopy(pair[1])
            new_chromosome = Chromosome()
            for gen_1, gen_2 in zip(chromosome_1.gens, chromosome_2.gens):
                if random.uniform(0, 1) < c_chance:
                    # Gene from first chromosome
                    gen = copy.deepcopy(gen_1)
                else:
                    # Gene from second chromosome
                    gen = copy.deepcopy(gen_2)
                new_chromosome.add_gen(gen)
            # Add newly created chromosome to a population
            new_population.add_chromo(new_chromosome)
        return new_population

    def evaluate(self, population, transponders_cost):
        for chromosome in population.chromosomes:
            rating = 0
            for gen in chromosome.gens:
                for vector in gen.vectors:
                    rating += transponders_cost[vector.transponder]
            chromosome.rating = rating

    def rand_choose(self, population):
        new_population = Population()
        for i in range(self.lmbd):
            chosen_index = random.randint(0, self.mu-1)
            chromosome = population[chosen_index]
            new_population.add_chromo(chromosome)
        return new_population

    def succession(self, first_population, second_population):
        all_chromos = first_population + second_population
        all_chromos = sorted(all_chromos, key=lambda chromosome: chromosome.rating)

        return Population(all_chromos[:self.mu])

    def get_population_score(self, population):
        score = 0
        for chromosome in population:
            score += chromosome.rating
        return score / len(population.chromosomes)
