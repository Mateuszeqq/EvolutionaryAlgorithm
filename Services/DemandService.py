from Modules.Demand import Demand


class DemandService:
    def __init__(self):
        pass

    def create_demand(self, id, cities, value, paths):
        return Demand(id, cities[0], cities[1], value, paths)

    def create_demands(self, xml_demands, paths):
        return [self.create_demand(demand[0], demand[1], demand[2], paths[i]) for i, demand in enumerate(xml_demands)]
