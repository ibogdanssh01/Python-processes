import sys
import ctypes
import platform
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QSize, QThread, pyqtSignal as Signal, pyqtSlot as Slot, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSystemTrayIcon, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/MainWindow.ui', self)

        icon = QIcon(QPixmap('assets/logo.png'))
        self.setWindowIcon(icon)

        my_gui = u'python.processes'
        if platform.system() == 'Windows':
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_gui)

        if platform.system() == 'Linux': # TODO: Fix on Wayland
            QApplication.setDesktopFileName(my_gui)
            QApplication.desktopFileName()

        self.setWindowTitle('BETA')

        icon_tray = QIcon(QPixmap('assets/tray.png'))
        tray = QSystemTrayIcon(self)
        tray.setIcon(icon_tray)
        tray.show()

        # tray example
        # tray.showMessage(
        #     "Tray Notification",
        #     "This is a test notification!",
        #     icon_tray,
        #     5000,
        # )


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    window = MainWindow()
    window.show()
    app.exec()
