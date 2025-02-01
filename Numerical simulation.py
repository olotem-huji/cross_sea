import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


plt.style.use("physrev.mlpstyle")

DEG_TO_RAD = np.pi / 180
l_angle = 120 * DEG_TO_RAD
r_angle = - l_angle
# r_angle = -90 * DEG_TO_RAD


# Define wave parameters
wavelength = 2  # Normalized wavelength
k = 2 * np.pi / wavelength  # Wave number
L = 10  # Domain size
N = 200  # Grid resolution
border_length = 20

t = 0  # Initial time step
t_values = np.linspace(0, 1000, 5)
x = np.linspace(-L, L, N)
y = np.linspace(-L, L, N)
X, Y = np.meshgrid(x, y)

# Define wave components from three reflection angles (0, +60, -60 degrees)
# k1 = np.array([k, 0])  # Incident wave
# k2 = np.array([k * np.cos(l_angle), k * np.sin(l_angle)])  # Reflected at +60 deg
# k3 = np.array([k * np.cos(r_angle), k * np.sin(r_angle)])  # Reflected at -60 deg

k1 = np.array([0, k])  # Incident wave
k2 = np.array([k * np.sin(l_angle), k * -np.cos(l_angle)])  # Reflected at +60 deg
k3 = np.array([k * np.sin(r_angle), k * -np.cos(r_angle)])  # Reflected at -60 deg

# Compute wave interference
wave1 = np.cos(k1[0] * X + k1[1] * Y - t)
wave2 = np.cos(k2[0] * X + k2[1] * Y - t)
wave3 = np.cos(k3[0] * X + k3[1] * Y - t)

# Superposition of waves
wave_pattern = wave1 + wave2 + wave3

# l_border = np.linspace([-L, L], N) * np.array([np.cos(l_angle), np.sin(l_angle)])
# print(l_border)

# Plot the standing wave pattern
fig, ax = plt.subplots(figsize=(8, 8))
c = ax.contourf(X, Y, wave_pattern, levels=50, cmap='RdBu')
# plt.plot(l_border)
plt.colorbar(c, ax=ax, label='Wave Amplitude')
ax.set_title("Hexagonal Standing Wave Pattern with Triangle Border")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

def update(t):
    wave1 = np.cos(k1[0] * X + k1[1] * Y - t)
    wave2 = np.cos(k2[0] * X + k2[1] * Y - t)
    wave3 = np.cos(k3[0] * X + k3[1] * Y - t)

    # Superposition of waves
    wave_pattern = wave1 + wave2 + wave3
    for collection in ax.collections:
        collection.remove()
    c = ax.contourf(X, Y, wave_pattern, levels=50, cmap='RdBu')

    return c.collections

ani = FuncAnimation(fig, update, frames=t_values, interval=50, blit=False)
plt.show()