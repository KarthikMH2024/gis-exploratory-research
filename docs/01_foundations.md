# Phase 1 – Foundations of Geographic Information Systems

## 1. Introduction

Geographic Information Systems (GIS) provide a computational framework for representing, storing, analyzing, and modeling spatially referenced data. At its core, GIS integrates geometry, attributes, topology, and spatial relationships into a structured decision-support system.

This phase establishes the theoretical foundations necessary for advanced spatial modeling and later framework development.

---

## 2. Spatial Data Models

Spatial information is represented using two primary data models: vector and raster.

### 2.1 Vector Model

The vector model represents discrete geographic entities using geometric primitives:

- **Points** – zero-dimensional objects (e.g., wells, bus stops)
- **Lines** – one-dimensional features (e.g., roads, rivers)
- **Polygons** – two-dimensional enclosed areas (e.g., land parcels, districts)

Each spatial feature contains:

- Geometry (spatial coordinates)
- Attributes (non-spatial descriptive data)

The vector model is precise and well-suited for network analysis and administrative boundary representation.

---

### 2.2 Raster Model

The raster model represents space as a grid of equally sized cells (pixels). Each cell contains a value representing a spatial attribute.

Common applications include:

- Elevation models
- Satellite imagery
- Temperature distribution
- Land cover classification

Raster models are resolution-dependent. Spatial accuracy varies according to cell size.

---

## 3. Coordinate Reference Systems (CRS)

Spatial data must be defined within a Coordinate Reference System (CRS). A CRS provides a standardized framework for mapping real-world locations onto a computational plane.

Two major types:

- **Geographic CRS** – Uses latitude and longitude (angular measurements).
- **Projected CRS** – Transforms the Earth's curved surface onto a flat coordinate plane.

Projection selection introduces distortion trade-offs involving:

- Area
- Distance
- Shape
- Direction

Understanding projection theory is critical for maintaining spatial accuracy.

---

## 4. Topology in GIS

Topology defines spatial relationships independent of exact coordinates.

Key topological relationships include:

- **Adjacency** – Two polygons share a boundary.
- **Connectivity** – Lines intersect or form networks.
- **Containment** – One object lies within another.
- **Overlap** – Spatial intersection between features.

Topological modeling ensures data integrity and enables network-based spatial reasoning.

---

## 5. Spatial Autocorrelation

Spatial autocorrelation describes the principle that spatial phenomena are not randomly distributed.

Foundational principle:

> Near things tend to be more related than distant things.

Spatial autocorrelation can be:

- Positive – Similar values cluster together.
- Negative – Dissimilar values are adjacent.
- Neutral – Random spatial distribution.

Quantitative measurement is typically conducted using spatial statistics such as Moran’s I and Geary’s C.

This concept challenges the assumption of independent observations in classical statistical models.

---

## 6. Spatial Resolution and Scale

Spatial analysis outcomes depend heavily on scale and resolution.

- **Resolution** refers to the smallest measurable unit (e.g., raster cell size).
- **Scale** influences generalization and abstraction.
- **Modifiable Areal Unit Problem (MAUP)** highlights how results change depending on aggregation boundaries.

Spatial modeling must account for scale sensitivity.

---

## 7. Foundational Assumptions of Traditional GIS

Traditional GIS frameworks often assume:

- Static spatial structures
- Crisp, well-defined boundaries
- Distance as a primary measure of interaction
- Deterministic relationships between spatial entities

These assumptions form the baseline for later critique and theoretical extension in Phase 3.

---

## 8. Summary

Phase 1 establishes the structural components of GIS:

- Spatial representation (vector and raster)
- Reference systems and projections
- Topological relationships
- Spatial dependence principles
- Scale and resolution considerations

This foundation enables the transition toward mathematical formalization and advanced spatial modeling in subsequent phases.
