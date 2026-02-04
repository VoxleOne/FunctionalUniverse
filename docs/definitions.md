---
title: "Definitions"
---
---

# **Functional Universe: Core Definitions**

---

### 1. **Transition $(f)$**

A **transition** is an irreducible physical function that maps one interface (state) to the next:

$$
f_i: S_i \rightarrow S_{i+1}
$$


* Fundamental ontological unit of reality
* Must satisfy minimum proper-time duration $(\Delta \tau \ge d\tau_{\min})$ (Axiom 2)
* Must produce minimum entropy $(\Delta S \ge \Delta S_{\min})$ (Axiom 3)
* Can only influence causally compatible transitions (Axiom 4)


![Functional Universe transition diagram](img/feynman-diagram-transition.png "Transition with aggregation and commitment")



The process begins with an initial state $(f_n)$ interaction. Evolves through an aggregation layer, representing all potential contributions (virtual processes). Ends with a commitment $(f_{n+1})$, which selects one outcome, produces entropy, and advances proper time along the worldline.

---

$$
\underbrace{\text{Initial interaction}}*{\text{left vertex}}
;;\longrightarrow;;
\underbrace{\text{Aggregation / proper-time interval}}*{\text{middle}}
;;\longrightarrow;;
\underbrace{\text{Commitment / output state}}_{\text{right vertex}}
$$

---

Or, using **functional notation** (with transitions $(f)$ and states $(S)$):

$$
S_{\text{in}}
;;\xrightarrow{\text{Initial interaction}};;
\mathcal{A}(\Delta \tau)
;;\xrightarrow{\text{Commitment}};;
S_{\text{out}}
$$

Where:

* $S_{\text{in}}$ = input state (before the transition)
* $\mathcal{A}(\Delta \tau)$ = aggregation layer during proper-time interval $\Delta \tau$
* $S_{\text{out}}$ = committed output state (after the transition)

---

Or, to make it **explicitly functional** like the successor function notation:

$$
f: S_{\text{in}} ;;\mapsto;;
\underbrace{\mathcal{A}(\Delta \tau)}*{\text{aggregation interval}}
;;\mapsto;;
\underbrace{S*{\text{out}}}_{\text{commitment}}
$$

Transitions are where indeterminacy lives: during the aggregation layer ${\mathcal{A}}$, multiple potential paths exist, interfere, or cancel. This is where “God plays dice.”

---

### 2. **State $(S)$**

* A state is a temporary, derived interface between transitions, not a fundamental entity.
* Represents the *record* or *boundary conditions* imposed by prior transitions during a finite interval $d\tau$
* Can be read or affected only through composable transitions
* Serves as a substrate that constrains subsequent transitions, but possesses no independent dynamics
* Exists only as a reference point for ongoing transitions, not as an ontological primitive

---

### 3. **Composability**

Two transitions $(f_i, f_j)$ are **composable** if the output of $(f_i)$ can serve as the input to $(f_j)$:

$$
f_i \circ f_j \quad \text{is defined} \iff S_{i+1} \text{ compatible with } S_j
$$

* Encodes causality (Axiom 4)
* Defines which transitions can influence each other

*The universe evolves through an ongoing chain of irreducible functional compositions; non-determinism arises precisely because quantum aggregations may or may not contribute to each successive composition, altering outcomes without interrupting causal execution.*

---

### 4. **Proper Time $(d\Tau)$**

Proper time is **the measure of accumulated irreducible transitions along a causal chain**:

$$
\tau = \sum_i \Delta \tau_i
$$

* Emergent from transition execution
* Not a background parameter
* Local and invariant along each worldline

*In the Functional Universe framework, the quantity conventionally known as Planck time is reinterpreted as $d_tau$, the minimum duration of an irreducible physical transition. No claim is made that time itself is discrete or that the universe evolves in global ticks; rather, $d_tau$ is a lower bound on local proper-time advancement associated with committed transitions.

---

### 5. **Aggregation Layer**

The **aggregation layer** is the collection of **potential, non-committed transitions**:

* Represents quantum superpositions and virtual processes
* Exists outside proper time until a transition commits
* Provides amplitudes for possible outcomes (analogous to Feynman path integrals)
* Cannot produce entropy or propagate causally until commitment occurs

---

