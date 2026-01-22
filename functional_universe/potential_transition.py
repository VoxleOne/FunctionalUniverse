class PotentialTransition:
    """
    Represents a latent state and its space of possible functional outcomes.
    Lives in category 𝒞 (aggregation of possibilities).
    """
    def __init__(self, state, possibilities):
        """
        Args:
            state: The latent state before causal commitment.
            possibilities: Possible outcomes (functions to be composed in 𝒟).
        """
        self.state = state
        self.possibilities = possibilities

    def aggregate(self, other):
        """
        Combine two potential transitions (superpositional merging).

        Args:
            other: Another PotentialTransition.
        Returns:
            A new aggregated PotentialTransition.
        """
        combined_possibilities = self.possibilities.union(other.possibilities)
        return PotentialTransition(self.state, combined_possibilities)

    def commit(self, decision_rule):
        """
        Commit to one specific outcome (causal commitment, 𝒟).

        Args:
            decision_rule: Callable to select a specific possibility.
        Returns:
            A Transition object in the category 𝒟.
        """
        selected = decision_rule(self.possibilities)
        return Transition(selected.function, selected.duration, selected.entropy)