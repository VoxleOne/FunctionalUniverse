"""
Transition - The fundamental unit of state change in the FunctionalUniverse.

Implements Axiom 1 (functional composition), Axiom 2 (minimum duration),
Axiom 3 (minimum entropy), and Axiom 4 (causal ordering).
"""

from typing import Callable, Any, Optional


class Transition:
    """
    Represents an irreducible state transition in the functional universe.
    
    Axiom 1: Each transition is a function that transforms one state to another.
    Axiom 2: Each transition has a duration >= dt_min.
    Axiom 3: Each transition carries entropy >= minimum_entropy.
    Axiom 4: Transitions can be composed to form causal chains.
    """
    
    def __init__(self, function: Callable[[Any], Any], duration: float, 
                 entropy: Optional[float] = None, name: Optional[str] = None):
        """
        Create a new transition.
        
        Args:
            function: The state transformation function (Axiom 1).
            duration: Duration of this transition, must be >= dt_min (Axiom 2).
            entropy: Entropy of this transition, defaults to minimum_entropy (Axiom 3).
            name: Optional name for this transition for debugging.
        
        Note: The duration and entropy constraints are validated when the transition
              is added to a Universe with specific constants.
        """
        self._function = function
        self._duration = duration
        self._entropy = entropy
        self._name = name or f"Transition_{id(self)}"
        self._causal_order = 0  # Position in causal chain (Axiom 4)
    
    @property
    def function(self) -> Callable[[Any], Any]:
        """The state transformation function (Axiom 1)."""
        return self._function
    
    @property
    def duration(self) -> float:
        """Duration of this transition (Axiom 2)."""
        return self._duration
    
    @property
    def entropy(self) -> Optional[float]:
        """Entropy of this transition (Axiom 3)."""
        return self._entropy
    
    @property
    def name(self) -> str:
        """Name of this transition."""
        return self._name
    
    @property
    def causal_order(self) -> int:
        """Position in causal chain (Axiom 4)."""
        return self._causal_order
    
    def set_causal_order(self, order: int):
        """Set the causal order of this transition (Axiom 4)."""
        self._causal_order = order
    
    def apply(self, state: Any) -> Any:
        """
        Apply this transition to a state (Axiom 1).
        
        Args:
            state: The current state to transform.
        
        Returns:
            The new state after applying this transition.
        """
        return self._function(state)
    
    def compose(self, other: 'Transition', constants: Any) -> 'Transition':
        """
        Compose this transition with another (Axiom 4).
        
        Axiom 4: Causality is the ordered composability of transitions;
        only the composable influence each other.
        
        Args:
            other: Another transition to compose with this one.
            constants: Universe constants for validation.
        
        Returns:
            A new transition representing the composition.
        
        Raises:
            ValueError: If composition would violate causal composition bounds.
        """
        # Check if composition is allowed (Axiom 5)
        composed_duration = self._duration + other._duration
        max_rate = constants.max_composition_rate()
        
        # The composition should not exceed the causal bound
        # In terms of duration, we need: duration >= (number_of_transitions / max_rate)
        # For 2 transitions: duration >= 2 / max_rate = 2 * dt_min / c
        min_allowed_duration = 2.0 / max_rate
        
        if composed_duration < min_allowed_duration:
            raise ValueError(
                f"Composition would violate causal rate bound: "
                f"{composed_duration} < {min_allowed_duration}"
            )
        
        # Create composed function (Axiom 1: compositional structure)
        def composed_function(state):
            intermediate_state = self._function(state)
            return other._function(intermediate_state)
        
        # Sum entropies (entropy is additive for composed transitions)
        composed_entropy = None
        if self._entropy is not None and other._entropy is not None:
            composed_entropy = self._entropy + other._entropy
        
        # Create composed transition
        composed = Transition(
            function=composed_function,
            duration=composed_duration,
            entropy=composed_entropy,
            name=f"{self._name} >> {other._name}"
        )
        
        # Maintain causal order (Axiom 4)
        composed.set_causal_order(max(self._causal_order, other._causal_order) + 1)
        
        return composed
    
    def is_composable_with(self, other: 'Transition') -> bool:
        """
        Check if this transition can be composed with another (Axiom 4).
        
        Axiom 4: Only composable transitions influence each other.
        For now, we consider all transitions potentially composable,
        but this could be extended with compatibility rules.
        
        Args:
            other: Another transition.
        
        Returns:
            True if transitions can be composed.
        """
        # Basic composability: transitions can be composed if they exist
        # More sophisticated rules could be added based on state types, etc.
        return other is not None
    
    def validate(self, constants: Any):
        """
        Validate this transition against universe constants.
        
        Sets entropy to minimum_entropy if not specified, then validates all constraints.
        
        Args:
            constants: UniverseConstants to validate against.
        
        Raises:
            ValueError: If transition violates any axioms.
        """
        # If no entropy specified, set to minimum (Axiom 3)
        if self._entropy is None:
            self._entropy = constants.minimum_entropy
        
        # Axiom 2: Check minimum duration
        if self._duration < constants.dt_min:
            raise ValueError(
                f"Transition duration {self._duration} is less than "
                f"minimum duration {constants.dt_min} (Axiom 2)"
            )
        
        # Axiom 3: Check minimum entropy
        if self._entropy < constants.minimum_entropy:
            raise ValueError(
                f"Transition entropy {self._entropy} is less than "
                f"minimum entropy {constants.minimum_entropy} (Axiom 3)"
            )
    
    def __repr__(self):
        return (f"Transition(name='{self._name}', duration={self._duration}, "
                f"entropy={self._entropy}, causal_order={self._causal_order})")
    
    def __rshift__(self, other: 'Transition'):
        """
        Syntactic sugar for composition using >> operator.
        
        Note: This returns a lambda that needs constants to complete composition.
        Use Universe.compose() for proper composition with validation.
        """
        def compose_with_constants(constants):
            return self.compose(other, constants)
        return compose_with_constants
