
import numpy as np
import matplotlib.pyplot as plt

def stream_function(r, theta, U, a, K):
    return U * np.sin(theta) * (r - a**2 / r) - K * np.log(r / a)

def simulate_flow_past_cylinder(U, a, K_values, n_points=100):
    x = np.linspace(-5 * a, 5 * a, n_points)
    y = np.linspace(-5 * a, 5 * a, n_points)
    X, Y = np.meshgrid(x, y)

    R = np.sqrt(X**2 + Y**2)
    Theta = np.arctan2(Y, X)

    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    axs = axs.ravel()

    for i, K in enumerate(K_values):
        psi = stream_function(R, Theta, U, a, K)
        axs[i].contour(X, Y, psi, levels=np.linspace(-10*U*a, 10*U*a, 100), linewidths=0.5)
        axs[i].set_title(f"K/(U*a) = {K / (U * a)}")
        cylinder = plt.Circle((0, 0), a, color='black', fill=False, linewidth=1)
        axs[i].add_patch(cylinder)
        axs[i].set_aspect('equal', 'box')
        axs[i].set_xlim(-5 * a, 5 * a)
        axs[i].set_ylim(-5 * a, 5 * a)
        axs[i].set_xlabel('X')
        axs[i].set_ylabel('Y')

    plt.tight_layout()
    plt.show()
