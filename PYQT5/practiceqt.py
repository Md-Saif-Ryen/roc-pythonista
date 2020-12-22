#=------------------------Main Window------------------------------
# from PyQt5.QtWidgets import QMainWindow,QApplication
# from PyQt5.QtGui import QIcon
# import sys
#
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyQt5 Main Window")
#         self.setGeometry(200,200,500,500)
#         self.setWindowIcon(QIcon("home.jpg"))
#
#         # self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     sys.exit(app.exec_())

#-----------------------PushButton with Signal and Event---------------------
# from PyQt5.QtWidgets import QDialog,QApplication,QPushButton,QLabel,QHBoxLayout
# from PyQt5.QtGui import QIcon,QFont
# from PyQt5.QtCore import QSize,QRect
# import sys
#
# class MyWindow(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyQt5 Main Window")
#         self.setGeometry(200,200,500,500)
#         self.setWindowIcon(QIcon("home.jpg"))
#
#         self.UiComponents()
#         self.show()
#
#
#     def UiComponents(self):
#         hbox = QHBoxLayout()
#
#         button = QPushButton("Enter", self)
#         button.setGeometry(QRect(200,200,111,28))
#         button.setFont(QFont("Sensarif", 13))
#         button.setIcon(QIcon("button.jpg"))
#         button.setIconSize(QSize(25,25))
#         button.setToolTip("Please Enter")
#         button.clicked.connect(self.Clicked)
#         hbox.addWidget(button)
#
#         self.label = QLabel(self)
#         hbox.addWidget(self.label)
#
#
#
#     def Clicked(self):
#         if button.isClicked(True):
#             self.label.setText("You have Entered")


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     sys.exit(app.exec_())

#------------------CheckBox------------------
# from PyQt5.QtWidgets import QDialog,QApplication,QLabel,QHBoxLayout,QVBoxLayout,QGroupBox,QCheckBox
# from PyQt5.QtGui import QIcon,QFont
# from PyQt5.QtCore import QSize,QRect
# import sys
#
#
# class MyWindow(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyQt5 Main Window")
#         self.setGeometry(200,200,450,100)
#         self.setWindowIcon(QIcon("home.jpg"))
#
#         self.UiComponents()
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.groupbox)
#         self.label = QLabel("hello")
#         self.label.setFont(QFont("Senserif",15))
#         vbox.addWidget(self.label)
#         self.setLayout(vbox)
#         self.show()
#
#     def UiComponents(self):
#         self.groupbox = QGroupBox("What is you favourite sport?")
#         self.groupbox.setFont(QFont("Senserif", 20))
#         hbox = QHBoxLayout()
#
#         self.check1 = QCheckBox("Football")
#         self.check1.setFont(QFont("Senserif", 13))
#         self.check1.toggled.connect(self.OnChecked)
#         self.check1.setIcon(QIcon("Football.jpg"))
#         self.check1.setIconSize(QSize(30,30))
#         hbox.addWidget(self.check1)
#
#         self.check2 = QCheckBox("Cricket")
#         self.check2.setFont(QFont("Senserif", 13))
#         self.check2.toggled.connect(self.OnChecked)
#         self.check2.setIcon(QIcon("Cricket.png"))
#         self.check2.setIconSize(QSize(40, 40))
#         hbox.addWidget(self.check2)
#
#         self.check3 = QCheckBox("Tennis")
#         self.check3.setFont(QFont("Senserif", 13))
#         self.check3.toggled.connect(self.OnChecked)
#         self.check3.setIcon(QIcon("Tennnis.jpg"))
#         self.check3.setIconSize(QSize(40, 40))
#         hbox.addWidget(self.check3)
#
#         self.groupbox.setLayout(hbox)
#
#     def OnChecked(self):
#         check = self.sender()
#         if check.isChecked():
#             self.label.setText("You have selected " + check.text())
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     sys.exit(app.exec_())



#-----------------------Radio Button--------------------

