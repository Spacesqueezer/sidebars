import sys, os
import win32gui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap


class Sidebar(QMainWindow):
    """Класс боковой панели.
    :param left : Левая или правая панель.
    :type left : bool
    :param coord_y : Координата отступа сверху. По умолчанию 0.
    :type coord_y : int
    :param width : Ширина панели.
    :type width : int
    """
    def __init__(self,
                 left: bool,
                 coord_y=0,
                 width=300,
                 height=400,
                 title="Sidebar",
                 ):
        super().__init__()

        self.file_list = []

        self.desktop = QApplication.desktop().screenGeometry()
        self.desktop_width = self.desktop.width()
        width = int(self.desktop_width / 10)
        taskbar_hwnd = win32gui.FindWindow("Shell_TrayWnd", None)
        height = win32gui.GetWindowRect(taskbar_hwnd)[1]

        if left:
            coord_x = 0
        else:
            coord_x = self.desktop_width - width

        button = QPushButton("Кнопа", self)
        button.move(20, 20)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(coord_x, coord_y, width, height)

    def get_icon(self):
        path = "C:/Users/user/Desktop/Games"
        icon = QIcon(path)
        print(icon)
        pixmap = icon.pixmap(QSize(64, 64))

        pixmap.save("C:/qqqq.png", "PNG")

    def get_files(self):
        path = "C:/Users/user/Desktop/Games"
        self.file_list = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        print(self.file_list)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window1 = Sidebar(True)
    window1.show()
    window1.get_files()

    window2 = Sidebar(False)
    window2.show()

    sys.exit(app.exec_())
