from pyQt.QtGui import *

class RadioButtonWidget(QWidget):
    """Radio Buttons"""

    def __init__(self,label,instruction,button_list):
        super().__init__()

        self.title_label = QLabel(label)
        self.radio_group_box = QGroupBox(instruction)
        self.radio_button_group = QButtonGroup()

        self.radio_button_list = []
        for each in button_list:
            self.radio_button_list.append(QRadioButton(each))

        self.radio_button_list[0].setChecked(True)

        self.radio_button_layout = QVBoxLayout()

        counter = 1
        for each in self.radio_button_list:
            self.radio_button_layout.addWidget(each)
            self.radio_button_group.addButton(each)
            self.radio_button_group.setId(each,counter)
            counter += 1

        self.radio_group_box.setLayout(self.radio_button_layout)
