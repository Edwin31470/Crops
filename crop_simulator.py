import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CropWindow(QMainWindow):
    """Crop Window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator")
        self.create_layout()                            

    def create_layout(self):
        #Create Widgets
        self.text_box = QLineEdit()
        self.button = QPushButton("Submit")
        self.label = QLabel("Please enter your name")
        #Create Layouts
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        #Create Central Widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        #Connections
        self.button.clicked.connect(self.display_name)

    def display_name(self):
        name = self.text_box.text()
        self.label.setText("Hello {0}".format(name))
        
if __name__ == "__main__":
    crop_simulation = QApplication(sys.argv)
    window = CropWindow()
    window.show()
    window.raise_()
    crop_simulation.exec_()
    

