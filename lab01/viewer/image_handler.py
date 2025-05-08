import cv2
import numpy as np


def load_image(
    filename: str, imread_flag: int = cv2.IMREAD_COLOR
) -> tuple[np.ndarray | None, str | None]:
    """
    Load an image using OpenCV with the given read flag.

    Parameters
    ----------
    filename : str
        Path to the image file.
    imread_flag : int, optional
        OpenCV imread flag (default is cv2.IMREAD_COLOR).

    Returns
    -------
    tuple[np.ndarray | None, str | None]
        A tuple containing the loaded image or None and an error message or None.
    """
    new_image = cv2.imread(filename, imread_flag)
    if new_image is None:
        error_string = "Error opening image"
        return None, error_string
    return new_image, None


def to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Convert an RGB (or BGR) image to grayscale using OpenCV.

    Parameters
    ----------
    image : np.ndarray
        Input image in BGR or RGB format.

    Returns
    -------
    np.ndarray
        Grayscale image.
    """
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


def extract_channel(image: np.ndarray, mode: str) -> np.ndarray:
    """
    Extract a single color channel from a BGR image and zero out the others.

    Parameters
    ----------
    image : np.ndarray
        BGR image as loaded by OpenCV.
    mode : str
        One of 'red', 'green', or 'blue'.

    Returns
    -------
    np.ndarray
        An image with only the selected color channel visible.
    """
    channels = cv2.split(image)
    mode_index = {"red": 0, "green": 1, "blue": 2}
    mode = mode.lower()
    idx = mode_index[mode]
    zeros = np.zeros_like(channels[idx])
    return cv2.merge([channels[idx] if i == idx else zeros for i in range(3)])


def change_brightness(image: np.ndarray, factor: float) -> np.ndarray:
    """
    Change the brightness of the image by a given factor.

    Parameters
    ----------
    image : np.ndarray
        Input image.
    factor : float
        Brightness adjustment value. Can be negative or positive.

    Returns
    -------
    np.ndarray
        Brightness-adjusted image with values clipped to valid range.
    """
    return cv2.add(image, factor)
