from __future__ import annotations

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import (
    QDialog,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QVBoxLayout,
)
from PySide6.QtGui import QColorSpace, QGuiApplication, QPixmap
from PySide6.QtCore import Slot, QDir

from lab01.viewer.UI.viewer_window import Ui_mwViewer
from lab01.viewer.constants import ABOUT
from lab01.viewer.image_handler import load_image
from lab01.viewer.image_plotter import plot_image
from lab01.viewer.dialog_helpers import initialize_image_filedialog


class Viewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self._first_file_dialog = True
        self._image = None

        self._ui = Ui_mwViewer()
        self._ui.setupUi(self)

        self.fig_image = Figure(figsize=(5, 3))
        self.fig_type_image = Figure(figsize=(5, 3))

        self.canvas_image = FigureCanvas(self.fig_image)
        layout_image = self._ui.wdgImage.layout()
        if layout_image is None:
            layout_image = QVBoxLayout(self._ui.wdgImage)
            self._ui.wdgImage.setLayout(layout_image)
        layout_image.addWidget(self.canvas_image)

        self.canvas_type_image = FigureCanvas(self.fig_type_image)
        layout_type_image = self._ui.wdgTypeImage.layout()
        if layout_type_image is None:
            layout_type_image = QVBoxLayout(self._ui.wdgTypeImage)
            self._ui.wdgTypeImage.setLayout(layout_type_image)
        layout_type_image.addWidget(self.canvas_type_image)

        self._create_actions()

    def load_file(self, filename):
        """Load image file and display it."""
        new_image, error = load_image(filename)
        native_filename = QDir.toNativeSeparators(filename)
        if new_image is None:
            QMessageBox.information(
                self,
                QGuiApplication.applicationDisplayName(),
                f"Cannot load {native_filename}: {error}",
            )
            return False

        self._set_image(new_image)
        self.setWindowFilePath(filename)

        h, w, c = self._image.shape
        message = f'Opened "{native_filename}", {w}x{h}, Channels: {c}'
        self.statusBar().showMessage(message)

        return True

    def _set_image(self, new_image):
        """Set the current image and update display."""
        self._image = new_image
        plot_image(
            self.fig_image, self._image, mode="Original", canvas=self.canvas_image
        )

        self._ui.lblImage.setText("Original Image")

        self._update_actions()

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
    def _about(self):
        QMessageBox.about(self, "About Image Viewer", ABOUT)

    @Slot()
    def _combo_option(self, text):
        plot_image(
            self.fig_type_image, self._image, mode=text, canvas=self.canvas_type_image
        )

    def _create_actions(self):
        self._ui.actOpen.triggered.connect(self._open)
        self._ui.actExit.triggered.connect(self.close)
        self._ui.actAbout.triggered.connect(self._about)
        self._ui.cbTypeImage.currentTextChanged.connect(self._combo_option)

    def _update_actions(self):
        # Placeholder for enabling/disabling UI actions based on image state.
        has_image = not self._image is None
