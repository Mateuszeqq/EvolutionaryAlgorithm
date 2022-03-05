from XMLNetworkParser import XMLNetworkParser
from Services.LinkService import LinkService
from Services.PathService import PathService
from Services.DemandService import DemandService
from Services.EvolutionAlgorithmService import EvolutionAlgorithmService
from Modules.Population import Population
from matplotlib import pyplot as plt


def save_best_result(P):
    best_result = P.get_best()
    with open('result.txt', 'w') as f:
        for gen in best_result.gens:
            f.write(f'{gen.demand.id}: {gen.demand.source}-{gen.demand.target}, value:{gen.demand.value}\n')
            for vec in gen.vectors:
                f.write(f'      T: {vec.transponder} Path: {vec.path.id} Wavelength: {vec.wavelength}\n')


BANDWIDTH = 96

transponders_cost = {
                40: 1,
               100: 3,
               200: 5,
               400: 7
               }


mu = 100
lmbd = 200

max_iters = 41
m_chance = 0.05
c_chance = 0.2


link_serv = LinkService()
path_serv = PathService()
dem_serv = DemandService()

network = XMLNetworkParser('data/polska.xml')

nodes = network.nodes()
links = network.links()
demands = network.demands()
paths = network.paths()
transponders = [400, 200, 100, 40]
S = [wavelength for wavelength in range(BANDWIDTH)]


links = link_serv.create_links(links)
paths = path_serv.create_paths(paths, links)
demands = dem_serv.create_demands(demands, paths)

evol_alg_serv = EvolutionAlgorithmService(mu, lmbd, demands, transponders, S)

P = Population()

evol_alg_serv.initiate(P)

x_plot = []
best_plot = []
population_best_plot = []

evol_alg_serv.evaluate(P, transponders_cost)

i = 0
for epoch in range(max_iters):
    # New population of mu size (individuals selected from population P)
    O = evol_alg_serv.rand_choose(P)

    # C - We cross individuals from the O population with a certain probability c_chance. A new population of C is created
    C = evol_alg_serv.crossing(O, c_chance)

    # M - individuals from the O population with a certain probability m_chance. A new population of M is formed
    M = evol_alg_serv.mutation(C, m_chance, transponders, S)

    # Evaluation and succession
    evol_alg_serv.evaluate(M, transponders_cost)
    P = evol_alg_serv.succession(M, P)

    best_result = P.get_best()

    x_plot.append(epoch)
    best_plot.append(best_result.rating)
    population_best_plot.append(evol_alg_serv.get_population_score(P))

    if i % 10 == 0:
        print(f'ITERATION [{i}]')
        print(f'BEST --> {best_result.rating}')
        print(f'POPULATION_SCORE --> {evol_alg_serv.get_population_score(P)}')
    i += 1


plt.plot(x_plot, best_plot, color='r', label='POPULATION_BEST')
plt.plot(x_plot, population_best_plot, color='g', label='POPULATION_AVG')
plt.title(f"EA: p_m={m_chance}, p_c={c_chance}, mu={mu}, lambda={lmbd}")

plt.xlabel("iteration")
plt.ylabel("cost")

plt.legend()
plt.show()

save_best_result(P)

