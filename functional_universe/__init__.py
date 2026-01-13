"""
FunctionalUniverse - Modeling the cosmos as a sequence of functional states.

This package implements a universe based on five fundamental axioms:
1. The universe is a compositional structure of functions
2. Universal minimum duration (dτmin) for state transitions
3. Minimum entropy per transition
4. Causal ordering through composability
5. Universal upper bound (c) on causal composition
"""

from .transition import Transition
from .universe import Universe
from .constants import UniverseConstants

__version__ = "0.1.0"
__all__ = ["Transition", "Universe", "UniverseConstants"]
