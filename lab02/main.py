import napari
from pathlib import Path

import image_handler


def main():
    # File paths
    base_path = Path(__file__).parent.resolve() / "dataset"
    image_path = base_path / "CardioClarityFluoro.dcm"

    try:
        file_dcm = image_handler.load_image(image_path)
        print(file_dcm)

        # Parameter extraction
        image_dcm = file_dcm.pixel_array
        z, y, x = image_dcm.shape
        print("---")
        print(
            f"The image contains frames of size {x}x{y} and the total number of frames is {z}"
        )
        print(f"Manufacturer : {str(file_dcm.Manufacturer)}")
        print(f"Manufacturer Model Name : {str(file_dcm.ManufacturerModelName)}")
        frame_rate = int(file_dcm.CineRate)
        print(f"Frame Rate : {frame_rate} Hz")
        print(f"Duration of acquisition : {round(z/frame_rate,1)} s")

        viewer = napari.Viewer()
        viewer.add_image(image_dcm, name="DICOM Volume", colormap="gray")
        napari.run()

    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise RuntimeError(f"Unexpected error while reading image: {e}") from e


if __name__ == "__main__":
    main()
