import cv2
import napari
import numpy as np
from pathlib import Path

import hist_equalization
import image_handler
import image_plotter


def main():
    # File paths
    base_path = Path(__file__).parent.resolve() / "dataset"
    image_path = base_path / "CardioClarityFluoro.dcm"

    try:
        # Opening image with parameters of interest
        file_dcm = image_handler.load_image(image_path)
        print(file_dcm)

        # Parameter extraction
        image_dcm = file_dcm.pixel_array
        z, y, x = image_dcm.shape
        N = file_dcm.BitsAllocated
        print("---")
        print(
            f"The image contains frames of size {x}x{y} and the total number of frames is {z}"
        )
        print(f"Manufacturer : {str(file_dcm.Manufacturer)}")
        print(f"Manufacturer Model Name : {str(file_dcm.ManufacturerModelName)}")
        frame_rate = int(file_dcm.CineRate)
        print(f"Frame Rate : {frame_rate} Hz")
        print(f"Duration of acquisition : {round(z/frame_rate,1)} s")

        # Visualize the volume
        # viewer = napari.Viewer()
        # viewer.add_image(image_dcm, name="DICOM Volume", colormap="gray")
        # napari.run()

    except (FileNotFoundError, ValueError) as e:
        raise e
    except Exception as e:
        raise RuntimeError(f"Unexpected error while reading image: {e}") from e

    try:
        n_frame = 39
        ref_image = image_dcm[n_frame, :, :]
        image_plotter.display_image_hist(ref_image, N)

        equ = cv2.equalizeHist(ref_image)
        image_plotter.display_image_hist(equ, N)

        res = np.hstack((ref_image, equ))  # stacking images side-by-side
        image_plotter.display_image_hist(res, N)

        hist_equalization.cumulative_histogram(ref_image, N)

    except Exception as e:
        raise RuntimeError(f"Unexpected error while equalizing histogram: {e}") from e


if __name__ == "__main__":
    main()
