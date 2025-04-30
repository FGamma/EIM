from __future__ import annotations

from PySide6.QtWidgets import QDialog, QFileDialog, QMainWindow, QMessageBox
from PySide6.QtGui import QColorSpace, QGuiApplication, QPixmap
from PySide6.QtCore import Slot, QDir

from myimageviewer.viewer.UI.viewer_window import Ui_mwViewer
from myimageviewer.viewer.constants import ABOUT
from myimageviewer.viewer.image_handler import load_image, save_image
from myimageviewer.viewer.dialog_helpers import initialize_image_filedialog


class Viewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self._scale_factor = 1.0
        self._first_file_dialog = True

        self._ui = Ui_mwViewer()
        self._ui.setupUi(self)

        self._create_actions()

    def load_file(self, fileName):
        new_image, error = load_image(fileName)
        native_filename = QDir.toNativeSeparators(fileName)
        if new_image is None:
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
        success, error = save_image(self._image, fileName)
        native_filename = QDir.toNativeSeparators(fileName)
        if not success:
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
        initialize_image_filedialog(
            dialog, QFileDialog.AcceptMode.AcceptOpen, self._first_file_dialog
        )
        self._first_file_dialog = False
        while dialog.exec() == QDialog.DialogCode.Accepted and not self.load_file(
            dialog.selectedFiles()[0]
        ):
            pass

    @Slot()
    def _save_as(self):
        dialog = QFileDialog(self, "Save File As")
        initialize_image_filedialog(dialog, QFileDialog.AcceptMode.AcceptSave)
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
