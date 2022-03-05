class Chromosome:
    def __init__(self):
        self.gens = []
        self.rating = 0
        self.size = 0

    def add_gen(self, gen):
        self.gens.append(gen)
        self.size += 1

    def wavelengths_occupacy(self):
        links = []
        for gen in self.gens:
            for vec in gen.vectors:
                for link in vec.path.links:
                    links.append(link)
        links = list(set(links))
        return links


