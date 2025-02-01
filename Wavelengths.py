import matplotlib.pyplot as plt
import numpy as np

plt.style.use("physrev.mlpstyle")

SCREEN_TO_REAL_RAT = 10.5/28
wavelength_by_freq = {
    12.5: 4.3,
    15: 3.2,
    17.5: 3.1,
    20: 2.8,
    22.5: 2.2,
    25: 2.1,
    27.5: 2.1,
    30: 2
}

plt.plot(wavelength_by_freq.keys(), [v/100 * SCREEN_TO_REAL_RAT for v in wavelength_by_freq.values()])
x_fit = np.linspace(10, 30, 100)
y_fit = 2*np.pi * 9.81 * 0.006 / (2*np.pi*x_fit) * 3
plt.plot(x_fit, y_fit)
plt.show()