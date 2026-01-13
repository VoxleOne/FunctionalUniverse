"""
Tests for the FunctionalUniverse package.
"""

import unittest
from functional_universe import Universe, UniverseConstants, Transition


class TestUniverseConstants(unittest.TestCase):
    """Tests for UniverseConstants (Axiom 2, 3, 5)."""
    
    def test_valid_constants(self):
        """Test creating valid universe constants."""
        constants = UniverseConstants(dt_min=1.0, minimum_entropy=0.5, c=10.0)
        self.assertEqual(constants.dt_min, 1.0)
        self.assertEqual(constants.minimum_entropy, 0.5)
        self.assertEqual(constants.c, 10.0)
    
    def test_default_constants(self):
        """Test default constant values."""
        constants = UniverseConstants()
        self.assertEqual(constants.dt_min, 1.0)
        self.assertEqual(constants.minimum_entropy, 1.0)
        self.assertEqual(constants.c, 1.0)
    
    def test_zero_dt_min_rejected(self):
        """Test that zero dt_min is rejected (Axiom 2)."""
        with self.assertRaises(ValueError) as context:
            UniverseConstants(dt_min=0.0)
        self.assertIn("nonzero", str(context.exception).lower())
    
    def test_negative_dt_min_rejected(self):
        """Test that negative dt_min is rejected (Axiom 2)."""
        with self.assertRaises(ValueError) as context:
            UniverseConstants(dt_min=-1.0)
        self.assertIn("positive", str(context.exception).lower())
    
    def test_zero_minimum_entropy_rejected(self):
        """Test that zero minimum_entropy is rejected (Axiom 3)."""
        with self.assertRaises(ValueError) as context:
            UniverseConstants(minimum_entropy=0.0)
        self.assertIn("positive", str(context.exception).lower())
    
    def test_zero_c_rejected(self):
        """Test that zero c is rejected (Axiom 5)."""
        with self.assertRaises(ValueError) as context:
            UniverseConstants(c=0.0)
        self.assertIn("positive", str(context.exception).lower())
    
    def test_max_composition_rate(self):
        """Test maximum composition rate calculation (Axiom 5)."""
        constants = UniverseConstants(dt_min=2.0, c=10.0)
        self.assertEqual(constants.max_composition_rate(), 5.0)


