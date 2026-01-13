"""
Examples demonstrating the FunctionalUniverse axioms.
"""

from functional_universe import Universe, UniverseConstants, Transition


def example_simple_universe():
    """
    Example: A simple universe with basic state transitions.
    
    Demonstrates all five axioms in action.
    """
    print("=" * 70)
    print("Example: Simple Functional Universe")
    print("=" * 70)
    
    # Create a universe with specific constants
    # Axiom 2: dt_min = 1.0 (minimum duration)
    # Axiom 3: minimum_entropy = 0.5 (minimum entropy per transition)
    # Axiom 5: c = 10.0 (upper bound on causal composition)
    constants = UniverseConstants(dt_min=1.0, minimum_entropy=0.5, c=10.0)
    universe = Universe(constants)
    
    print(f"\nUniverse Constants: {constants}")
    print(f"Maximum composition rate: {constants.max_composition_rate()} transitions/time")
    
    # Axiom 1: The universe is a compositional structure of functions
    # Define some state transformations (functions)
    
    def increment(x):
        """Increment the state."""
        return x + 1
    
    def double(x):
        """Double the state."""
        return x * 2
    
    def square(x):
        """Square the state."""
        return x ** 2
    
    # Create transitions (Axiom 1, 2, 3)
    # Each transition must have duration >= dt_min (Axiom 2)
    # Each transition must have entropy >= minimum_entropy (Axiom 3)
    print("\n--- Creating Transitions ---")
    
    t1 = universe.create_transition(
        function=increment,
        duration=1.5,  # >= dt_min
        entropy=0.7,   # >= minimum_entropy
        name="Increment"
    )
    print(f"Created: {t1}")
    
    t2 = universe.create_transition(
        function=double,
        duration=2.0,
        entropy=1.0,
        name="Double"
    )
    print(f"Created: {t2}")
    
    t3 = universe.create_transition(
        function=square,
        duration=1.0,  # Exactly at minimum
        entropy=0.5,   # Exactly at minimum
        name="Square"
    )
    print(f"Created: {t3}")
    
    # Axiom 4: Causality is the ordered composability of transitions
    # Compose transitions to form causal chains
    print("\n--- Composing Transitions (Axiom 4) ---")
    
    # Compose t1 and t2: (x + 1) * 2
    composed_12 = universe.compose(t1, t2)
    print(f"Composed t1 >> t2: {composed_12}")
    print(f"  Duration: {composed_12.duration}, Entropy: {composed_12.entropy}")
    
    # Compose entire chain: ((x + 1) * 2) ^ 2
    composed_all = universe.compose_chain([t1, t2, t3])
    print(f"Composed t1 >> t2 >> t3: {composed_all}")
    print(f"  Duration: {composed_all.duration}, Entropy: {composed_all.entropy}")
    
    # Axiom 5: Check causal rate validity
    print("\n--- Validating Causal Rate (Axiom 5) ---")
    chain = [t1, t2, t3]
    total_duration = universe.total_evolution_duration(chain)
    is_valid = universe.is_causal_rate_valid(chain)
    print(f"Transition chain: {[t.name for t in chain]}")
    print(f"Total duration: {total_duration}")
    print(f"Number of transitions: {len(chain)}")
    print(f"Causal rate valid: {is_valid}")
    
    # Evolve a state through the universe
    print("\n--- Evolving States (Axiom 1) ---")
    initial_state = 5
    print(f"Initial state: {initial_state}")
    
    # Apply t1: 5 + 1 = 6
    state1 = t1.apply(initial_state)
    print(f"After {t1.name}: {state1}")
    
    # Apply t2: 6 * 2 = 12
    state2 = t2.apply(state1)
    print(f"After {t2.name}: {state2}")
    
    # Apply t3: 12 ^ 2 = 144
    state3 = t3.apply(state2)
    print(f"After {t3.name}: {state3}")
    
    # Or evolve through entire chain at once
    final_state = universe.evolve(initial_state, [t1, t2, t3])
    print(f"\nFinal state (evolve): {final_state}")
    
    # Verify composed transition gives same result
    composed_result = composed_all.apply(initial_state)
    print(f"Final state (composed): {composed_result}")
    print(f"Results match: {final_state == composed_result}")
    
    print("\n" + "=" * 70)


def example_axiom_violations():
    """
    Example: Demonstrating what happens when axioms are violated.
    """
    print("\n" + "=" * 70)
    print("Example: Axiom Violations")
    print("=" * 70)
    
    constants = UniverseConstants(dt_min=1.0, minimum_entropy=0.5, c=10.0)
    universe = Universe(constants)
    
    # Attempt to violate Axiom 2 (minimum duration)
    print("\n--- Testing Axiom 2: Minimum Duration ---")
    try:
        bad_transition = Transition(
            function=lambda x: x + 1,
            duration=0.5,  # Less than dt_min!
            entropy=1.0,
            name="BadDuration"
        )
        universe.add_transition(bad_transition)
        print("ERROR: Should have raised ValueError!")
    except ValueError as e:
        print(f"✓ Correctly rejected: {e}")
    
    # Attempt to violate Axiom 3 (minimum entropy)
    print("\n--- Testing Axiom 3: Minimum Entropy ---")
    try:
        bad_entropy = Transition(
            function=lambda x: x * 2,
            duration=1.5,
            entropy=0.1,  # Less than minimum_entropy!
            name="BadEntropy"
        )
        universe.add_transition(bad_entropy)
        print("ERROR: Should have raised ValueError!")
    except ValueError as e:
        print(f"✓ Correctly rejected: {e}")
    
    # Test edge case: exactly at minimum is OK
    print("\n--- Testing Edge Case: Exactly at Minimum ---")
    try:
        ok_transition = Transition(
            function=lambda x: x + 10,
            duration=1.0,  # Exactly dt_min
            entropy=0.5,   # Exactly minimum_entropy
            name="ExactMinimum"
        )
        universe.add_transition(ok_transition)
        print(f"✓ Accepted: {ok_transition}")
    except ValueError as e:
        print(f"ERROR: Should have accepted: {e}")
    
    print("\n" + "=" * 70)


def example_causal_bounds():
    """
    Example: Exploring Axiom 5 - causal composition bounds.
    """
    print("\n" + "=" * 70)
    print("Example: Causal Composition Bounds (Axiom 5)")
    print("=" * 70)
    
    # Create universe with tight bounds
    constants = UniverseConstants(dt_min=1.0, minimum_entropy=1.0, c=5.0)
    universe = Universe(constants)
    
    print(f"\nConstants: {constants}")
    print(f"Max composition rate: {constants.max_composition_rate()} transitions/time")
    
    # Create several short transitions
    transitions = []
    for i in range(5):
        t = universe.create_transition(
            function=lambda x, i=i: x + i,
            duration=1.0,  # Minimum duration
            name=f"T{i}"
        )
        transitions.append(t)
    
    # Test different chain lengths
    print("\n--- Testing Chain Lengths ---")
    for length in [1, 2, 3, 4, 5]:
        chain = transitions[:length]
        total_duration = universe.total_evolution_duration(chain)
        is_valid = universe.is_causal_rate_valid(chain)
        rate = length / total_duration if total_duration > 0 else float('inf')
        
        print(f"Chain length {length}: duration={total_duration:.1f}, "
              f"rate={rate:.2f}, valid={is_valid}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    example_simple_universe()
    example_axiom_violations()
    example_causal_bounds()
    
    print("\n✓ All examples completed successfully!")
