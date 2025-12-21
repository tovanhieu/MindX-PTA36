import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Label
        self.label = QLabel("Button not clicked", self)
        self.label.move(50, 50)

        # Button
        btn = QPushButton("Click Me", self)
        btn.move(50, 100)
        btn.clicked.connect(self.onButtonClick)

        # Window config
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle("Day 7 Application PTA36")
        self.show()

    def onButtonClick(self):
        self.label.setText("Button Clicked!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
# Ví dụ về envent handler

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt
import sys

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Day 7 Application PTA36')
        self.setGeometry(300, 300, 400, 300)
        self.show()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
           self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())

# Ví dụ về message box 
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
app = QApplication(sys.argv)
msg_box = QMessageBox()
msg_box.setWindowTitle("Error - Lỗi")
msg_box.setIcon(QMessageBox.Icon.Warning)
msg_box.setText("Vui lòng nhập đúng thông tin!")
msg_box.setStyleSheet("background-color: blue; font-size: 14px; color: white;")
sys.exit(msg_box.exec())