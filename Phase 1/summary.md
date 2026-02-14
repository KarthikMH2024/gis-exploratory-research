# Phase 1 – Conceptual and Computational Foundations of GIS

## 1. Representation of Discrete Geographic Entities (Vector Model)

The first part of the exploration revolves around the vector model, which describes geographic space as composed of discrete and well-defined objects. In the vector model, spatial reality is represented as geometric objects:

- Points represent fixed locations (e.g., cities, facilities).
- Lines represent linear features (e.g., rivers, roads, corridors).
- Polygons represent spatial regions (e.g., agricultural areas, administrative boundaries).

As represented in the implemented simulation:

- Two cities are represented as points defined by their coordinates.
- A river is represented as a polyline defined by a series of vertices.
- An agricultural zone is represented using a closed polygon.

The representation of geographic space as objects with well-defined boundaries and geometry corresponds with the object-oriented representation of geographic space in vector GIS systems.

The vector model enables computation of:

- Euclidean distance (direct geometric distance between two points)
- Path-based distance (distance along a constrained route or network)
- Spatial relationships (intersection, containment, adjacency)

If we compare the direct Euclidean distance and the segmented path distance, we observe that the vector model allows reasoning about constrained movement, such as along roads or river crossings. This demonstrates the vector model’s support for network-based reasoning.

The vector model allows us to conceptualize questions such as:

- How are places connected?
- What is the shortest path?
- Do two places intersect?

The vector model views space as a set of distinct objects that interact.

---

## 2. Representation of Continuous Spatial Phenomena (Raster Model)

The second component shifts to the raster model, which treats space not as a set of objects but as a continuous plane.

In this approach:

- Space is divided into a grid of equal-sized cells.
- Each cell contains a value representing a spatial attribute.
- Resolution (number and size of grid cells) determines the level of detail.

In the simulation:

- A land suitability surface is mathematically derived.
- Each cell in the grid contains a suitability index influenced by spatial gradients and variation patterns.
- Two resolutions are compared:
  - High-resolution grid (fine detail)
  - Low-resolution grid (coarse representation)

This demonstrates a key principle of raster GIS: spatial resolution directly affects analytical precision.

- In low-resolution representation, spatial detail is lost.
- In high-resolution representation, spatial variability becomes visible.

Unlike the vector model, raster boundaries are not sharply defined. Instead, gradual changes across space are captured.

The raster model is well-suited for applications such as:

- Environmental modelling
- Temperature distribution analysis
- Pollution mapping
- Elevation modelling

Conceptually, the raster model addresses questions such as:

- Where are high-intensity areas located?
- How does intensity change across space?
- Where do spatial clusters emerge?

---

## 3. Spatial Dependence and Neighborhood Effects

A foundational principle of GIS is spatial autocorrelation, or spatial dependence. Spatial observations are not independent of one another.

In the simulation:

- A reference point is selected.
- Random points are generated around the reference point.
- A comparison is made between near and far values.

The result illustrates the principle:

Near things are more related to each other than distant things.

Spatial dependence violates the assumption of independence central to classical statistics.

In spatial systems:

- Proximity influences similarity.
- Interaction declines with distance.
- Behavior and attributes exhibit spatial structure.

Distance and neighborhood effects are therefore fundamental to spatial reasoning.

---

## 4. Structural Insights from Phase 1

Through computational experimentation, the following foundational principles of GIS become evident:

1. Space can be represented as discrete objects (vector model).
2. Space can be represented as continuous fields (raster model).
3. Resolution and representation influence interpretation.
4. Distance functions as a core interaction metric.
5. Spatial proximity influences similarity and behavior.

The distinction between vector (object-based) and raster (field-based) models extends beyond representation. The choice of representation determines:

- The type of analysis possible
- The computational approach
- The interpretation of results
- The theoretical assumptions embedded in the model

Representation shapes reasoning.

---

## 5. Transition Toward Mathematical Formalization

With Phase 1 established, the foundational terminology and conceptual structure of GIS are defined.

The next phase of the repository will focus on methodological and mathematical development. The objectives include:

- Understanding formal spatial relations
- Representing weighted edges in network graphs
- Modelling distance-based interactions
- Exploring spatial optimization techniques

The goal is to transition from conceptual understanding to structured analytical frameworks, incorporating methodological rigor and potential innovation.
