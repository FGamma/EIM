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
from lab01.viewer.image_plotter import plot_image, plot_image_brightness
from lab01.viewer.dialog_helpers import initialize_image_filedialog


class Viewer(QMainWindow):
    def __init__(self):
        super().__init__()

        # Internal state
        self._first_file_dialog = True
        self._scale_factor = 0.0
        self._image = None

        # UI setup
        self._ui = Ui_mwViewer()
        self._ui.setupUi(self)

        # Image display setup
        self.fig_image = Figure(figsize=(5, 3))
        self.canvas_image = FigureCanvas(self.fig_image)
        self._setup_canvas(self._ui.wdgImage, self.canvas_image)

        # Brightness/Type display setup
        self.fig_type_image = Figure(figsize=(5, 3))
        self.canvas_type_image = FigureCanvas(self.fig_type_image)
        self._setup_canvas(self._ui.wdgTypeImage, self.canvas_type_image)

        self._create_actions()

    def _setup_canvas(self, widget, canvas):
        layout = widget.layout()
        if layout is None:
            layout = QVBoxLayout(widget)
            widget.setLayout(layout)
        layout.addWidget(canvas)

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

    def _scale_brightness(self, factor):
        """Adjust image brightness by a scale factor."""
        self._scale_factor += factor
        plot_image_brightness(
            self.fig_type_image,
            self._image,
            mode="blue",
            canvas=self.canvas_type_image,
            factor=self._scale_factor,
        )

        # self._ui.actIn.setEnabled(self._scale_factor < 255)
        # self._ui.actOut.setEnabled(self._scale_factor > 1)

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
    def _brightness_in(self):
        self._scale_brightness(10)

    @Slot()
    def _brightness_out(self):
        self._scale_brightness(-10)

    @Slot()
    def _normal_brightness(self):
        plot_image(
            self.fig_type_image, self._image, mode="blue", canvas=self.canvas_type_image
        )
        self._scale_factor = 0.0

    @Slot()
    def _about(self):
        QMessageBox.about(self, "About Image Viewer", ABOUT)

    @Slot()
    def _combo_option(self, text):
        plot_image(
            self.fig_type_image, self._image, mode=text, canvas=self.canvas_type_image
        )

        self._update_actions()

    def _create_actions(self):
        self._ui.actOpen.triggered.connect(self._open)
        self._ui.actExit.triggered.connect(self.close)
        self._ui.actIn.triggered.connect(self._brightness_in)
        self._ui.actIn.setEnabled(False)
        self._ui.actOut.triggered.connect(self._brightness_out)
        self._ui.actOut.setEnabled(False)
        self._ui.actNormal.triggered.connect(self._normal_brightness)
        self._ui.actNormal.setEnabled(False)
        self._ui.actAbout.triggered.connect(self._about)
        self._ui.cbTypeImage.currentTextChanged.connect(self._combo_option)

    def _update_actions(self):
        """Enable or disable UI actions based on image and combo state."""
        has_image = not self._image is None
        is_blue_mode = self._ui.cbTypeImage.currentText() == "Blue"

        self._ui.actIn.setEnabled(has_image and is_blue_mode)
        self._ui.actOut.setEnabled(has_image and is_blue_mode)
        self._ui.actNormal.setEnabled(has_image and is_blue_mode)
