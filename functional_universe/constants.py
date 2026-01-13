"""
Universal constants for the FunctionalUniverse.

Implements Axiom 2 (minimum duration) and Axiom 5 (upper bound on causal composition).
"""


class UniverseConstants:
    """
    Universal constants that govern the functional universe.
    
    Axiom 2: dτmin - Universal minimum duration for any physical state transition.
    Axiom 3: minimum_entropy - Minimum entropy for any irreducible transition.
    Axiom 5: c - Universal upper bound on causal composition rate.
    """
    
    def __init__(self, dt_min=1.0, minimum_entropy=1.0, c=1.0):
        """
        Initialize universe constants.
        
        Args:
            dt_min: Minimum duration for any state transition (dτmin).
                   Must be nonzero and positive (Axiom 2).
            minimum_entropy: Minimum entropy for any irreducible transition (Axiom 3).
            c: Universal upper bound on causal composition (Axiom 5).
               Represents the maximum rate at which transitions can be composed.
        
        Raises:
            ValueError: If any constant is zero or negative.
        """
        if dt_min <= 0:
            raise ValueError("dt_min must be nonzero and positive (Axiom 2)")
        if minimum_entropy <= 0:
            raise ValueError("minimum_entropy must be positive (Axiom 3)")
        if c <= 0:
            raise ValueError("c must be positive (Axiom 5)")
        
        self._dt_min = dt_min
        self._minimum_entropy = minimum_entropy
        self._c = c
    
    @property
    def dt_min(self):
        """Universal minimum duration for state transitions (Axiom 2)."""
        return self._dt_min
    
    @property
    def minimum_entropy(self):
        """Minimum entropy per irreducible transition (Axiom 3)."""
        return self._minimum_entropy
    
    @property
    def c(self):
        """Universal upper bound on causal composition (Axiom 5)."""
        return self._c
    
    def max_composition_rate(self):
        """
        Calculate the maximum rate at which transitions can be composed.
        
        Based on Axiom 5: The minimum transition duration implies an upper bound
        on causal composition.
        
        Returns:
            float: Maximum transitions per unit time = c / dt_min
        """
        return self._c / self._dt_min
    
    def __repr__(self):
        return (f"UniverseConstants(dt_min={self._dt_min}, "
                f"minimum_entropy={self._minimum_entropy}, c={self._c})")
