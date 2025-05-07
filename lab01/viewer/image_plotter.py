import cv2

from lab01.viewer.image_handler import to_grayscale, extract_channel


def plot_image(fig, image, mode: str, canvas=None):
    """
    Plot an image or its specific color/grayscale representation.

    Parameters
    ----------
        fig: Matplotlib figure object.
        image: Image as numpy array.
        mode : Mode to plot ('rgb', 'grayscale', 'red', 'green', 'blue').
        canvas: Optional Qt canvas for GUI.
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
            ax.set_title("Original image")
        ax.axis("off")

    if canvas:
        canvas.draw()
