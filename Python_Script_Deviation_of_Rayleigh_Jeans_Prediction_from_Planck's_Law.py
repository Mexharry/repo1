import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-34  # Planck's constant (J s)
c = 3.0e8       # Speed of light (m/s)
k = 1.38e-23    # Boltzmann's constant (J/K)
T = 1500        # Temperature in Kelvin

# Frequency range (in Hz)
nu = np.linspace(0.1e14, 4e14, 400)

# Planck's Law: Spectral radiance
B_nu = ( (2 * h * nu**3) / (c**2) ) / (np.exp((h * nu) / (k * T)) - 1)

# Classical Rayleigh-Jeans Law approximation
RJ_nu = (2 * nu**2 * k * T) / (c**2)


# Set up the figure and axis
fig, ax1 = plt.subplots()


for ax in ['top', 'bottom', 'left', 'right']:
    # ax1.spines[]
    ax1.spines[ax].set_linewidth(5.5)
    ax1.spines[ax].set_color('black')
#ax1.tick_params(width=6)
fig.set_dpi(120)

#plt.style.use('bmh')
ax1.tick_params(direction='in', length=6, width=2, colors='k',
               grid_color='b', grid_alpha=0.5)

fontsize = 16



for tick in ax1.xaxis.get_major_ticks():
    tick.label1.set_fontsize(fontsize)
    tick.label1.set_fontweight('bold')
for tick in ax1.yaxis.get_major_ticks():
    tick.label1.set_fontsize(fontsize)
    tick.label1.set_fontweight('bold')

# Plotting
#plt.figure(figsize=(8,5))
ax1.plot(nu / 1e14, B_nu * 1e17, label="Planck's Black Body Spectrum", color='blue', linewidth = 3)  # Scaled for visualization
ax1.plot(nu / 1e14, RJ_nu * 1e17, '--', label='Classical Rayleigh-Jeans Prediction', color='red', linewidth = 3)
ax1.set_title(r"Deviation of Rayleigh-Jeans Prediction from the Planck's Spectrum", fontsize = 14, fontweight = 'bold')
#%%
# Labels and annotations
plt.xlabel(r'$\nu \ (10^{14} Hz)$', fontsize = 18, fontweight = 'bold')
plt.ylabel(r'$\rho_T(\nu) \ (10^{-17} \frac{J}{m^3 Hz})$', fontsize = 18, fontweight = 'bold')
plt.text(2, 2.07e7, r'$T = 1500^\circ K$', fontsize=12, color='magenta', fontweight = 'bold')
plt.text(1, 6.2e7, r"Planck's Radiation Spectrum", fontsize=12, color='red', fontweight = 'bold')
plt.text(0.54, 1.25e8, r'Rayleigh-Jeans Ultraviolet Catastrophe', fontsize = 12, color = 'blue', fontweight = 'bold')
plt.xlim(0.091, 4)
plt.ylim(0.001e9, 0.2e9)

plt.legend()
plt.grid()

# Show plot
plt.show()
