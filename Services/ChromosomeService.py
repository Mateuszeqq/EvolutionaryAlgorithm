from Services.GenService import GenService
from Modules.Chromosome import Chromosome


class ChromosomeService:
    def __init__(self):
        pass

    def create_chromosome(self, demands, transponders, wavelengths):
        gen_serv = GenService()
        chromosome = Chromosome()
        for demand in demands:
            chromosome.add_gen(gen_serv.create_gen(demand, transponders, wavelengths))

        return chromosome
