# TASK
The task is to optimize the cost of the optical network (minimize the cost of the transponders used) for the network of 12 Polish cities. The network is represented by a graph, the nodes and edges of which are described in the data attached to the task.

# DATA
There is a set of predefined paths between each city in the dataset. The data also include the requirements assigned between the two cities. There are 66 demands to be met.  There are available transponders with a capacity of 40, 100, 200 and 400G. Their cost is as follows: 1, 3, 5, 7. Each of the transponders is assigned a separate path connecting both cities and one wavelength which it uses and which is unique on the edge scale. In this case, we will consider the case where an optical fiber can accommodate 96 wavelengths.

# MODEL CONSTRAINTS
* We have to take into account that the adopted set of transponders ensures demand *d* between cities.
* It should also be ensured that the wavelength unit *(λ)* is unique within one edge.

# RUN THE SCRIPT
To run the script type: *python EvolutionaryAlgorithm.py*. You can also change parameters in this file.