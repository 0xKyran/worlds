import numpy as np
from noise import pnoise2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Generate the height map
def generate_height_map(size, scale):
    height_map = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            height_map[i][j] = pnoise2(i/scale, j/scale)
    return height_map

# Step 2: Convert the height map to a 3D mesh
def height_map_to_3d_mesh(height_map, scale=10):
    size = height_map.shape[0]
    X, Y = np.meshgrid(range(size), range(size))
    Z = height_map * scale
    return X, Y, Z

# Step 3: Visualize the 3D mesh in an isometric view with pastel colors
def plot_isometric_view(X, Y, Z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Customize the colors and view
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.cividis(Z), rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False)

    # Set pastel colors
    ax.xaxis.set_pane_color((0.95, 0.95, 0.95, 1.0))
    ax.yaxis.set_pane_color((0.95, 0.95, 0.95, 1.0))
    ax.zaxis.set_pane_color((0.95, 0.95, 0.95, 1.0))
    
    # Remove grid lines
    ax.grid(False)

    # Set isometric view
    ax.view_init(30, 45)
    
    plt.axis('off')  # Turn off the axis
    plt.show()

# Main execution
size = 100
scale = 10.0
height_map = generate_height_map(size, scale)
X, Y, Z = height_map_to_3d_mesh(height_map)
plot_isometric_view(X, Y, Z)
