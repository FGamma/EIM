from pydicom import dcmread, FileDataset
import numpy as np
from pathlib import Path


def load_image(path: Path) -> FileDataset:
    """Load image.

    Parameters
    ----------
    path : Path
        File path.

    Returns
    -------
    FileDataset
        Loaded image.
    """
    if not path.is_file():
        raise FileNotFoundError(f"Image {path.name} does not exist.")

    image = dcmread(path)

    return image