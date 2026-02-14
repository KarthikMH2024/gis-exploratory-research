# ============================================================
# Phase 1 – Visual GIS Foundations Exploration
# Focus: Vector vs Raster Representation
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# ============================================================
# 1. VECTOR MODEL VISUALIZATION
# ============================================================

print("\n--- VECTOR MODEL VISUALIZATION ---")

fig1, ax1 = plt.subplots()

# Points (e.g., hospital, school)
hospital = (2, 3)
school = (8, 7)

ax1.scatter(*hospital)
ax1.scatter(*school)

ax1.text(hospital[0], hospital[1], " Hospital")
ax1.text(school[0], school[1], " School")

# Line (e.g., road)
road_x = [hospital[0], school[0]]
road_y = [hospital[1], school[1]]
ax1.plot(road_x, road_y)

# Polygon (e.g., district boundary)
district = Polygon([(4,1), (9,2), (7,6), (3,5)], fill=False)
ax1.add_patch(district)

ax1.set_title("Vector Representation (Points, Line, Polygon)")
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_aspect('equal')
plt.show()


# ============================================================
# 2. RASTER MODEL VISUALIZATION
# ============================================================

print("\n--- RASTER MODEL VISUALIZATION ---")

# Create 2D grid surface (e.g., elevation)
x = np.linspace(0, 10, 50)
y = np.linspace(0, 10, 50)
X, Y = np.meshgrid(x, y)

# Simulated elevation surface
Z = np.sin(X/2) + np.cos(Y/3)

plt.figure()
plt.imshow(Z, extent=(0,10,0,10), origin='lower')
plt.colorbar(label="Raster Value")
plt.title("Raster Representation (Continuous Surface Grid)")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.show()


# ============================================================
# 3. VISUAL COMPARISON – VECTOR vs RASTER
# ============================================================

print("\n--- VISUAL COMPARISON ---")

fig, (ax_vec, ax_ras) = plt.subplots(1, 2, figsize=(12, 5))

# --- Vector Side ---
ax_vec.scatter(*hospital)
ax_vec.scatter(*school)
ax_vec.plot(road_x, road_y)
ax_vec.add_patch(Polygon([(4,1), (9,2), (7,6), (3,5)], fill=False))

ax_vec.set_title("Vector Model")
ax_vec.set_xlim(0, 10)
ax_vec.set_ylim(0, 10)
ax_vec.set_aspect('equal')

# --- Raster Side ---
ax_ras.imshow(Z, extent=(0,10,0,10), origin='lower')
ax_ras.set_title("Raster Model")
ax_ras.set_xlabel("X")
ax_ras.set_ylabel("Y")

plt.tight_layout()
plt.show()


# ============================================================
# END
# ============================================================

print("\nVisual comparison complete.")