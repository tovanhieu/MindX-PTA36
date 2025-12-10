import sys
from PyQt6.QtWidgets import (
    QApplication, QCheckBox, QComboBox,
    QDateEdit, QFontComboBox, QLineEdit,
    QMainWindow, QPushButton, QRadioButton,
    QSlider, QSpinBox, QVBoxLayout, QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):    
        super().__init__()
        self.setWindowTitle("Book Management App")
        
        self.layout = QVBoxLayout()

        # Sửa danh sách widget
        self.widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QFontComboBox,
            QLineEdit,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QCheckBox
        ]

        # Thêm widget vào layout
        for w in self.widgets:
            if w == QPushButton:
                self.layout.addWidget(w("Button"))  # thêm label cho button
            else:
                self.layout.addWidget(w())

        # Thiết lập widget trung tâm
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
