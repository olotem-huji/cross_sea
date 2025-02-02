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
yerr = 0.075

plt.errorbar(wavelength_by_freq.keys(),
            [v * SCREEN_TO_REAL_RAT for v in wavelength_by_freq.values()],
            yerr=yerr,
             fmt='o',
             capsize=3,
             # s=15
             )
x_fit = np.linspace(10, 30, 100)

y_fit = 2*np.pi * 9.81 * 0.006 / (x_fit)
# plt.plot(x_fit, y_fit)
plt.xlabel("Source Frequency [Hz]", fontsize=18)
plt.ylabel("Wavelength [cm]", fontsize=18)
plt.show()