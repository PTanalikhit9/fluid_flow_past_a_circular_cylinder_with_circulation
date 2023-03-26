
import numpy as np
import matplotlib.pyplot as plt

def stream_function(r, theta, U, a, K):
    return U * np.sin(theta) * (r - a**2 / r) - K * np.log(r / a)
