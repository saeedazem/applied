task:
- a graph represents modules of a system
- each module has the build() ability
- the arrows represents dependencies(e.g. A is dependent on B and C,  B is dependent on D, C is dependent on D and E, F is dependent on E and G, D and E and G had no dependent)
- create a data structure to receive this graph as input
- write python code that traverse the modules and invokes the method build() in each