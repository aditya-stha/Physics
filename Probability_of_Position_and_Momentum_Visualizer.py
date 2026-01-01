import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Parameters
x = np.linspace(-10, 10, 2000)

# Initial width of wave packet
sigma_init = 1.0

# Function to compute Gaussian wave packet
def wave_packet(sigma):
    # Position-space wavefunction (Gaussian)
    psi_x = (1/(sigma * np.sqrt(2*np.pi))) * np.exp(-x**2 / (2*sigma**2))
    
    # Fourier transform to momentum space
    psi_p = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(psi_x)))
    p = np.fft.fftshift(np.fft.fftfreq(len(x), d=(x[1]-x[0]))) * 2*np.pi
    psi_p = np.abs(psi_p)**2
    psi_p /= np.sum(psi_p)  # Normalizing
    
    return psi_x, p, psi_p

# Plot setup
fig, ax = plt.subplots(2, 1, figsize=(10,6))
plt.subplots_adjust(bottom=0.25, hspace=0.582, left=0.1, right=0.9, top=0.9)

# Initial wave
psi_x, p, psi_p = wave_packet(sigma_init)
line1, = ax[0].plot(x, np.abs(psi_x)**2, color='blue')
ax[0].set_title("Position-space Probability |ψ(x)|²")
ax[0].set_xlabel("x")
ax[0].set_ylabel("Probability Density")

line2, = ax[1].plot(p, psi_p, color='red')
ax[1].set_title("Momentum-space Probability |ψ(p)|²")
ax[1].set_xlabel("p")
ax[1].set_ylabel("Probability Density")

# Slider axis
ax_sigma = plt.axes([0.25, 0.1, 0.65, 0.03])
sigma_slider = Slider(ax_sigma, 'Sigma', 0.1, 5.0, valinit=sigma_init)

# Update function
def update(val):
    sigma = sigma_slider.val
    psi_x, p, psi_p = wave_packet(sigma)
    line1.set_ydata(np.abs(psi_x)**2)
    line2.set_ydata(psi_p)
    fig.canvas.draw_idle()

sigma_slider.on_changed(update)
plt.show()
