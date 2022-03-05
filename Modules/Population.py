class Population:

    def __init__(self, chromosomes=None):
        if chromosomes is None:
            chromosomes = []
        self.chromosomes = chromosomes
        self.size = len(chromosomes)

    def add_chromo(self, chromo):
        self.chromosomes.append(chromo)
        self.size += 1

    def get_best(self):
        best = None
        for chromosome in self.chromosomes:
            if best is None or chromosome.rating <= best.rating:
                best = chromosome

        return best

    def __getitem__(self, i): return self.chromosomes[i]

    def __add__(self, other): return Population(self.chromosomes+other.chromosomes)

