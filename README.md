# Functional Universe

Modeling the cosmos as a sequence of functional states.

## Overview

FunctionalUniverse is a Python implementation of a universe based on five fundamental axioms that govern state transitions, composition, and causality.

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

Defines the fundamental constants of your universe:

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
# The Universe as a Compositional Sequence of States

Modeling the cosmos as a sequence of functional states.

## 1. Conceptual Framework

We represent the universe as a **sequence of nested states**:

$$
f_0, \quad f_1 = T(f_0), \quad f_2 = T(f_1), \quad \dots
$$

where 

$$
T(f_n)\)
$$

is a **successor function** generating the next state.  

- Each state \(f_n\) encodes the physical properties of the universe at that stage.  
- Observables are functions of the state: \(\mathcal{O}_n = \mathcal{O}(f_n)\).  
- Time is **emergent**, measured as the accumulation of **internal transitions** along worldlines.  
- Each transition between states has a **finite duration** \(d\tau\), reflecting the minimal physically allowed evolution (e.g., energy-limited quantum transitions).  
- The evolution of the universe is **compositional**: each state is fully defined by applying the successor function to the previous state(s), with no reference to an external clock.

### Church Numeral Analogy

This is naturally analogous to **Church numerals**, which encode numbers via **repeated composition**:

$$
f_0 = \{\}, \quad f_1 = \{f_0\}, \quad f_2 = \{f_0, f_1\}, \quad \dots
$$

- Each numeral is a **composition of a function** applied \(n\) times.  
- Likewise, each universe state is a **compositional application** of the successor function, naturally encoding **history and potential branching**.  
- Each composition step is associated with a **transition duration** \(d\tau\), emphasizing that even functional evolution is **physically mediated**.

---

## 2. Successor Function and CMB Cooling Example

We can test this framework with a **quantitative cosmology example**: the cooling of the Cosmic Microwave Background (CMB) after recombination.  

1. **Physical Model**  
After recombination (\(t_0 \sim 3.8 \times 10^5\) years), the CMB temperature evolves as:

$$
T(t) \propto a(t)^{-1}
$$

where \(a(t)\) is the scale factor. In a **matter-dominated universe**:

$$
a(t) \propto t^{2/3} \quad \implies \quad T(t) \propto t^{-2/3}.
$$

2. **Discrete State Steps**  
We define discrete states corresponding to **successor function applications**:

$$
f_n = T_n = T(f_n)
$$

and choose each state step \(n \to n+1\) to correspond to a **doubling of cosmic time**:

$$
t_n = t_0 \cdot 2^n.
$$

Then the temperature at state \(n\) is:

$$
T_n = T_0 \cdot 2^{-2n/3}.
$$

Each state transition is associated with a **minimal transition duration** \(d\tau\), reflecting the time it takes for physical changes to occur in the system.

3. **Initial Conditions**  

$$
T_0 = 3000\,\text{K}, \quad t_0 = 3.8\times 10^5\,\text{yr}.
$$

4. **Successor Function (Discrete Update)**  

$$
f_{n+1} = T(f_n) = f_n \cdot 2^{-2/3} \approx 0.63 f_n
$$

- The factor \(0.63 \approx 2^{-2/3}\) comes from the **matter-dominated temperature scaling**, not an arbitrary number.  
- Each step represents one **compositional application** of the successor function.  
- Each application takes a **finite duration** \(d\tau\).

5. **First Few States**

| n  | t_n (yr)       | T_n (K) |
|----|----------------|---------|
| 0  | 3.80×10⁵       | 3000    |
| 1  | 7.60×10⁵       | 1890    |
| 2  | 1.52×10⁶       | 1190    |
| 3  | 3.04×10⁶       | 750     |
| 4  | 6.08×10⁶       | 470     |
| 5  | 1.22×10⁷       | 296     |
| …  | …              | …       |
| 16 | 2.50×10¹⁰      | 1.9     |

Observation: after ~16 compositional steps, the predicted temperature approaches the observed CMB temperature \(T_{\rm CMB} \approx 2.725\) K.

---

### 3. Emergent Time and Transition Duration

- Each transition \(f_n \to f_{n+1}\) represents a **physically meaningful change**: any evolution of a quantum state into a **distinguishable new state**.  
- Transitions are **not instantaneous**; they take a finite duration \(d\tau_n\), reflecting the **minimal physically allowed evolution** consistent with quantum mechanics and causality.  
- The **accumulated transition durations** along a worldline define operational **proper time**:

$$
\tau_{\rm worldline} = \sum_n d\tau_n
$$

- This formalizes the idea that **time is emergent** — only **composition and transition counting** matter.  
- In this view, **time dilation** arises naturally: systems moving relative to one another, or in different gravitational potentials, accumulate **fewer or more internal transitions per global state**, reproducing the predictions of relativity without invoking a fundamental time parameter.

---

**Key Insights**

1. The universe evolves **compositionally**, via repeated application of a successor function \(T\).  
2. Church numeral analogy makes **nested, history-dependent evolution** intuitive.  
3. Each transition has a **finite duration \(d\tau\)**, giving rise to emergent **proper time**.  
4. Discrete functional evolution reproduces **real cosmological observables**, like the cooling of the CMB.  
5. **Time dilation** and **spacetime geometry** naturally emerge from **transition counting** and compositional structure.

---

## References

1. Margolus, N., & Levitin, L. B. "The maximum speed of dynamical evolution." *Physica D*, 1998.  
2. Peebles, P. J. E. *Principles of Physical Cosmology*, 1993.  
3. Sorkin, R. "Causal sets: Discrete gravity," 2003.  

