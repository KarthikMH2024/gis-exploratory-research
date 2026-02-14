import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from scipy.spatial.distance import cdist


# ------------------------------------------------------------------
# Urban object geometry (vector representation)
# ------------------------------------------------------------------

city_A = np.array([1.5, 2.0])
city_B = np.array([8.5, 7.0])

river_path = np.array([
    [2.0, 8.5],
    [3.5, 6.2],
    [5.0, 4.5],
    [6.5, 3.0],
    [8.0, 1.5]
])

agri_zone = np.array([
    [3.0, 1.0],
    [7.0, 1.2],
    [6.2, 4.0],
    [2.8, 3.8]
])


fig, ax = plt.subplots()

ax.scatter(*city_A, s=70)
ax.scatter(*city_B, s=70)
ax.plot(river_path[:, 0], river_path[:, 1], linewidth=1.6)
ax.add_patch(Polygon(agri_zone, fill=False))

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect("equal")
ax.set_title("Vector Representation: Discrete Geographic Entities")

plt.show()


# ------------------------------------------------------------------
# Continuous land suitability surface (raster representation)
# ------------------------------------------------------------------

def generate_surface(resolution):
    x = np.linspace(0, 10, resolution)
    y = np.linspace(0, 10, resolution)
    X, Y = np.meshgrid(x, y)

    suitability = (
        np.exp(-((X - 5.5)**2 + (Y - 5.0)**2) / 8.0)
        - 0.25 * np.cos(X)
        + 0.15 * np.sin(Y * 1.2)
    )

    return suitability


high_res_surface = generate_surface(120)
low_res_surface = generate_surface(25)


plt.figure()
plt.imshow(high_res_surface, extent=(0, 10, 0, 10), origin="lower")
plt.title("Raster Representation (High Resolution)")
plt.colorbar(label="Suitability Index")
plt.show()


plt.figure()
plt.imshow(low_res_surface, extent=(0, 10, 0, 10), origin="lower")
plt.title("Raster Representation (Low Resolution)")
plt.colorbar(label="Suitability Index")
plt.show()


# ------------------------------------------------------------------
# Spatial dependence intuition (neighbor similarity)
# ------------------------------------------------------------------

center_point = np.array([[5.0, 5.0]])
random_points = np.random.uniform(0, 10, size=(40, 2))

distances = cdist(center_point, random_points)[0]
near_mask = distances < 2.0

near_values = np.exp(-distances[near_mask])
far_values = np.exp(-distances[~near_mask])

print("Average value near center:", np.mean(near_values))
print("Average value far from center:", np.mean(far_values))


# ------------------------------------------------------------------
# Distance comparison (Euclidean vs path segmentation)
# ------------------------------------------------------------------

direct_distance = np.linalg.norm(city_A - city_B)

path_segments = np.vstack([city_A, river_path, city_B])
segmented_distance = np.sum(
    np.linalg.norm(path_segments[1:] - path_segments[:-1], axis=1)
)

print("Direct Euclidean distance:", round(direct_distance, 2))
print("Distance following segmented path:", round(segmented_distance, 2))
