import networkx as nx

class CausalGraph:
    def __init__(self):
        self.graph = nx.DiGraph()  # Directed acyclic graph

    def add_transition(self, parent_state, transition):
        """
        Add a committed transition to the causal graph.

        Args:
            parent_state: The state before the transition.
            transition: The committed Transition object.
        """
        new_state = transition.apply(parent_state)
        self.graph.add_edge(parent_state, new_state, transition=transition)
        return new_state

    def validate(self):
        if not nx.is_directed_acyclic_graph(self.graph):
            raise ValueError("Causal graph no longer consistent (cycle detected)")