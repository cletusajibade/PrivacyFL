from PyQt5.QtWidgets import QApplication
from app_main_window import AppMainWindow

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = AppMainWindow()
    window.show()
    sys.exit(app.exec_())
