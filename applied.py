
# To represent the graph and traverse the modules invoking the build() method, you can use a 
# class-based approach for the modules and a graph data structure to capture the dependencies.

# The Module class represents a module in the system with a build() method and a set of dependencies.
class Module:
    def __init__(self, name):
        self.name = name
        self.dependencies = set()
    
    def add_dependency(self, module):
        self.dependencies.add(module)

    def build(self):
        print(f"Building module {self.name}")

# The ModuleGraph class represents the graph and provides methods to add modules, add dependencies,
# and traverse the graph to build the modules.
class ModuleGraph:
    def __init__(self):
        self.modules = {}

    def add_module(self, module):
        self.modules[module.name] = module

    def add_dependency(self, module_name, dependency_name):
        self.modules[module_name].add_dependency(self.modules[dependency_name])

# The traverse_and_build method uses depth-first search (DFS) to traverse the 
# modules in the correct order based on dependencies and invokes the build() method for each module.
    def traverse_and_build(self):
        visited = set()

        def dfs(module):
            if module.name not in visited:
                visited.add(module.name)
                for dependency in module.dependencies:
                    dfs(dependency)
                module.build()

        for module in self.modules.values():
            dfs(module)

# main method
def main():
    # Example usage:
    module_a = Module("A")
    module_b = Module("B")
    module_c = Module("C")
    module_d = Module("D")
    module_e = Module("E")
    module_f = Module("F")
    module_g = Module("G")

    graph = ModuleGraph()

    graph.add_module(module_a)
    graph.add_module(module_b)
    graph.add_module(module_c)
    graph.add_module(module_d)
    graph.add_module(module_e)
    graph.add_module(module_f)
    graph.add_module(module_g)

    graph.add_dependency("A", "B")
    graph.add_dependency("A", "C")
    graph.add_dependency("B", "D")
    graph.add_dependency("C", "D")
    graph.add_dependency("C", "E")
    graph.add_dependency("F", "E")
    graph.add_dependency("F", "G")

    graph.traverse_and_build()

    # The output for this:
    # Building module D
    # Building module B
    # Building module E
    # Building module C
    # Building module A
    # Building module G
    # Building module F

if __name__ == "__main__":
    main()


