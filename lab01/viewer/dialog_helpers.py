from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QDir, QStandardPaths
from PySide6.QtGui import QImageWriter


def initialize_image_filedialog(dialog, accept_mode, first_time=True):
    if first_time:
        locations = QStandardPaths.standardLocations(
            QStandardPaths.StandardLocation.PicturesLocation
        )
        dialog.setDirectory(locations[-1] if locations else QDir.currentPath())

    mime_types = [m.data().decode("utf-8") for m in QImageWriter.supportedMimeTypes()]
    mime_types.sort()

    dialog.setMimeTypeFilters(mime_types)
    dialog.selectMimeTypeFilter("image/jpeg")
    dialog.setAcceptMode(accept_mode)
    if accept_mode == QFileDialog.AcceptMode.AcceptSave:
        dialog.setDefaultSuffix("jpg")
