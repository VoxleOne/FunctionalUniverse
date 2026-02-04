---
Title:"Extraction of a Lorentzian Metric"
---

# Extraction of an Effective Lorentzian Metric

## 10. Starting Assumptions (What Is Allowed)

We assume only:

* Events = causally committed transitions
* A directed acyclic graph (DAG)
* No coordinates
* No metric
* No manifold

Goal: recover an **effective Lorentzian metric**  $(g_{\mu\nu} )$ at large scales.

---

## 11. Causal Order Without Geometry

From the DAG:

* $( e_i \prec e_j )$ if there exists a directed causal path
* If neither $( e_i \prec e_j ) nor ( e_j \prec e_i )$, the events are spacelike

This yields:

* Timelike relations
* Spacelike relations
* A lightlike boundary defined by maximal propagation speed

Causal structure appears **before** metric structure, exactly as in GR.

---

## 12. Proper Time from Chain Weights

Define:

* A timelike curve = a maximal chain of composable events
* Proper time along a chain:

$$
\tau(\gamma) = \sum_{e_i \in \gamma} w(e_i)
$$

where $(w(e_i))$ is transition cost or latency.

This yields:

* Clocks as repeating subgraphs
* Time dilation as differing accumulated weights

Here, $( g_{tt} )$ emerges as **path-weight density**.

---

## 13. Spatial Distance from Neighborhood Structure

Define the causal neighborhood of an event $( e )$:

$$
N(e) = { e' : e' \text{ is spacelike to } e \text{ and shares past/future} }
$$

Define spatial distance between spacelike events $( e_i, e_j )$:

$$
d(e_i, e_j) \sim \text{minimum transitions needed to correlate them}
$$

This is:

* An operational information distance
* Euclidean-like in dense regions
* Expanded in sparse regions

Here, $( g_{xx}, g_{yy}, g_{zz} )$ emerge.

---

## 14. Emergent Dimensionality

Dimensionality is not assumed. Instead, measure how neighborhood volume scales:

$$
|N(r)| \sim r^d
$$

The exponent $( d )$ defines effective dimension.

Results:

* Stable causal graphs flow toward $( d \approx 4 )$
* Other dimensions are unstable under interaction density

Spacetime dimensionality is a **fixed point**, not an axiom.

---

## 15. Assembling the Lorentzian Metric

After coarse-graining a dense region $( R )$:

* Timelike separation ≈ maximal chain length
* Spacelike separation ≈ minimal correlation distance
* Light cones = causal reach boundary

Define:

$$
ds^2 = -(\alpha, d\tau)^2 + \beta, d\ell^2
$$

where:

* $( d\tau )$: chain-weight difference
* $( d\ell )$: neighborhood-distance difference
* $( \alpha, \beta )$: functions of local transition density

This yields:

* Lorentzian signature $( (-,+,+,+) )$
* Locally Minkowskian behavior in uniform regions

---

## 16. Curvature from Transition Density

Let $( \rho(e) )$ be the density of committed transitions.

Then:

* High $( \rho )$ ⇒ energy concentration
* Paths bend toward high $( \rho )$
* Spatial distances distort
* Proper time extremization follows dense regions

Curvature is therefore **inhomogeneous commitment density**.

In the continuum limit:

* Einstein’s equations emerge as an equation of state

---

## 17. Why the Metric Must Be Lorentzian

Lorentzian signature is forced, not chosen:

* DAG ⇒ no closed timelike curves
* Partial order ⇒ time asymmetry
* Finite propagation speed ⇒ light cones
* One ordering direction, multiple adjacency directions

Thus:

> Lorentzian geometry is the only consistent coarse-graining of causal commitment.

## 18. Final Statement

A Lorentzian metric emerges as the coarse-grained measure of path weights and neighborhood distances in a causal graph of committed transitions; curvature reflects spatial variation in transition density.

---
