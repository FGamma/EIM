from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from viewer.viewer import Viewer


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    viewer = Viewer()
    viewer.show()
    sys.exit(app.exec())
