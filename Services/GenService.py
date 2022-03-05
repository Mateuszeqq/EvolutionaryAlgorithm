from Modules.Gen import Gen
from Services.VectorService import VectorService


class GenService:
    def __init__(self):
        self.s = 0
        pass

    def create_gen(self, demand, transpoders, wavelengths):
        self.s += 1
        gen = Gen(demand)
        vect_service = VectorService()
        while gen.demand_met < demand.value:
            vector = vect_service.create_vector(transpoders, demand.admiss_paths, wavelengths)
            gen.add_vector(vector)

        return gen