# from PyQt5.QtWidgets import QDialog,QApplication,QLabel,QHBoxLayout,QVBoxLayout,QGroupBox,QRadioButton
# from PyQt5.QtGui import QIcon,QFont,QPixmap
# from PyQt5.QtCore import QSize,QRect
# import sys
#
#
# class MyWindow(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyQt5 Main Window")
#         self.setGeometry(200,200,450,100)
#         self.setWindowIcon(QIcon("home.jpg"))
#
#         self.UiComponents()
#         vbox = QVBoxLayout()
#
#         vbox.addWidget(self.groupbox)
#         self.label = QLabel("Hello")
#         self.label.setFont(QFont("Senserif",15))
#         vbox.addWidget(self.label)
#         self.setLayout(vbox)
#
#
#
#         self.show()
#
#     def UiComponents(self):
#         self.groupbox = QGroupBox("What is you favourite sport?")
#         self.groupbox.setFont(QFont("Senserif", 20))
#         hbox = QHBoxLayout()
#
#         labelImage = QLabel()
#         labelImage.setText("Hello")
#         self.pixmap = QPixmap("bg.jpg")
#         labelImage.setPixmap(self.pixmap)
#         hbox.addWidget(labelImage)
#
#
#         self.Radiobtn1 = QRadioButton("Football")
#         self.Radiobtn1.setFont(QFont("Senserif", 13))
#         self.Radiobtn1.toggled.connect(self.OnChecked)
#         self.Radiobtn1.setIcon(QIcon("Football.jpg"))
#         self.Radiobtn1.setIconSize(QSize(30,30))
#         hbox.addWidget(self.Radiobtn1)
#
#         self.Radiobtn2 = QRadioButton("Cricket")
#         self.Radiobtn2.setFont(QFont("Senserif", 13))
#         self.Radiobtn2.toggled.connect(self.OnChecked)
#         self.Radiobtn2.setIcon(QIcon("Cricket.png"))
#         self.Radiobtn2.setIconSize(QSize(40, 40))
#         hbox.addWidget(self.Radiobtn2)
#
#         self.Radiobtn3 = QRadioButton("Tennis")
#         self.Radiobtn3.setFont(QFont("Senserif", 13))
#         self.Radiobtn3.toggled.connect(self.OnChecked)
#         self.Radiobtn3.setIcon(QIcon("Tennnis.jpg"))
#         self.Radiobtn3.setIconSize(QSize(40, 40))
#         hbox.addWidget(self.Radiobtn3)
#
#         self.groupbox.setLayout(hbox)
#
#     def OnChecked(self):
#         check = self.sender()
#         if check.isChecked():
#             self.label.setText("You have selected " + check.text())
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     sys.exit(app.exec_())



# ------------------QLineEdit0---------------------------


from PyQt5.QtWidgets import QDialog,QApplication,QLabel,QHBoxLayout,QLineEdit,QPushButton,QGroupBox,QVBoxLayout
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QSize,QRect
import sys


class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Main Window")
        self.setGeometry(200,200,450,100)
        self.setWindowIcon(QIcon("home.jpg"))

        self.UiComponents()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)
        self.setLayout(vbox)




        self.show()

    def UiComponents(self):
        self.groupbox = QGroupBox("This is it.!!!")
        self.groupbox.setFont(QFont("Senserif", 20))
        hbox = QHBoxLayout()

        self.qline = QLineEdit()
        self.qline.setFont(QFont("Senserif", 13))
        self.qline.returnPressed.connect(self.CmdLine)
        hbox.addWidget(self.qline)

        button = QPushButton(self)
        button.setIcon(QIcon("arrow.jpg"))
        button.setGeometry(QRect(40,40,111,28))
        hbox.addWidget(button)

        self.label = QLabel(self)
        self.label.setFont(QFont("Senserid", 15))
        hbox.addWidget(self.label)

        self.groupbox.setLayout(hbox,)

    def CmdLine(self):
        self.label.setText(self.qline.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())



#-----------------QButtonGroup---------------------

from PyQt5.QtWidgets import QDialog,QApplication,QLabel,QHBoxLayout,QPushButton,QGroupBox,QButtonGroup
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QSize,QRect
import sys

#
# class MyWindow(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyQt5 Main Window")
#         self.setGeometry(200,200,450,100)
#         self.setWindowIcon(QIcon("home.jpg"))
#
#         self.show()
#
#         hbox = QHBoxLayout()
#
#         self.label = QLabel(self)
#         self.label.setFont(QFont("Senserif", 15))
#         hbox.addWidget(self.label)
#
#         self.buttongroup = QButtonGroup()
#         self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)
#
#         button = QPushButton("Python")
#         button.setFont(QFont("Senserif", 15))
#         button.setIcon(QIcon("python.png"))
#         button.setIconSize(QSize(40,40))
#         self.buttongroup.addButton(button, 1)
#         hbox.addWidget(button)
#
#         button = QPushButton("Java")
#         button.setFont(QFont("Senserif", 15))
#         button.setIcon(QIcon("java.png"))
#         button.setIconSize(QSize(40, 40))
#         self.buttongroup.addButton(button, 2)
#         hbox.addWidget(button)
#
#         button = QPushButton("C")
#         button.setFont(QFont("Senserif", 15))
#         button.setIcon(QIcon("java.png"))
#         button.setIconSize(QSize(40, 40))
#         self.buttongroup.addButton(button, 3)
#         hbox.addWidget(button)
#
#         button = QPushButton("ruby")
#         button.setFont(QFont("Senserif", 15))
#         button.setIcon(QIcon("ruby.jpg"))
#         button.setIconSize(QSize(40, 40))
#         self.buttongroup.addButton(button, 4)
#         hbox.addWidget(button)
#
#         self.setLayout(hbox)
#
#     def on_button_clicked(self, id):
#         for button in self.buttongroup.buttons():
#             if button is self.buttongroup.button(id):
#                 self.label.setText(button.text() + " was clicked ")
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     sys.exit(app.exec_())
#
#


