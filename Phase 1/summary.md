## Understanding Core Spatial Representations in GIS

In studying Geographic Information Systems (GIS), two primary models emerge as foundational approaches to representing and analyzing geographic data: **Vector** and **Raster** models. Each serves a distinct analytical purpose and influences how spatial problems are formulated and solved.

---

## Vector Model

The vector model represents space using discrete geometric primitives:

- **Vertices (points)** – defined by coordinate pairs  
- **Edges (lines)** – formed by connecting vertices  
- **Polygons** – closed shapes formed by connected edges  

This model emphasizes **explicit spatial structure and relationships**. It is particularly suitable when analysis depends on:

- Pathfinding  
- Connectivity  
- Network optimization  
- Boundary definition  
- Infrastructure modeling  

For example:

If two cities, A and B, are separated by a river and surrounded by fertile agricultural land, a vector-based model allows us to:

- Represent the river as a line feature  
- Represent cities as point features  
- Represent agricultural zones as polygons  
- Compute optimal paths avoiding constraints  
- Analyze connectivity and access routes  

In essence, the vector model is object-oriented. It treats geographic space as a collection of distinct entities with defined boundaries and relationships.

---

## Raster Model

In contrast, the raster model represents space as a continuous grid of equally sized cells (pixels). Each cell stores a value corresponding to a spatial variable.

This model emphasizes **field-based representation** rather than discrete objects.

It is particularly effective for:

- Heatmaps  
- Elevation models  
- Pollution dispersion  
- Land suitability analysis  
- Environmental modeling  

For example:

If land is divided into a grid, each cell can store a suitability score for crop growth. By visualizing the grid as a surface or heatmap, we can identify:

- High-potential agricultural zones  
- Low-productivity regions  
- Spatial gradients and clusters  

Unlike vectors, rasters do not focus on boundaries or paths. Instead, they focus on **continuous variation across space**.

---

## Conceptual Distinction

The fundamental difference can be summarized as:
![Vector vs Raster](images/vector_raster_comparison.png)

- **Vector → Object-based spatial representation**
- **Raster → Field-based spatial representation**

Vectors model *things*.  
Rasters model *conditions*.

Understanding this distinction is critical, as the choice between vector and raster fundamentally shapes how a geographic problem is framed, analyzed, and interpreted.