### 6. Parallel Composition

**Parallel Composition** refers to the structural fact that a single committed transition may be supported by multiple, causally compatible aggregation pathways.

Formally, let

$$
\mathcal{A}(f_n) = {(T_i, w_i)}
$$
be the aggregation space associated with interface $f_n$.

Multiple aggregation elements $T_i$ may contribute to the same committed transition $T^*$ if they:

* are mutually compatible,
* reinforce rather than interfere destructively,
* and collectively produce a dominant effective weight (W^* \ge \Theta).

The commitment operator then applies **once**:
$$
f_{n+1} = \mathcal{C}(\mathcal{A}(f_n)) = T^*(f_n)
$$

All contributing aggregation paths **merge at commitment** and do not persist as separate historical events.

**Properties:**

* Parallel composition does **not** produce multiple successor states.
* It does **not** introduce parallel histories or branching worlds.
* It produces a **single irreversible transition** with a single entropy increment and proper-time advance.
* Multiplicity exists only *prior* to commitment.

### Canonical takeaway

> **Aggregation is parallel; composition is serial. Parallel composition names the way multiplicity collapses into one committed transition.**

**Interpretation:**

Parallel composition is analogous to multiple tributaries feeding a single waterfall: many paths converge, but only one irreversible descent occurs.

---

### 7. **Commitment**

A commitment is the irreversible realization of the next causal transition in the compositional chain, advancing proper time by $d\tau& and producing irreducible entropy.

This transition may incorporate compatible aggregation elements, but commitment itself does not depend on aggregation.

* Advances proper time
* Produces irreducible entropy
* Becomes part of the causal chain
* Corresponds to “collapse” or measurement in standard quantum terms

---

### 8. **Observer**

Observers emerge naturally from interaction. Any particle or subsystem becomes an observer the moment it participates in a transition.

* Microscopic observers: single particles registering a change

* Macroscopic observers: sustained sequences of interacting states that retain and propagate information

Observation is thus an emergent property of interaction, not a privileged fundamental entity.

### 9. **Vacuum**

The **vacuum** is an aggregation field :

* Supports non-committed, reversible transitions
* Provides the “substrate” from which transitions can commit
* Responsible for phenomena like Hawking radiation when commitments occur

---

### 10. **Entropy Increment ($(\Delta S)$)**

Each committed transition carries a minimum **entropy increment** $(\Delta S_{\min} > 0)$:

* Records the irreversibility of the transition
* Establishes the arrow of time
* Ensures physical transitions cannot be undone

---

### 11. **Causal Cone**

The **causal cone** of a transition is the set of all transitions that are composable with it, respecting Axiom 5 (maximum causal speed $(c)$):

* Defines emergent locality
* Prevents superluminal influence

---

### 12. **Worldline**

A **worldline** is a causal sequence of committed transitions:

$$
\cdots \rightarrow f_{i-1} \rightarrow f_i \rightarrow f_{i+1} \rightarrow \cdots
$$

* Proper time accumulates along worldlines
* Entropy increases irreversibly
* Local “now” is the frontier of committed transitions along the worldline

---

### 13. **Feynman Diagram Mapping**

A **Feynman diagram** corresponds to a functional universe process:

* Left: prior committed transitions $(f_{n-1}$)
* Middle: aggregation field $( \mathcal{A}(d\tau) )$ representing virtual superpositions
* Right: committed outcome $(f_n)$

> Transition amplitudes are encoded in the aggregation layer; only committed transitions enter physical history.

---

### 14. **Time Machine**

A **time machine** is a hypothetical structure that would allow a transition to influence its own causal past.

* **Forbidden** in the Functional Universe because past transitions are irreversible and cannot be recomposed
* Closed causal loops are non-executable

---

### 15. **Wormhole**

A **wormhole** is a persistent, composable channel connecting distant regions of spacetime (or causal neighborhoods):

* Must obey forward composability
* Must respect entropy increase and maximum causal speed (c)
* Cannot form closed causal loops

---

### 16. **Now**

The **“now”** is the local frontier of **committed transitions** along a worldline:

* There is no global present
* Each worldline may have a distinct “now”
* Emergent from execution, not presupposed

---

This set of definitions **covers the ontology, dynamics, quantum layer, and relativistic constraints** of the Functional Universe.

---