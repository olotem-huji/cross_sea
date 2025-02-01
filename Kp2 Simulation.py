import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.fftpack import fft2, ifft2

# Simulation parameters
Lx, Ly = 20, 20  # Spatial domain size
Nx, Ny = 128, 128  # Grid resolution
T = 10  # Total time
dt = 0.001  # Time step

# Wave parameters
c = 1.0  # Wave speed
beta = 0.1  # Dispersion coefficient
gamma = 1.0  # Transverse effect coefficient

# Create spatial grid
x = np.linspace(-Lx / 2, Lx / 2, Nx)
y = np.linspace(-Ly / 2, Ly / 2, Ny)
X, Y = np.meshgrid(x, y)
dx, dy = x[1] - x[0], y[1] - y[0]

# Define initial condition (localized wave packet)
eta = np.exp(-X ** 2 - Y ** 2)

# Define wave numbers
kx = 2 * np.pi * np.fft.fftfreq(Nx, d=dx)
ky = 2 * np.pi * np.fft.fftfreq(Ny, d=dy)
KX, KY = np.meshgrid(kx, ky)
K2 = KX ** 2 + KY ** 2  # Laplacian operator in Fourier space

# Create the figure for animation
fig, ax = plt.subplots(figsize=(6, 6))
contour = ax.contourf(X, Y, eta, levels=50, cmap='RdBu')
fig.colorbar(contour, ax=ax)
ax.set_title("KP-II Wave Simulation")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Function to update the plot for each frame
def update(t):
    global eta
    # Compute derivatives in Fourier space
    eta_hat = fft2(eta)
    eta_x = np.real(ifft2(1j * KX * eta_hat))
    eta_xx = np.real(ifft2(-KX ** 2 * eta_hat))
    eta_yyy = np.real(ifft2(-KY ** 2 * eta_hat))

    # KP-II update equation
    eta_t = - c * eta_x - beta * eta_xx - gamma * eta_yyy - eta * eta_x
    eta += dt * eta_t  # Forward Euler step

    # Update the contour plot by removing previous ones
    for collection in ax.collections:
        collection.remove()
    contour = ax.contourf(X, Y, eta, levels=50, cmap='RdBu')  # Create new contour
    ax.set_title(f"KP-II Simulation at t={t:.2f}")
    return contour.collections

# Create animation
t_values = np.arange(0, T, dt)
ani = FuncAnimation(fig, update, frames=t_values, interval=50, blit=False)

plt.show()
