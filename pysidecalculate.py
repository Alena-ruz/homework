import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.t=[]
        self.setWindowTitle("Калькулятор")
        self.setWindowTitle('form')
        self.resize(400, 400)
        self.move(300, 300)

        self.label1 = QLabel()
        self.label2 = QLabel('Ответ')
        self.button1 = QPushButton('1')
        self.button2 = QPushButton('2')
        self.button3 = QPushButton('3')
        self.button4 = QPushButton('4')
        self.button5 = QPushButton('5')
        self.button6 = QPushButton('6')
        self.button7 = QPushButton('7')
        self.button8 = QPushButton('8')
        self.button9 = QPushButton('9')
        self.button0 = QPushButton('0')
        self.buttonpl = QPushButton('+')
        self.buttonmi = QPushButton('-')
        self.buttonum = QPushButton('*')
        self.buttonde = QPushButton('/')
        self.buttonev = QPushButton('=')

        self.button1.clicked.connect(self.greetings1)
        self.button2.clicked.connect(self.greetings2)
        self.button3.clicked.connect(self.greetings3)
        self.button4.clicked.connect(self.greetings4)
        self.button5.clicked.connect(self.greetings2)
        self.button6.clicked.connect(self.greetings6)
        self.button7.clicked.connect(self.greetings7)
        self.button8.clicked.connect(self.greetings8)
        self.button9.clicked.connect(self.greetings9)
        self.button0.clicked.connect(self.greetings0)
        self.buttonpl.clicked.connect(self.greetingspl)
        self.buttonmi.clicked.connect(self.greetingsmi)
        self.buttonum.clicked.connect(self.greetingsum)
        self.buttonde.clicked.connect(self.greetingsde)
        self.buttonev.clicked.connect(self.greetingsev)

        self.layout = QGridLayout()

        self.layout.addWidget(self.label1,0,1)
        self.layout.addWidget(self.label2,1,1)
        self.layout.addWidget(self.buttonpl,2,0)
        self.layout.addWidget(self.buttonmi,3,0)
        self.layout.addWidget(self.buttonum,4,0)
        self.layout.addWidget(self.buttonde,5,0)
        self.layout.addWidget(self.buttonev,6,0)
        self.layout.addWidget(self.button1,2,1)
        self.layout.addWidget(self.button2,2,2)
        self.layout.addWidget(self.button3,2,3)
        self.layout.addWidget(self.button4,3,1)
        self.layout.addWidget(self.button5,3,2)
        self.layout.addWidget(self.button6,3,3)
        self.layout.addWidget(self.button7,4,1)
        self.layout.addWidget(self.button8,4,2)
        self.layout.addWidget(self.button9,4,3)
        self.layout.addWidget(self.button0,5,2)
        self.setLayout(self.layout)

    def greetings1(self):
        self.t.append(1)
        self.r = int("".join(map(str, self.t)))
        self.label1.setText('{}'.format(self.r))

    def greetings2(self):
        self.t.append(2)
        self.r =str("".join(map(str, self.t)))
        self.label1.setText('{}'.format(self.r))

    def greetings3(self):
        self.t.append(3)
        self.r = str("".join(map(str, self.t)))
        self.label1.setText('{}'.format(self.r))

    def greetings4(self):
        self.t.append(4)
        self.r = str("".join(map(str, self.t)))
        self.label1.setText('{}'.format(self.r))

    def greetings5(self):
        self.t.append(5)
        self.r = str("".join(map(str, self.t)))
        self.label1.setText('{}'.format(self.r))

    def greetings6(self):
        self.t.append(6)
        self.r = str("".join(map(str, self.t)))
        self.label1.setText('{}'.format(self.r))

    def greetings7(self):
        self.t.append(7)
        self.r = str("".join(map(str, self.t)))
        self.label1.setText('{}'.format(self.r))

    def greetings8(self):
        self.t.append(8)
        self.r = str("".join(map(str, self.t)))
        self.label1.setText('{}'.format(self.r))

    def greetings9(self):
        self.t.append(9)
        self.r = str("".join(map(str, self.t)))
        self.label1.setText('{}'.format(self.r))

    def greetings0(self):
        self.t.append(0)
        self.r = str("".join(map(str, self.t)))
        self.label1.setText('{}'.format(self.r))

    def greetingspl(self):
        self.t.append('+')
        self.r = str("".join(map(str, self.t)))
        self.label1.setText('{}'.format(self.r))

    def greetingsmi(self):
        self.t.append('-')
        self.r = str("".join(map(str, self.t)))
        self.label1.setText('{}'.format(self.r))

    def greetingsum(self):
        self.t.append('*')
        self.r = str("".join(map(str, self.t)))
        self.label1.setText('{}'.format(self.r))

    def greetingsde(self):
        self.t.append('/')
        self.r = str("".join(map(str, self.t)))
        self.label1.setText('{}'.format(self.r))

    def greetingsev(self):
        self.t = str("".join(map(str, self.t)))
        if not self.t.find('+')==-1:
            pl=self.t.find('+')
            int1=int(self.t[:pl])
            int2=int(self.t[(pl+1):])
            ev=int1+int2
            self.t=[]
            self.label2.setText('Ответ: {}'.format(ev))
        elif not self.t.find('-')==-1:
            pl = self.t.find('-')
            int1 = int(self.t[:pl])
            int2 = int(self.t[(pl + 1):])
            ev = int1 - int2
            self.t = []
            self.label2.setText('Ответ: {}'.format(ev))
        elif not self.t.find('*') == -1:
            pl = self.t.find('*')
            int1 = int(self.t[:pl])
            int2 = int(self.t[(pl + 1):])
            ev = int1 * int2
            self.t = []
            self.label2.setText('Ответ: {}'.format(ev))
        elif not self.t.find('/') == -1:
            pl = self.t.find('/')
            int1 = int(self.t[:pl])
            int2 = int(self.t[(pl + 1):])
            ev = int1 / int2
            self.t = []
            self.label2.setText('Ответ: {}'.format(ev))
        else:
            self.t=[]

if __name__ == '__main__':
    app = QApplication()

    form = Form()
    form.show()

    sys.exit(app.exec_())