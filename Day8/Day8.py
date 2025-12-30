import sys
from PyQt6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit, QFontComboBox, QLineEdit, QMainWindow, QPushButton, QRadioButton, QSlider, QSpinBox, QVBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widgets App")
        self.layout = QVBoxLayout()
        self.widgets = [QCheckBox, QComboBox, QDateEdit, QFontComboBox, QLineEdit, QPushButton, QRadioButton, QSlider, QSpinBox]
        for w in self.widgets:
            self.layout.addWidget(w())
            self.central_widget = QWidget()
            self.central_widget.setLayout(self.layout)
            self.setCentralWidget(self.central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())