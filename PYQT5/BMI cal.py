from PyQt5 import QtWidgets as widg
from PyQt5 import QtGui as gui
from PyQt5 import QtCore as core
import sys

class BMI(widg.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bass Mass Index(BMI)")
        self.setWindowIcon(gui.QIcon("My Music.png"))
        # self.setStyleSheet("background-color: rgb(50, 58, 255)")
        self.setMaximumSize(400,150)
        self.setLayout(widg.QVBoxLayout())
        self.bmi()



        self.show()


    def bmi(self):
        container = widg.QWidget()
        container.setLayout(widg.QGridLayout())

#Creating widgets
        self.label1 = widg.QLabel("Height(meters)")
        self.label1.setFont(gui.QFont("Montserrat", 14))
        self.line1 = widg.QLineEdit()
        self.label2 = widg.QLabel("Weight(Kg)")
        self.label2.setFont(gui.QFont("Montserrat", 14))
        self.label3 = widg.QLabel("BMI : ")
        self.label3.setFont(gui.QFont("Montserrat", 14))
        self.label4 = widg.QLabel(self)
        self.label4.setFont(gui.QFont("Montserrat", 14))
        self.line2 = widg.QLineEdit()
        self.btn_enter = widg.QPushButton("Enter", clicked = lambda : self.calc_bmi())
        self.btn_enter.setStyleSheet("Background-color:white\nBorder-top-color:red\nBorder-left-color:black")



#adding widgets to layout

        container.layout().addWidget(self.label1, 100,200)
        container.layout().addWidget(self.line1, 100, 400)
        container.layout().addWidget(self.label2, 200,200)
        container.layout().addWidget(self.line2, 200,400)
        container.layout().addWidget(self.label3, 250,200)
        container.layout().addWidget(self.label4, 250,400)
        container.layout().addWidget(self.btn_enter, 300,300)


        self.layout().addWidget(container)

    def calc_bmi(self):
        if self.line1.text()  and self.line2.text():
            self.label4.setText("")
            calculation = float(self.line2.text()) / float(self.line1.text()) ** 2
            self.label4.setText(str(calculation))
        else:
            pass





if __name__ == '__main__':
    app = widg.QApplication(sys.argv)
    calc = BMI()
    sys.exit(app.exec_())