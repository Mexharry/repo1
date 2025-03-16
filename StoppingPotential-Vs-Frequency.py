import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Given frequency data (in Hz) and stopping potential (V)
freq = np.array([5.5e14, 6.0e14, 7.0e14, 8.0e14, 10.0e14, 12.5e14])  # Hz
V_stop = np.array([0, 0.5, 0.9, 1.3, 2.2, 3.1])  # V

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(freq, V_stop)
fit_line = slope * freq + intercept

# Plot the graph
#plt.figure(figsize=(6, 4))
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

ax1.plot(freq, V_stop, 'bo', label="Data Points", linewidth = 3)  # Data points
ax1.plot(freq, fit_line, 'r-', label="Linear Fit", linewidth = 3)  # Best fit line

# Mark threshold frequency (x-intercept)
thresh_freq = 5.5e14
plt.annotate(r'$\nu_0$', xy=(thresh_freq, 0.22), xytext=(thresh_freq - 1e14, 0.3),
             arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=18, fontweight = 'bold', color='blue')

# Labels and title
plt.xlabel(r'$f$ (Hz)', fontsize=18, fontweight = 'bold')
plt.ylabel(r'$V_{stop}$ (V)', fontsize=18, fontweight = 'bold')
#plt.title("Photoelectric Effect Graph", fontsize=14, fontweight = 'bold')
plt.xlim(0, 12.5e14)
plt.ylim(0.2, 3.5)
plt.legend()
plt.grid(True)
plt.show()
