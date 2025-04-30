# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewer_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QScrollArea, QSizePolicy,
    QStatusBar, QWidget)

class Ui_mwViewer(object):
    def setupUi(self, mwViewer):
        if not mwViewer.objectName():
            mwViewer.setObjectName(u"mwViewer")
        mwViewer.resize(874, 694)
        self.actOpen = QAction(mwViewer)
        self.actOpen.setObjectName(u"actOpen")
        self.actExit = QAction(mwViewer)
        self.actExit.setObjectName(u"actExit")
        self.actAbout = QAction(mwViewer)
        self.actAbout.setObjectName(u"actAbout")
        self.actSaveAs = QAction(mwViewer)
        self.actSaveAs.setObjectName(u"actSaveAs")
        self.actZoomIn = QAction(mwViewer)
        self.actZoomIn.setObjectName(u"actZoomIn")
        self.actZoomOut = QAction(mwViewer)
        self.actZoomOut.setObjectName(u"actZoomOut")
        self.actNormalSize = QAction(mwViewer)
        self.actNormalSize.setObjectName(u"actNormalSize")
        self.centralwidget = QWidget(mwViewer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollImage = QScrollArea(self.centralwidget)
        self.scrollImage.setObjectName(u"scrollImage")
        self.scrollImage.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 854, 631))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblImage = QLabel(self.scrollAreaWidgetContents)
        self.lblImage.setObjectName(u"lblImage")
        self.lblImage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lblImage, 0, 0, 1, 1)

        self.scrollImage.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollImage, 0, 0, 1, 1)

        mwViewer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mwViewer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 874, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        mwViewer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mwViewer)
        self.statusbar.setObjectName(u"statusbar")
        mwViewer.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actOpen)
        self.menuFile.addAction(self.actSaveAs)
        self.menuFile.addAction(self.actExit)
        self.menuHelp.addAction(self.actAbout)

        self.retranslateUi(mwViewer)

        QMetaObject.connectSlotsByName(mwViewer)
    # setupUi

    def retranslateUi(self, mwViewer):
        mwViewer.setWindowTitle(QCoreApplication.translate("mwViewer", u"Image Viewer", None))
        self.actOpen.setText(QCoreApplication.translate("mwViewer", u"Open...", None))
#if QT_CONFIG(shortcut)
        self.actOpen.setShortcut(QCoreApplication.translate("mwViewer", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actExit.setText(QCoreApplication.translate("mwViewer", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actExit.setShortcut(QCoreApplication.translate("mwViewer", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actAbout.setText(QCoreApplication.translate("mwViewer", u"About", None))
        self.actSaveAs.setText(QCoreApplication.translate("mwViewer", u"Save As...", None))
        self.actZoomIn.setText(QCoreApplication.translate("mwViewer", u"Zoom In (25%)", None))
        self.actZoomOut.setText(QCoreApplication.translate("mwViewer", u"Zoom Out (25%)", None))
        self.actNormalSize.setText(QCoreApplication.translate("mwViewer", u"Normal Size", None))
        self.lblImage.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("mwViewer", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("mwViewer", u"Help", None))
    # retranslateUi

