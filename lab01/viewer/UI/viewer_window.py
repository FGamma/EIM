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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSlider, QStatusBar, QVBoxLayout, QWidget)

class Ui_mwViewer(object):
    def setupUi(self, mwViewer):
        if not mwViewer.objectName():
            mwViewer.setObjectName(u"mwViewer")
        mwViewer.resize(986, 704)
        self.actOpen = QAction(mwViewer)
        self.actOpen.setObjectName(u"actOpen")
        self.actExit = QAction(mwViewer)
        self.actExit.setObjectName(u"actExit")
        self.actAbout = QAction(mwViewer)
        self.actAbout.setObjectName(u"actAbout")
        self.actIn = QAction(mwViewer)
        self.actIn.setObjectName(u"actIn")
        self.actOut = QAction(mwViewer)
        self.actOut.setObjectName(u"actOut")
        self.actNormal = QAction(mwViewer)
        self.actNormal.setObjectName(u"actNormal")
        self.centralwidget = QWidget(mwViewer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vlayPlot = QVBoxLayout()
        self.vlayPlot.setObjectName(u"vlayPlot")
        self.lblImage = QLabel(self.centralwidget)
        self.lblImage.setObjectName(u"lblImage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblImage.sizePolicy().hasHeightForWidth())
        self.lblImage.setSizePolicy(sizePolicy)

        self.vlayPlot.addWidget(self.lblImage)

        self.wdgImage = QWidget(self.centralwidget)
        self.wdgImage.setObjectName(u"wdgImage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wdgImage.sizePolicy().hasHeightForWidth())
        self.wdgImage.setSizePolicy(sizePolicy1)

        self.vlayPlot.addWidget(self.wdgImage)

        self.lblContrast = QLabel(self.centralwidget)
        self.lblContrast.setObjectName(u"lblContrast")
        sizePolicy.setHeightForWidth(self.lblContrast.sizePolicy().hasHeightForWidth())
        self.lblContrast.setSizePolicy(sizePolicy)

        self.vlayPlot.addWidget(self.lblContrast)

        self.sldContrast = QSlider(self.centralwidget)
        self.sldContrast.setObjectName(u"sldContrast")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sldContrast.sizePolicy().hasHeightForWidth())
        self.sldContrast.setSizePolicy(sizePolicy2)
        self.sldContrast.setOrientation(Qt.Orientation.Horizontal)

        self.vlayPlot.addWidget(self.sldContrast)


        self.horizontalLayout.addLayout(self.vlayPlot)

        self.vlayControl = QVBoxLayout()
        self.vlayControl.setObjectName(u"vlayControl")
        self.lblTypeImage = QLabel(self.centralwidget)
        self.lblTypeImage.setObjectName(u"lblTypeImage")
        sizePolicy.setHeightForWidth(self.lblTypeImage.sizePolicy().hasHeightForWidth())
        self.lblTypeImage.setSizePolicy(sizePolicy)

        self.vlayControl.addWidget(self.lblTypeImage)

        self.wdgTypeImage = QWidget(self.centralwidget)
        self.wdgTypeImage.setObjectName(u"wdgTypeImage")
        sizePolicy1.setHeightForWidth(self.wdgTypeImage.sizePolicy().hasHeightForWidth())
        self.wdgTypeImage.setSizePolicy(sizePolicy1)

        self.vlayControl.addWidget(self.wdgTypeImage)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.vlayControl.addWidget(self.label)

        self.cbTypeImage = QComboBox(self.centralwidget)
        self.cbTypeImage.addItem("")
        self.cbTypeImage.addItem("")
        self.cbTypeImage.addItem("")
        self.cbTypeImage.addItem("")
        self.cbTypeImage.addItem("")
        self.cbTypeImage.setObjectName(u"cbTypeImage")
        sizePolicy2.setHeightForWidth(self.cbTypeImage.sizePolicy().hasHeightForWidth())
        self.cbTypeImage.setSizePolicy(sizePolicy2)

        self.vlayControl.addWidget(self.cbTypeImage)


        self.horizontalLayout.addLayout(self.vlayControl)

        mwViewer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mwViewer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 986, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuBlue_Brightness = QMenu(self.menubar)
        self.menuBlue_Brightness.setObjectName(u"menuBlue_Brightness")
        mwViewer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mwViewer)
        self.statusbar.setObjectName(u"statusbar")
        mwViewer.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuBlue_Brightness.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actOpen)
        self.menuFile.addAction(self.actExit)
        self.menuHelp.addAction(self.actAbout)
        self.menuBlue_Brightness.addAction(self.actIn)
        self.menuBlue_Brightness.addAction(self.actOut)
        self.menuBlue_Brightness.addAction(self.actNormal)

        self.retranslateUi(mwViewer)

        QMetaObject.connectSlotsByName(mwViewer)
    # setupUi

    def retranslateUi(self, mwViewer):
        mwViewer.setWindowTitle(QCoreApplication.translate("mwViewer", u"Viewer", None))
        self.actOpen.setText(QCoreApplication.translate("mwViewer", u"Open...", None))
        self.actExit.setText(QCoreApplication.translate("mwViewer", u"Exit", None))
        self.actAbout.setText(QCoreApplication.translate("mwViewer", u"About", None))
        self.actIn.setText(QCoreApplication.translate("mwViewer", u"In (25%)", None))
#if QT_CONFIG(shortcut)
        self.actIn.setShortcut(QCoreApplication.translate("mwViewer", u"Ctrl++", None))
#endif // QT_CONFIG(shortcut)
        self.actOut.setText(QCoreApplication.translate("mwViewer", u"Out (25%)", None))
#if QT_CONFIG(shortcut)
        self.actOut.setShortcut(QCoreApplication.translate("mwViewer", u"Ctrl+-", None))
#endif // QT_CONFIG(shortcut)
        self.actNormal.setText(QCoreApplication.translate("mwViewer", u"Normal", None))
        self.lblImage.setText(QCoreApplication.translate("mwViewer", u"Load Image", None))
        self.lblContrast.setText(QCoreApplication.translate("mwViewer", u"Contrast", None))
        self.lblTypeImage.setText(QCoreApplication.translate("mwViewer", u"Image color scale", None))
        self.label.setText(QCoreApplication.translate("mwViewer", u"Color scale type:", None))
        self.cbTypeImage.setItemText(0, QCoreApplication.translate("mwViewer", u"Grayscale", None))
        self.cbTypeImage.setItemText(1, QCoreApplication.translate("mwViewer", u"Red", None))
        self.cbTypeImage.setItemText(2, QCoreApplication.translate("mwViewer", u"Green", None))
        self.cbTypeImage.setItemText(3, QCoreApplication.translate("mwViewer", u"Blue", None))
        self.cbTypeImage.setItemText(4, QCoreApplication.translate("mwViewer", u"RGB", None))

        self.menuFile.setTitle(QCoreApplication.translate("mwViewer", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("mwViewer", u"Help", None))
        self.menuBlue_Brightness.setTitle(QCoreApplication.translate("mwViewer", u"Blue Brightness", None))
    # retranslateUi

