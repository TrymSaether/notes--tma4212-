import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Although not used directly, this import is needed for 3D plotting

# Set up the figure and 3D axis
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Parameters for the domain and time interval
T = 3.0  # maximum time for visualization
x_min, x_max = 0, 1

# Plot the spatial domain boundaries along time.
# We plot vertical lines along the time axis at x=0 and x=1.
ts = np.linspace(0, T, 50)
zeros = np.zeros_like(ts)
ones = np.ones_like(ts)
# Here, we plot a line (with a dummy third coordinate set to 0) for each boundary.
ax.plot(np.full_like(ts, x_min), ts, zeros, 'r-', lw=3, label=r'$x=0$ boundary')
ax.plot(np.full_like(ts, x_max), ts, zeros, 'b-', lw=3, label=r'$x=1$ boundary')

# For illustration, add a simple surface representing a “solution” u(x,t)
# (This is only to add a third dimension and is not essential for the boundary discussion.)
x_vals = np.linspace(x_min, x_max, 50)
T_vals = np.linspace(0, T, 50)
X, Tgrid = np.meshgrid(x_vals, T_vals)
# A dummy solution (e.g. decaying sine wave) — adjust as needed.
U = np.sin(np.pi * X) * np.exp(-0.5 * Tgrid)
ax.plot_surface(X, Tgrid, U, alpha=0.4, cmap='viridis')

# Mark outward normals at the boundaries.
# In 1D, the outward normal at x=0 is -1 (pointing to the left), and at x=1 it is +1 (pointing to the right).
# Since our plot is in (x,t,u) space and u is used for illustration, we show these arrows in the x-direction at a fixed time and u-value.
arrow_length = 0.15
t_arrow = T / 2
u_arrow = 0  # place arrows on the u=0 plane

# At x = 0:
# Outward normal: -1 means that the normal points in the negative x-direction.
ax.quiver(x_min, t_arrow, u_arrow, -arrow_length, 0, 0, color='r', linewidth=2, arrow_length_ratio=0.3)
ax.text(x_min - 0.2, t_arrow, u_arrow, r'$\mathbf{n}=-1$', color='r', fontsize=12)

# At x = 1:
# Outward normal: +1 means that the normal points in the positive x-direction.
ax.quiver(x_max, t_arrow, u_arrow, arrow_length, 0, 0, color='b', linewidth=2, arrow_length_ratio=0.3)
ax.text(x_max + 0.05, t_arrow, u_arrow, r'$\mathbf{n}=+1$', color='b', fontsize=12)

# Annotate the inflow conditions.
# Recall: a boundary is inflow if b(x) · (outward normal) < 0.
# For our assumed scenario:
# - If b(0) > 0, then at x=0 the dot product b(0)*(-1) < 0, so x=0 is inflow.
# - If b(1) < 0, then at x=1 the dot product b(1)*(+1) < 0, so x=1 is inflow.
ax.text(x_min - 0.5, t_arrow + 0.3, u_arrow, 'Dirichlet BC required here\n(if b(0) > 0)', color='r', fontsize=10)
ax.text(x_max + 0.1, t_arrow + 0.3, u_arrow, 'Dirichlet BC required here\n(if b(1) < 0)', color='b', fontsize=10)

# Add a title and axis labels
ax.set_title('3D Visualization of Transport Equation Domain and Inflow Boundaries', fontsize=14)
ax.set_xlabel('Space (x)', fontsize=12)
ax.set_ylabel('Time (t)', fontsize=12)
ax.set_zlabel('Solution (u)', fontsize=12)

# Optionally, add a text annotation for the transport equation itself.
eq_text = r'Transport Equation: $u_t + b(x)u_x = f(x)$'
ax.text(0.5, T + 0.2, np.max(U)*0.8, eq_text, fontsize=12, ha='center')

# Adjust the view angle for a better look
ax.view_init(elev=25, azim=-60)

plt.legend()
plt.tight_layout()
plt.show()
