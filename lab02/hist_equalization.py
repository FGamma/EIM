import matplotlib.pyplot as plt
import numpy as np

import image_plotter


def cumulative_histogram(image: np.ndarray, N: int):
    """
    Histogram cumulative calculation.

    Parameters
    ----------
    image : np.ndarray
        Image.
    N : int
        Number of bit.
    """
    lev = 2**N
    hist, bins = np.histogram(image.flatten(), lev, [0, lev])

    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()

    image_plotter.plot_cumulative(cdf_normalized, image, N)
