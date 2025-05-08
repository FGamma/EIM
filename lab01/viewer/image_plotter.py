import cv2
import numpy as np

from lab01.viewer.image_handler import to_grayscale, extract_channel, change_brightness


def plot_image(fig, image: np.ndarray, mode: str, canvas=None) -> None:
    """
    Plot an image or its specific color/grayscale representation.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Matplotlib figure object to draw on.
    image : np.ndarray
        Image in BGR format (as loaded by OpenCV).
    mode : str
        Mode to plot: 'rgb', 'grayscale', 'red', 'green', 'blue'.
    canvas : Optional[FigureCanvasQTAgg]
        Optional Qt canvas for GUI integration.
    """
    fig.clear()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mode = mode.lower()

    if mode == "rgb":
        colors = ["red", "green", "blue"]
        axs = fig.subplots(1, 3)
        for ax, color in zip(axs, colors):
            ax.imshow(extract_channel(image, color), interpolation="none")
            ax.set_title(f"{color} channel")
            ax.axis("off")
        fig.tight_layout()

    else:
        ax = fig.add_subplot(111)
        if mode == "grayscale":
            img = to_grayscale(image)
            ax.imshow(img, cmap="gray")
            ax.set_title("Grayscale")
        elif mode in {"red", "green", "blue"}:
            img = extract_channel(image, mode)
            ax.imshow(img)
            ax.set_title(f"{mode} channel")
        else:
            ax.imshow(image)
            ax.set_title("original image")
        ax.axis("off")

    if canvas:
        canvas.draw()


def plot_image_brightness(
    fig,
    image: np.ndarray,
    mode: str,
    canvas=None,
    factor: float = 0.0,
) -> None:
    """
    Adjust brightness and plot a single color channel from the image.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Matplotlib figure object to draw on.
    image : np.ndarray
        Image in BGR format (as loaded by OpenCV).
    mode : str
        Color channel to display ('red', 'green', 'blue').
    canvas : Optional[FigureCanvasQTAgg]
        Optional Qt canvas for GUI integration.
    factor : float
        Brightness adjustment factor (can be negative).
    """
    fig.clear()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_brightness = change_brightness(image, factor)
    ax = fig.add_subplot(111)
    image_mode = extract_channel(image_brightness, mode)
    ax.imshow(image_mode)
    ax.set_title(f"Brightness {factor}")
    ax.axis("off")

    if canvas:
        canvas.draw()
