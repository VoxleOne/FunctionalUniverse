# Functional Universe

Modeling the cosmos as a sequence of functional states.

## Overview

FunctionalUniverse is a Python implementation of a model universe based on five fundamental axioms that govern state transitions, composition, and causality.

## The Five Axioms

### Axiom 1: Compositional Structure
The universe is a compositional structure of functions. Every state transition is represented as a function that can be composed with other functions.

### Axiom 2: Minimum Duration (dτmin)
There exists a universal, nonzero minimum duration `dτmin` for any physical state transition. No transition can occur instantaneously.

### Axiom 3: Minimum Entropy
Every irreducible transition carries a minimum entropy. State changes inherently increase entropy according to this fundamental bound.

### Axiom 4: Causal Ordering
Causality is the ordered composability of transitions; only the composable influence each other. Transitions form causal chains through composition.

### Axiom 5: Universal Upper Bound (c)
The minimum transition duration implies a universal upper bound on causal composition, denoted `c`. This represents the maximum rate at which transitions can be composed, analogous to a speed limit in physics.

## Installation

```bash
# Clone the repository
git clone https://github.com/VoxleOne/FunctionalUniverse.git
cd FunctionalUniverse

# No external dependencies required - uses only Python standard library
```

## Quick Start

```python
from functional_universe import Universe, UniverseConstants, Transition

# Create a universe with specific constants
constants = UniverseConstants(
    dt_min=1.0,           # Minimum duration (Axiom 2)
    minimum_entropy=0.5,  # Minimum entropy (Axiom 3)
    c=10.0                # Causal composition bound (Axiom 5)
)
universe = Universe(constants)

# Define state transformations (Axiom 1)
increment = universe.create_transition(
    function=lambda x: x + 1,
    duration=1.5,
    entropy=1.0,
    name="Increment"
)

double = universe.create_transition(
    function=lambda x: x * 2,
    duration=2.0,
    entropy=1.0,
    name="Double"
)

# Compose transitions (Axiom 4)
composed = universe.compose(increment, double)

# Apply to a state
initial_state = 5
final_state = composed.apply(initial_state)
print(f"Result: {final_state}")  # (5 + 1) * 2 = 12

# Or evolve through multiple transitions
final_state = universe.evolve(5, [increment, double])
print(f"Evolved: {final_state}")  # 12
```

## Examples

Run the included examples to see all axioms in action:

```bash
python examples.py
```

This will demonstrate:
- Simple universe creation and evolution
- Axiom violations and validation
- Causal composition bounds

## Running Tests

```bash
python -m unittest tests/test_functional_universe.py
```

Or run all tests with verbose output:

```bash
python -m unittest discover -s tests -v
```

## Core Concepts

### UniverseConstants

Defines the fundamental constants of our universe:

```python
constants = UniverseConstants(
    dt_min=1.0,           # Minimum transition duration
    minimum_entropy=0.5,  # Minimum entropy per transition
    c=10.0                # Upper bound on causal composition
)
```

### Transition

Represents an irreducible state transition:

```python
transition = Transition(
    function=lambda x: x * 2,  # State transformation
    duration=1.5,               # Duration of transition
    entropy=1.0,                # Entropy change
    name="Double"               # Optional name
)
```

### Universe

Orchestrates transitions according to all five axioms:

```python
universe = Universe(constants)

# Add transitions
t1 = universe.create_transition(lambda x: x + 1, 1.0, name="Inc")
t2 = universe.create_transition(lambda x: x * 2, 1.0, name="Double")

# Compose transitions
composed = universe.compose(t1, t2)

# Evolve states
final = universe.evolve(initial_state, [t1, t2])

# Validate causal rates
is_valid = universe.is_causal_rate_valid([t1, t2])
```

## API Reference

### UniverseConstants

- `dt_min`: Minimum duration for any transition (Axiom 2)
- `minimum_entropy`: Minimum entropy per transition (Axiom 3)
- `c`: Universal upper bound on causal composition (Axiom 5)
- `max_composition_rate()`: Calculate maximum transitions per unit time

### Transition

- `function`: State transformation function (Axiom 1)
- `duration`: Duration of this transition (Axiom 2)
- `entropy`: Entropy of this transition (Axiom 3)
- `causal_order`: Position in causal chain (Axiom 4)
- `apply(state)`: Apply transition to a state
- `compose(other, constants)`: Compose with another transition
- `validate(constants)`: Validate against universe constants

### Universe

- `constants`: Universe constants
- `transitions`: All transitions in the universe
- `add_transition(transition)`: Add a transition
- `create_transition(function, duration, entropy, name)`: Create and add a transition
- `compose(t1, t2)`: Compose two transitions
- `compose_chain(transitions)`: Compose multiple transitions
- `evolve(initial_state, transitions)`: Evolve state through transitions
- `total_evolution_duration(transitions)`: Calculate total duration
- `total_entropy(transitions)`: Calculate total entropy
- `is_causal_rate_valid(transitions)`: Check if transitions respect causal bounds

## License

MIT License - See LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
