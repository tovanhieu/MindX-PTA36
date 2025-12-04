import sys
from PyQt6.QtWidget import QMainWindow, QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Cửa sổ đầu tiên")
    window.setGeometry(100, 100, 600, 400)
    window.show()
    sys.exit(app.exec())
