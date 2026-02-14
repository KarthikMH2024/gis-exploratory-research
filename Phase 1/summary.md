# Phase 1 – Conceptual and Computational Foundations of GIS

## 1. Representation of Discrete Geographic Entities (Vector Model)

The first part of the exploration revolves around the vector model, which describes geographic space as composed of discrete and well-defined objects. In the vector model, spatial reality is represented as geometric objects:

* Points are used to represent fixed locations, like cities and facilities.
* Lines are used to represent linear features, like rivers, roads, and corridors.
* Polygons are used to represent spatial regions, like agricultural areas and administrative boundaries.

As represented in the implemented simulation, two cities are represented as points defined by their coordinates. A river is represented as a polyline, with the river defined by a series of vertices. Let’s assume that the agricultural zone is represented with the help of a closed polygon.

The representation of geographic space as objects with well-defined boundaries and geometry corresponds with the object-oriented representation of geographic space in vector GIS systems. The ability of the vector model to compute the distance between locations, referred to as the "Euclidean" distance, as well as the ability of the vector model to compute the path between locations, referred to as the "Path-based" distance, and the ability of the vector model to compute spatial relationships between objects.

The key insight here is that if we compare the direct Euclidean distance and the segmented path distance, we note that the vector model allows us to reason about the movement of objects in a constrained path, like roads or river crossings. This is another example of the vector model supporting network-based reasoning. The vector model also allows us to conceptualize questions like: How are places connected? What is the shortest path? Do two places intersect? The vector model views space as a set of distinct objects that interact.

---

## 2. Representation of Continuous Spatial Phenomena (Raster Model)

The second component shifts to the raster model, which treats space not as a set of objects but as a continuous plane as one. In this approach, the continuous plane can be abstracted into the following geometric primitives:

* Spaces are divided into a grid of equal-sized cells.
* Each cell contains a value, which is a representation of a spatial attribute.
* Resolution, or the number of grid cells, determines detail.

In this simulation, a land suitability surface is mathematically derived. Each cell in a grid contains a suitability index, which is affected by spatial gradients and variation patterns. Two resolutions are being compared as High-resolution grid(fine detail) or a low-resolution grid(coarse representation).

This is another important principle of the Raster GIS. Spatial resolution has a direct effect on the precision of the analysis. In the low-resolution representation, the spatial detail is missing. In the high-resolution representation, the spatial inconsistency is visible.

In the Raster model, the boundaries are not present as in the vector model. Instead, the gradual changes are captured. The Raster model is best suited for use cases like Environmental modelling, Temperature scattering, Polluted Regions, Elevation modelling, etc.

The conceptual model of the Raster model is to find answers to where high intensity areas are present, how the intensity changes, or what the spatial clusters are.

---

## 3. Spatial Dependence and Neighborhood Effects

One of the theoretical bases of GIS is spatial autocorrelation or the principle of spatial dependence(In other words, the spatial observations are not independent of each other). The simulation above illustrates this principle. A reference point is chosen, then random points are created around the reference point, and finally, A comparison is made between near and far values.

The above simulation shows that near values are more similar to each other than far values. This is based on the following principle.

Near things are more related to each other than distant things.

Spatial dependence violates the assumption of independence that is central to classical statistics. In the spatial world, proximity is an important determinant of similarity, interaction, and behaviour.

---

## 4. Structural Insights from Phase 1

With computational experimentation, the following foundational presumptions of GIS become apparent:

1. Space can be represented as discrete objects (vector).

2. Space can be represented as continuous fields (raster).

3. Resolution and representation play a role in interpretation.

4. Distance tends to play an important role as an interaction metric.

5. Spatial proximity tends to play an important role in determining similarity.

It’s not just that vector representation is object-based, and raster representation is field-based. It’s more than the choice between these representations, and the implications that choice holds, determines: The type of analysis that’s possible, the computational approach, the interpretation, And The theory.

---

## 5. Transition Toward Mathematical Formalization

After having established phase 1, this helps in providing an outline of some basic terminologies commonly used in GIS. Now, after these concepts, I plan to move towards the next phase of the repository. The next objectives include understanding the right methods involved and incorporating change to make it novel and innovative. I plan to understand Spatial relations, Representing Weighted edges in Network graphs, Distance-based interactions, and spatial optimizations.