class TestTransition(unittest.TestCase):
    """Tests for Transition (Axiom 1, 2, 3, 4)."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.constants = UniverseConstants(dt_min=1.0, minimum_entropy=0.5, c=10.0)
    
    def test_create_transition(self):
        """Test creating a basic transition (Axiom 1)."""
        def increment(x):
            return x + 1
        
        t = Transition(increment, duration=1.5, entropy=1.0, name="Increment")
        self.assertEqual(t.name, "Increment")
        self.assertEqual(t.duration, 1.5)
        self.assertEqual(t.entropy, 1.0)
    
    def test_apply_transition(self):
        """Test applying a transition to a state (Axiom 1)."""
        t = Transition(lambda x: x * 2, duration=1.0, name="Double")
        result = t.apply(5)
        self.assertEqual(result, 10)
    
    def test_validate_duration(self):
        """Test duration validation (Axiom 2)."""
        t = Transition(lambda x: x, duration=0.5, name="TooShort")
        with self.assertRaises(ValueError) as context:
            t.validate(self.constants)
        self.assertIn("minimum duration", str(context.exception).lower())
    
    def test_validate_entropy(self):
        """Test entropy validation (Axiom 3)."""
        t = Transition(lambda x: x, duration=1.5, entropy=0.1, name="LowEntropy")
        with self.assertRaises(ValueError) as context:
            t.validate(self.constants)
        self.assertIn("minimum entropy", str(context.exception).lower())
    
    def test_entropy_defaults_to_minimum(self):
        """Test that entropy defaults to minimum when not specified (Axiom 3)."""
        t = Transition(lambda x: x, duration=1.5, name="NoEntropy")
        t.validate(self.constants)
        self.assertEqual(t.entropy, self.constants.minimum_entropy)
    
    def test_compose_transitions(self):
        """Test composing two transitions (Axiom 1, 4)."""
        t1 = Transition(lambda x: x + 1, duration=1.0, entropy=0.5, name="Inc")
        t2 = Transition(lambda x: x * 2, duration=1.0, entropy=0.5, name="Double")
        
        composed = t1.compose(t2, self.constants)
        
        # Test the composed function
        result = composed.apply(5)
        self.assertEqual(result, (5 + 1) * 2)  # 12
        
        # Test duration and entropy are summed
        self.assertEqual(composed.duration, 2.0)
        self.assertEqual(composed.entropy, 1.0)
    
    def test_causal_order_increases(self):
        """Test that causal order increases with composition (Axiom 4)."""
        t1 = Transition(lambda x: x, duration=1.0, name="T1")
        t2 = Transition(lambda x: x, duration=1.0, name="T2")
        
        t1.set_causal_order(1)
        t2.set_causal_order(2)
        
        composed = t1.compose(t2, self.constants)
        self.assertGreater(composed.causal_order, t1.causal_order)
        self.assertGreater(composed.causal_order, t2.causal_order)
    
    def test_is_composable_with(self):
        """Test composability check (Axiom 4)."""
        t1 = Transition(lambda x: x, duration=1.0)
        t2 = Transition(lambda x: x, duration=1.0)
        
        self.assertTrue(t1.is_composable_with(t2))
        self.assertFalse(t1.is_composable_with(None))


class TestUniverse(unittest.TestCase):
    """Tests for Universe (all axioms)."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.constants = UniverseConstants(dt_min=1.0, minimum_entropy=0.5, c=10.0)
        self.universe = Universe(self.constants)
    
    def test_create_universe(self):
        """Test creating a universe."""
        universe = Universe()
        self.assertIsNotNone(universe.constants)
    
    def test_create_universe_with_constants(self):
        """Test creating a universe with specific constants."""
        self.assertEqual(self.universe.constants, self.constants)
    
    def test_add_valid_transition(self):
        """Test adding a valid transition (Axiom 1, 2, 3)."""
        t = Transition(lambda x: x + 1, duration=1.5, entropy=1.0, name="Inc")
        self.universe.add_transition(t)
        
        self.assertEqual(len(self.universe.transitions), 1)
        self.assertEqual(self.universe.transitions[0], t)
    
    def test_add_invalid_duration_rejected(self):
        """Test that transitions violating Axiom 2 are rejected."""
        t = Transition(lambda x: x, duration=0.5, name="BadDuration")
        with self.assertRaises(ValueError):
            self.universe.add_transition(t)
    
    def test_add_invalid_entropy_rejected(self):
        """Test that transitions violating Axiom 3 are rejected."""
        t = Transition(lambda x: x, duration=1.5, entropy=0.1, name="BadEntropy")
        with self.assertRaises(ValueError):
            self.universe.add_transition(t)
    
    def test_create_transition_helper(self):
        """Test the create_transition helper method."""
        t = self.universe.create_transition(
            lambda x: x * 2, duration=1.5, entropy=1.0, name="Double"
        )
        
        self.assertEqual(t.name, "Double")
        self.assertEqual(len(self.universe.transitions), 1)
    
    def test_compose_two_transitions(self):
        """Test composing two transitions (Axiom 4)."""
        t1 = self.universe.create_transition(lambda x: x + 1, 1.0, name="Inc")
        t2 = self.universe.create_transition(lambda x: x * 2, 1.0, name="Double")
        
        composed = self.universe.compose(t1, t2)
        result = composed.apply(5)
        self.assertEqual(result, 12)  # (5 + 1) * 2
    
    def test_compose_chain(self):
        """Test composing a chain of transitions (Axiom 4)."""
        t1 = self.universe.create_transition(lambda x: x + 1, 1.0, name="Inc")
        t2 = self.universe.create_transition(lambda x: x * 2, 1.0, name="Double")
        t3 = self.universe.create_transition(lambda x: x ** 2, 1.0, name="Square")
        
        composed = self.universe.compose_chain([t1, t2, t3])
        result = composed.apply(5)
        self.assertEqual(result, 144)  # ((5 + 1) * 2) ** 2
    
    def test_compose_single_transition(self):
        """Test composing a single transition returns itself."""
        t = self.universe.create_transition(lambda x: x + 1, 1.0, name="Inc")
        composed = self.universe.compose_chain([t])
        self.assertEqual(composed, t)
    
    def test_compose_empty_chain_fails(self):
        """Test that composing an empty chain raises error."""
        with self.assertRaises(ValueError):
            self.universe.compose_chain([])
    
    def test_evolve_state(self):
        """Test evolving a state through transitions (Axiom 1)."""
        t1 = self.universe.create_transition(lambda x: x + 10, 1.0, name="Add10")
        t2 = self.universe.create_transition(lambda x: x * 3, 1.0, name="Triple")
        
        final_state = self.universe.evolve(5, [t1, t2])
        self.assertEqual(final_state, 45)  # (5 + 10) * 3
    
    def test_total_evolution_duration(self):
        """Test calculating total evolution duration (Axiom 2)."""
        t1 = self.universe.create_transition(lambda x: x, 1.5, name="T1")
        t2 = self.universe.create_transition(lambda x: x, 2.0, name="T2")
        t3 = self.universe.create_transition(lambda x: x, 1.0, name="T3")
        
        total = self.universe.total_evolution_duration([t1, t2, t3])
        self.assertEqual(total, 4.5)
    
    def test_total_entropy(self):
        """Test calculating total entropy (Axiom 3)."""
        t1 = self.universe.create_transition(lambda x: x, 1.0, entropy=1.0, name="T1")
        t2 = self.universe.create_transition(lambda x: x, 1.0, entropy=2.0, name="T2")
        t3 = self.universe.create_transition(lambda x: x, 1.0, entropy=1.5, name="T3")
        
        total = self.universe.total_entropy([t1, t2, t3])
        self.assertEqual(total, 4.5)
    
    def test_causal_rate_valid(self):
        """Test causal rate validation (Axiom 5)."""
        # Max rate is 10.0 transitions/time
        # With dt_min=1.0, we can have at most 10 transitions per time unit
        
        # 3 transitions in 3 seconds: rate = 1.0 < 10.0 (valid)
        transitions = [
            self.universe.create_transition(lambda x: x, 1.0, name=f"T{i}")
            for i in range(3)
        ]
        self.assertTrue(self.universe.is_causal_rate_valid(transitions))
    
    def test_causal_rate_within_bounds(self):
        """Test causal rate well within bounds (Axiom 5)."""
        # With dt_min=1.0, c=10.0: max_rate = 10.0 transitions/time
        # Create 10 transitions with minimum duration = 10.0 total
        # Rate = 10 / 10.0 = 1.0, which is well below max_rate of 10.0
        transitions = [
            self.universe.create_transition(lambda x: x, 1.0, name=f"T{i}")
            for i in range(10)
        ]
        self.assertTrue(self.universe.is_causal_rate_valid(transitions))
    
    def test_get_set_state(self):
        """Test getting and setting universe state."""
        self.universe.set_state(42)
        self.assertEqual(self.universe.get_state(), 42)
    
    def test_evolve_updates_state(self):
        """Test that evolve updates the current state."""
        t = self.universe.create_transition(lambda x: x * 2, 1.0, name="Double")
        self.universe.evolve(10, [t])
        self.assertEqual(self.universe.get_state(), 20)


class TestIntegration(unittest.TestCase):
    """Integration tests for the full system."""
    
    def test_full_workflow(self):
        """Test a complete workflow using all axioms."""
        # Create universe with specific physics
        constants = UniverseConstants(dt_min=0.5, minimum_entropy=1.0, c=20.0)
        universe = Universe(constants)
        
        # Create transitions
        increment = universe.create_transition(
            lambda x: x + 1, duration=1.0, entropy=1.5, name="Increment"
        )
        double = universe.create_transition(
            lambda x: x * 2, duration=0.5, entropy=1.0, name="Double"
        )
        
        # Compose them
        composed = universe.compose(increment, double)
        
        # Verify composition
        result = composed.apply(5)
        self.assertEqual(result, 12)  # (5 + 1) * 2
        
        # Verify total duration
        self.assertEqual(composed.duration, 1.5)
        
        # Verify total entropy
        self.assertEqual(composed.entropy, 2.5)
        
        # Verify causal rate
        self.assertTrue(universe.is_causal_rate_valid([increment, double]))


if __name__ == '__main__':
    unittest.main()
