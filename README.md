# The Universe as a Compositional Sequence of States

Modeling the cosmos as a sequence of functional states.

## 1. Introduction

Traditionally, physics treats time as a fundamental parameter: events unfold within a pre-existing temporal framework. Here, we explore an alternative:

- The universe is a **sequence of nested states**.  
- **Time emerges** from the succession of states, rather than existing independently.  

$$
f_{n+1} = T(f_n)
$$

--

## 2. Axioms

### Axiom 1 — Functional Ontology
The universe is a compositional structure of functions. What exists fundamentally are compositions of transitions, not states or objects. Formally:

$$
fi​:(Si​→Si+1​)↦(Si+1​→Si+2​) 
$$

Consequence
- “Things” are stabilized patterns of transitions
- States are interfaces, not ontological primitives

### Axiom 2 — Minimal Transition Duration
There exists a universal, nonzero lower bound dτmin​ on the duration of any irreducible physical transition. 

_The value of this bound is an empirical parameter to be constrained by observation, not fixed by the axioms themselves._

Consequence
- No instantaneous change
- No infinite rates
- Zeno paradoxes are impossible
- Time must be emergent and discrete at base

### Axiom 3 — Entropy as Physical Quantity
Every irreducible transition carries a minimum entropy ΔSmin​ (e.g. one bit).

Consequence
- Energy = entropy flow rate
- Irreversibility is fundamental
- Arrow of time is built in
- Decoherence is not optional

### Axiom 4 — Causality as Composability
Causality is the ordered composability of transitions; only composable transitions can influence each other.

Consequence
- Causal structure precedes geometry
- Locality is emergent
- Causal cones are inevitable

### Axiom 5 — Invariant Speed of Causality
The minimum transition duration implies a universal upper bound on causal composition, denoted c, which is invariant.

Consequence
- Lorentz symmetry is forced
- No preferred frame
- c cannot vary without breaking causality

---

## 3. Conceptual Framework

We represent the universe as a sequence of nested states:

$$
f_0, \quad f_1 = T(f_0), \quad f_2 = T(f_1), \quad \dots
$$

where 

$$
T(f_n)
$$

is a **successor function** generating the next state.  

- Each state $(f_n)& encapsulates the physical properties of the universe at step $(n)$, and a **successor function** \(T\) generates the next state:
- Observables are functions of the state: $(\mathcal{O}_n = \mathcal{O}(f_n))$.  
- Time is **emergent**, measured as the accumulation of **internal transitions** along worldlines.  
- Each transition between states has a **finite duration** $(d\tau$), reflecting the minimal physically allowed evolution (e.g., energy-limited quantum transitions).  
- The evolution of the universe is **compositional**: each state is fully defined by applying the successor function to the previous state(s), with no reference to an external clock.

###  Note: Church Numeral Analogy

We can represent sequential states and their compositions using concepts analogous to Church numerals in lambda calculus. Each state can be seen as a function of the previous state, and iteration over these functions mirrors the counting structure of Church numerals. 

**Disclaimer**: this analogy is purely mathematical and conceptual. It is not a claim about metaphysics, consciousness, or the universe literally being a computer. The purpose is to illustrate formal compositional structure in state evolution, not to make ontological or physical assertions about reality.

$$
f_0 = \{\}, \quad f_1 = \{f_0\}, \quad f_2 = \{f_0, f_1\}, \quad \dots
$$

- Each numeral is a **composition of a function** applied $(n)$ times.  
- Likewise, each universe state is a **compositional application** of the successor function, naturally encoding **history and potential branching**.  
- Each composition step is associated with a **transition duration** $(d\tau)$, emphasizing that even functional evolution is **physically mediated**.

---

## 4. Application Examples

### 4.1. Successor Function and CMB Cooling Example

We can test this framework with a quantitative cosmology example: the cooling of the Cosmic Microwave Background (CMB) after recombination.  

1. **Physical Model**  
After recombination $(\(t_0 \sim 3.8 \times 10^5\) years)$, the CMB temperature evolves as:

$$
T(t) \propto a(t)^{-1}
$$

where $(a(t))$ is the scale factor. In a matter-dominated universe::

$$
a(t) \propto t^{2/3} \quad \implies \quad T(t) \propto t^{-2/3}.
$$

2. **Discrete State Steps**  
We define discrete states corresponding to successor function applications:

$$
f_n = T_n = T(f_n)
$$

and choose each state step $(n \to n+1)$ to correspond to a **doubling of cosmic time**:

$$
t_n = t_0 \cdot 2^n.
$$

Then the temperature at state $(n)$ is:

$$
T_n = T_0 \cdot 2^{-2n/3}.
$$

Each state transition is associated with a **minimal transition duration** $(d\tau)$, reflecting the time it takes for physical changes to occur in the system.

3. **Initial Conditions**  

$$
T_0 = 3000\,\text{K}, \quad t_0 = 3.8\times 10^5\,\text{yr}.
$$

4. **Successor Function (Discrete Update)**  

$$
f_{n+1} = T(f_n) = f_n \cdot 2^{-2/3} \approx 0.63 f_n
$$

- The factor $(0.63 \approx 2^{-2/3})$ comes from the **matter-dominated temperature scaling**, not an arbitrary number.  
- Each step represents one **compositional application** of the successor function.  
- Each application takes a **finite duration** $(d\tau)$.

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

Observation: after ~16 compositional steps, the predicted temperature approaches the observed CMB temperature $(T_{\rm CMB} \approx 2.725)$ K.

---

### 4.2.. Emergent Time and Transition Duration

- Each transition $(f_n \to _{n+1})$ represents a physically meaningful change: any evolution of a quantum state into a distinguishable new state
- Transitions are not instantaneou; they take a finite duration $(d\tau_n)$, reflecting the minimal physically allowed evolutio consistent with quantum mechanics and causality.
- The  accumulated transition durations along a worldline define operational proper time:

$$
\tau_{\rm worldline} = \sum_n d\tau_n
$$

- This formalizes the idea that time is emergent; only **composition and transition counting** matter.  
- In this view, **time dilation** arises naturally: systems moving relative to one another, or in different gravitational potentials, accumulate **fewer or more internal transitions per global state**, reproducing the predictions of relativity without invoking a fundamental time parameter.

---

**Key Insights**

1. The universe evolves **compositionally**, via repeated application of a successor function $(T)$.  
2. Church numeral analogy makes **nested, history-dependent evolution** intuitive.  
3. Each transition has a **finite duration** $(d\tau)$, giving rise to emergent **proper time**.  
4. Discrete functional evolution reproduces **real cosmological observables**, like the cooling of the CMB.  
5. **Time dilation** and **spacetime geometry** naturally emerge from **transition counting** and compositional structure.

---

## References

1. Margolus, N., & Levitin, L. B. "The maximum speed of dynamical evolution." *Physica D*, 1998.  
2. Peebles, P. J. E. *Principles of Physical Cosmology*, 1993.  
3. Sorkin, R. "Causal sets: Discrete gravity," 2003.  

