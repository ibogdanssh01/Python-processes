import sys
import orjson
import ctypes
from time import sleep
import platform
from src.core.python_processes.python_processes import ProcessMonitor
from src.core.python_processes.enums import ProcessType
from src.config.json_script import dump_data
from PyQt6.QtGui import QIcon, QPixmap, QStandardItemModel, QStandardItem
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

        processMonitor = ProcessMonitor()
        json_data = processMonitor.get_processes_with_parents()
        dump_data(json_data)
        print(json_data)


        self.pushButton_3.clicked.connect(self.start)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Name", "PID", "PPID", "Status", "Process type", "Path"])

        for parent, child in json_data.items():

            parent_name = QStandardItem(parent.split('_')[-1])
            parent_pid = QStandardItem(parent.split('_')[1])

            self.model.appendRow([parent_name, parent_pid])

            for pid, data in child.items():

                child_name = QStandardItem(data['name'])
                child_pid = QStandardItem(pid.split('_')[-1])
                child_ppid = QStandardItem(parent_pid)
                child_status = QStandardItem(data['status'])
                child_type = QStandardItem(str(data['process_type'].value))
                child_path = QStandardItem(data['path'])

                parent_name.appendRow([child_name, child_pid, child_ppid, child_status, child_type, child_path])

        self.treeView.setModel(self.model)
        self.treeView.setColumnWidth(0, 200)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setAnimated(True)
        self.treeView.expandAll()


        # tray example
        # tray.showMessage(
        #     "Tray Notification",
        #     "This is a test notification!",
        #     icon_tray,
        #     5000,
        # )

    def start(self):
        print("start")




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    window = MainWindow()
    window.show()
    app.exec()
