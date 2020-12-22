import PyQt5.QtWidgets as qwt
import sys

"""
For the logic of calculator, I will create a function that will store all the first input into a list 
and when an operator is called, all the input after that will be stored in another list and when enter is press I will create yet
another method that will join all the elements of both the list seperately and apply the given operator and setText the result into
the result field and A method that will erase both list when clear button is clicked"""


class MyWindow(qwt.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setMaximumSize(300, 300)

        self.setLayout(qwt.QVBoxLayout())
        self.temp_nums = []
        self.fin_nums = []
        self.mycal()
        self.show()

    def mycal(self):
        container = qwt.QWidget()
        container.setLayout(qwt.QGridLayout())

        # Buttons
        self.result_field = qwt.QLineEdit()
        clear = qwt.QPushButton("Clear", clicked=lambda: self.clear_calc())
        enter = qwt.QPushButton("Enter", clicked=lambda: self.func_result())
        btn_1 = qwt.QPushButton("1", clicked=lambda: self.func_press("1"))
        btn_2 = qwt.QPushButton("2", clicked=lambda: self.func_press("2"))
        btn_3 = qwt.QPushButton("3", clicked=lambda: self.func_press("3"))
        btn_4 = qwt.QPushButton("4", clicked=lambda: self.func_press("4"))
        btn_5 = qwt.QPushButton("5", clicked=lambda: self.func_press("5"))
        btn_6 = qwt.QPushButton("6", clicked=lambda: self.func_press("6"))
        btn_7 = qwt.QPushButton("7", clicked=lambda: self.func_press("7"))
        btn_8 = qwt.QPushButton("8", clicked=lambda: self.func_press("8"))
        btn_9 = qwt.QPushButton("9", clicked=lambda: self.func_press("9"))
        btn_0 = qwt.QPushButton("0", clicked=lambda: self.func_press("0"))
        btn_back = qwt.QPushButton("Backspace", clicked=lambda: self.backspace())

        # Operators
        btn_add = qwt.QPushButton("+", clicked=lambda: self.num_press("+"))
        btn_min = qwt.QPushButton("-", clicked=lambda: self.num_press("-"))
        btn_mul = qwt.QPushButton("x", clicked=lambda: self.num_press("*"))
        btn_div = qwt.QPushButton("/", clicked=lambda: self.num_press("/"))

        # Adding buttons to the GridLayout
        container.layout().addWidget(self.result_field, 0, 0, 1, 4)
        container.layout().addWidget(enter, 1, 0, 1, 2)
        container.layout().addWidget(clear, 1, 2, 1, 2)
        container.layout().addWidget(btn_9, 2, 0)
        container.layout().addWidget(btn_8, 2, 1)
        container.layout().addWidget(btn_7, 2, 2)
        container.layout().addWidget(btn_6, 3, 0)
        container.layout().addWidget(btn_5, 3, 1)
        container.layout().addWidget(btn_4, 3, 2)
        container.layout().addWidget(btn_3, 4, 0)
        container.layout().addWidget(btn_2, 4, 1)
        container.layout().addWidget(btn_1, 4, 2)
        container.layout().addWidget(btn_add, 3, 3)
        container.layout().addWidget(btn_min, 4, 3)
        container.layout().addWidget(btn_mul, 5, 3)
        container.layout().addWidget(btn_div, 5, 2)
        container.layout().addWidget(btn_0, 5, 0, 1, 2)
        container.layout().addWidget(btn_back, 2, 3)

        self.layout().addWidget(container)

    def func_press(self, Key_number):

        if len(self.temp_nums) == 1 and "0" in self.temp_nums:
            self.temp_nums[0] = Key_number
        else:
            self.temp_nums.append(Key_number)
        temp_string = "".join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText("".join(self.fin_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def num_press(self, Operator):
        temp_string = "".join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append((Operator))
        self.temp_nums = []
        self.result_field.setText("".join(self.fin_nums))

    def func_result(self):
        fin_string = "".join(self.fin_nums) + "".join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += "="
        fin_string += str(result_string)
        self.result_field.setText(fin_string)

    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []

    def backspace(self):
        if self.temp_nums:
            self.temp_nums.pop()
        else:
            self.fin_nums.pop()
        temp_string = "".join(self.fin_nums) + "".join(self.temp_nums)
        self.result_field.setText(temp_string)


print("hello motherfather")
if __name__ == "__main__":
    app = qwt.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
