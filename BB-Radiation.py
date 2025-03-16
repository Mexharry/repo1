import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-34  # Planck's constant (J·s)
c = 3.0e8       # Speed of light (m/s)
kb = 1.381e-23  # Boltzmann constant (J/K)

# Define Planck's energy density function
def planck_energy_density(wavelength, temperature):
    """Calculate energy density using the given Planck's formula."""
    numerator = 8 * np.pi * h * c / (wavelength**5)
    denominator = np.exp((h * c) / (wavelength * kb * temperature)) - 1.0
    return numerator / denominator

# Wavelength range (in nanometers)
lambda_range = np.linspace(100, 2000, 500)  # 100 nm to 2000 nm

# Convert nm to meters for calculation
lambda_meters = lambda_range * 1e-9

# Define temperatures (in Kelvin)
temperatures = [4000, 5000, 6000, 7000]

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



# Plot the blackbody curves
#plt.figure(figsize=(8, 5))
for T in temperatures:
    radiance = planck_energy_density(lambda_meters, T)
    ax1.plot(lambda_range, radiance, linewidth = 3)
    max_idx = np.argmax(radiance)
    plt.text(lambda_range[max_idx], radiance[max_idx], f"{T}K", fontsize=12, fontweight = 'bold',
             verticalalignment='bottom', horizontalalignment='left', color='black')

# Highlight visible range (~400nm to 700nm)
plt.axvspan(400, 700, color='gray', alpha=0.3, label='Visible Region')

# Labels and title
plt.xlabel( r'$\lambda \ (nm)$', fontsize = 18, fontweight = 'bold')
plt.ylabel(r'$\rho_T (\lambda)  \frac{J}{m^3 nm})$', fontsize = 18, fontweight = 'bold')
plt.title("Blackbody Radiation Energy Density as a Function of Wavelength", fontsize = 14, fontweight = 'bold' )
plt.legend(loc='upper right')
plt.xlim(100, 2000)
plt.ylim(100, 3.5e6)
plt.grid(True)
plt.show()
