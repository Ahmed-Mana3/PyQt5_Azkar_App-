import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QCheckBox, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.counter = 0
        # main window
        self.setWindowTitle("2M3.com")
        self.setWindowIcon(QIcon("logo.ico"))
        self.setGeometry(350, 150, 1200, 700)
        # title
        self.title = QLabel("اني احبك في الله ❤️", self)
        # button1
        self.button = QPushButton("سبحان الله", self)
        # text under button
        self.textPlace = QLabel("أذكر الله يا ولد 👆", self)
        # chek box
        self.checkbox = QCheckBox("هل تريد البدء من جديد ؟", self)
        # group of radio buttons
        self.radio1 = QRadioButton("سبحان الله", self)
        self.radio2 = QRadioButton("الحمد لله", self)
        self.radio3 = QRadioButton("الله أكبر", self)
        self.button_group1 = QButtonGroup(self)
        # style function
        self.initUI()
        
    def initUI(self):
        # main window style
        self.setStyleSheet("background-color: gray;")
        # title bar style
        self.title.setGeometry(0, 0, self.width(), 100)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-size: 30px; background-color: black; color: Red;")
        # button style
        self.button.setGeometry(500, 250, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)
        # text under button style
        self.textPlace.setGeometry(500, 350, 200, 100)
        self.textPlace.setStyleSheet("font-size: 25px; font-weight: bold;")
        self.textPlace.setAlignment(Qt.AlignCenter)
        # check box style
        self.checkbox.setGeometry(900, 600, 300, 100)
        self.checkbox.setStyleSheet("font-size: 20px; ")
        self.checkbox.stateChanged.connect(self.on_check)
        # radio buttons style
        self.radio1.setGeometry(400, 100, 150, 100)
        self.radio2.setGeometry(550, 100, 150, 100)
        self.radio3.setGeometry(700, 100, 150, 100)
        self.setStyleSheet("QRadioButton{font-size: 20px;}")
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.radio1.toggled.connect(self.radio_changed)
        self.radio2.toggled.connect(self.radio_changed)
        self.radio3.toggled.connect(self.radio_changed)

    # function on_click  for button1
    def on_click(self):
        self.button.setStyleSheet("font-size: 30px; color: Red")
        if self.counter <= 32:
            self.counter += 1
        else:
            self.counter = 0
            self.button.setStyleSheet("font-size: 30px; color: black")
        self.textPlace.setText(f"{self.counter}")
    
    # function on_check for the checkbox
    def on_check(self, state):
        self.button.setEnabled(True)
        self.radio_changed()
        self.button.setStyleSheet("font-size: 30px;")
        self.textPlace.setText("أذكر الله يا ولد 👆")
        self.textPlace.setStyleSheet("font-size: 25px; font-weight: bold;")
        self.counter = 0
        
    # function radio_changed for radio buttons
    def radio_changed(self):
        self.counter = 0
        self.textPlace.setText("أذكر الله يا ولد 👆")
        self.button.setStyleSheet("font-size: 30px; color: black")
        if self.radio1.isChecked():
            self.button.setText("سبحان الله")
        elif self.radio2.isChecked():
            self.button.setText("الحمد لله")
        elif self.radio3.isChecked():
            self.button.setText("الله أكبر")
      
# main function
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# if running the file
if __name__ == "__main__":
    main()





