import matplotlib.pyplot as plt
import numpy as np


def display_image_hist(image: np.ndarray, N: int):
    """
    Display an image using Matplotlib.

    Parameters
    ----------
    image : np.ndarray
        The image matrix to be displayed.
    N : int
        Number of bit.
    """
    lev = 2**N
    fig, ax = plt.subplots(2, 1, figsize=(5, 3))
    ax[0].imshow(image, cmap="gray")
    ax[0].axis("off")
    ax[0].set_title("Image")

    ax[1].hist(image.ravel(), lev, [0, lev])
    ax[1].set(
        title="Histogram",
        xlabel="Pixel Intensity",
        ylabel="Number of Pixels",
        xlim=(0, lev),
    )
    plt.show()


def plot_cumulative(cdf_normalized: np.ndarray, image: np.ndarray, N: int):
    """
    Display histogram cumulative and histogram.

    Parameters
    ----------
    cdf_normalized: np.ndarray
        Histogram cumulative
    image : np.ndarray
        The image matrix to be displayed.
    N : int
        Number of bit.
    """
    lev = 2**N
    plt.plot(cdf_normalized, color="b")
    plt.hist(image.flatten(), lev, [0, lev], color="r")
    plt.xlim([0, 256])
    plt.legend(("cdf", "histogram"), loc="upper left")
    plt.show()
