import cv2
import numpy as np


def load_image(filename: str, imread_flag: int = cv2.IMREAD_COLOR):
    """
    Load an image using OpenCV with the given read flag.

    Parameters
    ----------
        filename (str): Path to the image file.
        imread_flag (int): OpenCV imread flag (default is cv2.IMREAD_COLOR).
    """
    new_image = cv2.imread(filename, imread_flag)
    if new_image is None:
        error_string = "Error opening image"
        return None, error_string
    return new_image, None


def to_grayscale(image: np.ndarray) -> np.ndarray:
    """Convert an RGB image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


def extract_channel(image: np.ndarray, mode: str) -> np.ndarray:
    """
    Extract a single color channel from an RGB image.

    Parameters
    ----------
        image (np.ndarray): RGB image.
        mode (str): One of 'red', 'green', or 'blue'.

    Returns
    ----------
        np.ndarray: An image with only the selected color channel.
    """
    channels = cv2.split(image)
    mode_index = {"red": 0, "green": 1, "blue": 2}
    mode = mode.lower()
    idx = mode_index[mode]
    zeros = np.zeros_like(channels[idx])
    return cv2.merge([channels[idx] if i == idx else zeros for i in range(3)])
