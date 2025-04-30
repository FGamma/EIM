from __future__ import annotations

from PySide6.QtWidgets import (
    QDialog,
    QFileDialog,
    QMainWindow,
    QMessageBox,
)
from PySide6.QtGui import (
    QColorSpace,
    QGuiApplication,
    QImageReader,
    QImageWriter,
    QPixmap,
)
from PySide6.QtCore import QDir, QStandardPaths, Slot

from myimageviewer.viewer.UI.viewer_window import Ui_mwViewer


ABOUT = """<p>The <b>Image Viewer</b> example shows how to combine QLabel
and QScrollArea to display an image. QLabel is typically used
for displaying a text, but it can also display an image.
QScrollArea provides a scrolling view around another widget.
If the child widget exceeds the size of the frame, QScrollArea
automatically provides scroll bars. </p><p>The example
demonstrates how QLabel's ability to scale its contents
(QLabel.scaledContents), and QScrollArea's ability to
automatically resize its contents
(QScrollArea.widgetResizable), can be used to implement
zooming and scaling features. </p>
"""


class Viewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self._scale_factor = 1.0
        self._first_file_dialog = True

        self._ui = Ui_mwViewer()
        self._ui.setupUi(self)

        self._create_actions()

    def load_file(self, fileName):
        reader = QImageReader(fileName)
        reader.setAutoTransform(True)
        new_image = reader.read()
        native_filename = QDir.toNativeSeparators(fileName)
        if new_image.isNull():
            error = reader.errorString()
            QMessageBox.information(
                self,
                QGuiApplication.applicationDisplayName(),
                f"Cannot load {native_filename}: {error}",
            )
            return False
        self._set_image(new_image)
        self.setWindowFilePath(fileName)

        w = self._image.width()
        h = self._image.height()
        d = self._image.depth()
        color_space = self._image.colorSpace()
        description = color_space.description() if color_space.isValid() else "unknown"
        message = f'Opened "{native_filename}", {w}x{h}, Depth: {d} ({description})'
        self.statusBar().showMessage(message)
        return True

    def _set_image(self, new_image):
        self._image = new_image
        if self._image.colorSpace().isValid():
            color_space = QColorSpace(QColorSpace.NamedColorSpace.SRgb)
            self._image.convertToColorSpace(color_space)
        self._ui.lblImage.setPixmap(QPixmap.fromImage(self._image))
        self._ui.lblImage.adjustSize()
        self._scale_factor = 1.0

        self._ui.scrollImage.setVisible(True)
        self._update_actions()

    def _save_file(self, fileName):
        writer = QImageWriter(fileName)

        native_filename = QDir.toNativeSeparators(fileName)
        if not writer.write(self._image):
            error = writer.errorString()
            message = f"Cannot write {native_filename}: {error}"
            QMessageBox.information(
                self, QGuiApplication.applicationDisplayName(), message
            )
            return False
        self.statusBar().showMessage(f'Wrote "{native_filename}"')
        return True

    @Slot()
    def _open(self):
        dialog = QFileDialog(self, "Open File")
        self._initialize_image_filedialog(dialog, QFileDialog.AcceptMode.AcceptOpen)
        while dialog.exec() == QDialog.DialogCode.Accepted and not self.load_file(
            dialog.selectedFiles()[0]
        ):
            pass

    @Slot()
    def _save_as(self):
        dialog = QFileDialog(self, "Save File As")
        self._initialize_image_filedialog(dialog, QFileDialog.AcceptMode.AcceptSave)
        while dialog.exec() == QDialog.DialogCode.Accepted and not self._save_file(
            dialog.selectedFiles()[0]
        ):
            pass

    @Slot()
    def _about(self):
        QMessageBox.about(self, "About Image Viewer", ABOUT)

    def _create_actions(self):

        self._ui.actOpen.triggered.connect(self._open)

        self._ui.actSaveAs.triggered.connect(self._save_as)
        self._ui.actSaveAs.setEnabled(False)

        self._ui.actExit.triggered.connect(self.close)

        self._ui.actAbout.triggered.connect(self._about)

    def _update_actions(self):
        has_image = not self._image.isNull()
        self._ui.actSaveAs.setEnabled(has_image)

    def _initialize_image_filedialog(self, dialog, acceptMode):
        if self._first_file_dialog:
            self._first_file_dialog = False
            locations = QStandardPaths.standardLocations(
                QStandardPaths.StandardLocation.PicturesLocation
            )  # noqa: E501
            directory = locations[-1] if locations else QDir.currentPath()
            dialog.setDirectory(directory)

        mime_types = [
            m.data().decode("utf-8") for m in QImageWriter.supportedMimeTypes()
        ]
        mime_types.sort()

        dialog.setMimeTypeFilters(mime_types)
        dialog.selectMimeTypeFilter("image/jpeg")
        dialog.setAcceptMode(acceptMode)
        if acceptMode == QFileDialog.AcceptMode.AcceptSave:
            dialog.setDefaultSuffix("jpg")
