"""
Universe - The orchestrator of all transitions in the FunctionalUniverse.

Implements all five axioms through coordination of transitions and constants.
"""

from typing import List, Any, Callable
from .transition import Transition
from .constants import UniverseConstants


class Universe:
    """
    The universe as a compositional structure of functions.
    
    This class orchestrates transitions according to all five axioms:
    1. Compositional structure of functions
    2. Universal minimum duration
    3. Minimum entropy per transition
    4. Causal ordering and composability
    5. Universal upper bound on causal composition
    """
    
    def __init__(self, constants: UniverseConstants = None):
        """
        Initialize a new universe.
        
        Args:
            constants: Universe constants (dt_min, minimum_entropy, c).
                      If None, default constants are used.
        """
        self._constants = constants or UniverseConstants()
        self._transitions: List[Transition] = []
        self._causal_chains: List[List[Transition]] = []
        self._current_state = None
    
    @property
    def constants(self) -> UniverseConstants:
        """The universal constants governing this universe."""
        return self._constants
    
    @property
    def transitions(self) -> List[Transition]:
        """All transitions registered in this universe."""
        return self._transitions.copy()
    
    def add_transition(self, transition: Transition) -> 'Universe':
        """
        Add a transition to the universe (Axiom 1, 2, 3).
        
        The transition is validated against universe constants.
        
        Args:
            transition: The transition to add.
        
        Returns:
            Self for method chaining.
        
        Raises:
            ValueError: If transition violates any axioms.
        """
        # Validate transition against universe constants
        transition.validate(self._constants)
        
        # Add to universe
        self._transitions.append(transition)
        transition.set_causal_order(len(self._transitions))
        
        return self
    
    def create_transition(self, function: Callable[[Any], Any], 
                         duration: float, entropy: float = None,
                         name: str = None) -> Transition:
        """
        Create and add a transition to the universe.
        
        Args:
            function: State transformation function.
            duration: Duration of the transition.
            entropy: Entropy of the transition (optional, defaults to minimum).
            name: Name for the transition (optional).
        
        Returns:
            The created transition.
        
        Raises:
            ValueError: If transition violates any axioms.
        """
        transition = Transition(function, duration, entropy, name)
        self.add_transition(transition)
        return transition
    
    def compose(self, t1: Transition, t2: Transition) -> Transition:
        """
        Compose two transitions (Axiom 1, 4, 5).
        
        Args:
            t1: First transition.
            t2: Second transition.
        
        Returns:
            Composed transition.
        
        Raises:
            ValueError: If transitions cannot be composed or would violate bounds.
        """
        if not t1.is_composable_with(t2):
            raise ValueError(
                f"Transitions {t1.name} and {t2.name} are not composable (Axiom 4)"
            )
        
        return t1.compose(t2, self._constants)
    
    def compose_chain(self, transitions: List[Transition]) -> Transition:
        """
        Compose a chain of transitions in causal order (Axiom 4).
        
        Args:
            transitions: List of transitions to compose in order.
        
        Returns:
            Single composed transition representing the entire chain.
        
        Raises:
            ValueError: If chain is empty or composition violates bounds.
        """
        if not transitions:
            raise ValueError("Cannot compose empty transition chain")
        
        if len(transitions) == 1:
            return transitions[0]
        
        # Compose sequentially (left to right, maintaining causal order)
        result = transitions[0]
        for t in transitions[1:]:
            result = self.compose(result, t)
        
        return result
    
    def evolve(self, initial_state: Any, transitions: List[Transition]) -> Any:
        """
        Evolve a state through a sequence of transitions (Axiom 1, 4).
        
        This applies transitions in causal order, respecting all axioms.
        
        Args:
            initial_state: The starting state.
            transitions: List of transitions to apply in order.
        
        Returns:
            The final state after all transitions.
        """
        state = initial_state
        self._current_state = state
        
        # Apply each transition in causal order
        for transition in transitions:
            state = transition.apply(state)
            self._current_state = state
        
        return state
    
    def total_evolution_duration(self, transitions: List[Transition]) -> float:
        """
        Calculate total duration for a sequence of transitions (Axiom 2, 5).
        
        Args:
            transitions: List of transitions.
        
        Returns:
            Total duration in universe time units.
        """
        return sum(t.duration for t in transitions)
    
    def total_entropy(self, transitions: List[Transition]) -> float:
        """
        Calculate total entropy for a sequence of transitions (Axiom 3).
        
        Args:
            transitions: List of transitions. All transitions should be validated
                        (have non-None entropy values).
        
        Returns:
            Total entropy.
        
        Raises:
            TypeError: If any transition has None entropy (not validated).
        
        Note:
            All transitions added to the universe via add_transition() are
            automatically validated and will have entropy set.
        """
        try:
            return sum(t.entropy for t in transitions)
        except TypeError:
            raise TypeError(
                "Cannot calculate total entropy: one or more transitions have "
                "None entropy. Ensure all transitions are validated first."
            )
    
    def is_causal_rate_valid(self, transitions: List[Transition]) -> bool:
        """
        Check if a sequence of transitions respects the causal bound (Axiom 5).
        
        The rate of transitions must not exceed c / dt_min.
        
        Args:
            transitions: List of transitions to check.
        
        Returns:
            True if the causal rate is valid, False otherwise.
        """
        if not transitions:
            return True
        
        total_duration = self.total_evolution_duration(transitions)
        num_transitions = len(transitions)
        max_rate = self._constants.max_composition_rate()
        
        # Rate = number of transitions / total duration
        # Must satisfy: rate <= max_rate
        # Equivalently: num_transitions / total_duration <= max_rate
        # Equivalently: total_duration >= num_transitions / max_rate
        min_required_duration = num_transitions / max_rate
        
        return total_duration >= min_required_duration
    
    def get_state(self) -> Any:
        """Get the current state of the universe."""
        return self._current_state
    
    def set_state(self, state: Any):
        """Set the current state of the universe."""
        self._current_state = state
    
    def __repr__(self):
        return (f"Universe(constants={self._constants}, "
                f"transitions={len(self._transitions)})")
