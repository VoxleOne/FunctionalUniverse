## Current Standing: A "Single Worldline" Simulation

We have successfully implemented a **0-dimensional, linear time** version of our Functional Universe. The code rigorously enforces the axioms for a single sequence of events.

1.  **Axiom 1 (Composition)**: Implemented. `Transition` objects wrap Python functions and can be composed mathematically `f(g(x))` and physically (summing entropy/duration).

2.  **Axiom 2 (Min Duration)**: Enforced. The `Universe` rejects any transition where `duration < dt_min`.

3.  **Axiom 3 (Entropy)**: Enforced. Entropy is tracked and strictly non-decreasing (monotonic).

4.  **Axiom 4 (Causality)**: Partially Implemented. Currently, causality is represented as a **Total Order** (a single list: $t_1 \to t_2 \to t_3$). In physics, causality is a **Partial Order** (a Directed Acyclic Graph). This means currently, *everything* blocks *everything else*. There is no concept of "spatial separation" where two events can happen independently.

5.  **Axiom 5 (Speed limit $c$)**: Implemented as a "Rate Limit". The code correctly calculates if a sequence of transitions happens "too fast" for the physical limits allowed.

### The Missing Piece: Emergent Space

The axioms suggest that "Locality is emergent" and "Causal cones are inevitable." However, the current Python implementation processes a single global `state`.

*   **Current State:** `state = f_n( ... f_1(f_0) )`. This is one particle or one observer's clock.
*   **Target State:** A network where multiple transitions can happen "in parallel" (logically) if they don't depend on each other's outputs.

## Proposed Next Steps

To demonstrate the power of these axioms, we are working to move from a Linear Time framework to a Causal Graph (DAG) representation. In this extended framework, we introduce a function aggregation layer that allows us to model non-sequential quantum phenomena such as superposition and entanglement.

1.  **Refactor `Universe` to support Partial Ordering**:
    Instead of a single `current_state`, the universe should track a **Frontier** of states.
    *   *Linear:* Transition A -> Transition B -> Transition C
    *   *Causal Graph:* Transition A splits into B and C (which are independent). B and C merge into D.
    *   *Why?* This creates "Space". The "distance" between B and C is defined by how far back their common ancestor (A) is.

2.  **Concrete "Matter" Simulation**:
    We need a concrete state to visualize "stabilized patterns" (Axiom 1).
    *   *Idea:* Use a simple **Bit Grid** or **Graph Node** as the state.
    *   Define a transition that "moves" a bit of information.
    *   If we run this, we should see "light cones" (speed limits) appearing naturally in the grid without us programming them explicitly, just by enforcing Axiom 5.

3.  **Visualizer**:
    A simple script to plot the `Transition` history as a graph.
    *   Nodes = States
    *   Edges = Transitions (weighted by duration)
    *   Hopefully this will visually show that **Time is emergent** (longest path length) and **Space is emergent** (separation in the graph).
