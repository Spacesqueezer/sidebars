import sys
import win32gui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt


# Это окно, которое всегда находится сверху, не имеет границ и всегда имеет ту же ширину, что и панель задач.
class Sidebar(QMainWindow):
    """Класс боковой панели"""

    def __init__(self,
                 left: bool,
                 coord_y=0,
                 width=300,
                 height=400,
                 title="Sidebar",
                 ):
        super().__init__()

        self.desktop = QApplication.desktop().screenGeometry()
        self.desktop_width = self.desktop.width()
        self.desktop_height = self.desktop.height()
        width = int(self.desktop_width / 10)
        taskbar_hwnd = win32gui.FindWindow("Shell_TrayWnd", None)
        height = win32gui.GetWindowRect(taskbar_hwnd)[1]

        if left:
            coord_x = 0
        else:
            coord_x = self.desktop_width - width

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(coord_x, coord_y, width, height)

        label1 = QLabel(str(int(self.desktop_width / 10)), self)
        label1.move(50, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    print()

    window1 = Sidebar(True)
    window1.show()

    window2 = Sidebar(False)
    window2.show()

    sys.exit(app.exec_())
