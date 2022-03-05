class Gen:
    def __init__(self, demand):
        self.demand = demand
        self.vectors = []
        self.size = 0
        self.demand_met = 0

    def add_vector(self, vector):
        self.vectors.append(vector)
        self.size += 1
        self.demand_met += vector.transponder


