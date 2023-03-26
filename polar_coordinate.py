
import numpy as np
import matplotlib.pyplot as plt

def stream_function(r, theta, U, a, K):
    return U * np.sin(theta) * (r - a**2 / r) - K * np.log(r / a)

def simulate_flow_past_cylinder(U, a, K_values, n_points=100):
    r = np.linspace(a, 5*a, n_points)
    theta = np.linspace(0, 2 * np.pi, n_points)
    R, Theta = np.meshgrid(r, theta)

    fig, axs = plt.subplots(2, 2, figsize=(10, 10), subplot_kw={'polar': True})
    axs = axs.ravel()

    for i, K in enumerate(K_values):
        psi = stream_function(R, Theta, U, a, K)
        axs[i].contour(Theta, R, psi, levels=np.linspace(-10*U*a, 10*U*a, 100), linewidths=0.5)
        axs[i].set_title(f"K/(U*a) = {K / (U * a)}")
        cylinder = plt.Circle((0, 0), a, color='black', fill=True)
        axs[i].add_patch(cylinder)

    plt.tight_layout()
    plt.show()
    
U = 1.0
a = 1.0
K_values = [0, 1.0 * U * a, 2.0 * U * a, 3.0 * U * a]
simulate_flow_past_cylinder(U, a, K_values)
