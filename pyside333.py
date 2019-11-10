import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.setWindowTitle('form')
        self.resize(250, 150)
        self.move(300, 300)

        self.label = QLabel('Введите числа')
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.button = QPushButton('Вычислить сумму')

        self.button.clicked.connect(self.greetings)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.edit1)
        self.layout.addWidget(self.edit2)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def greetings(self):
        self.label.setText('{}'.format(float(self.edit1.text())+float(self.edit2.text())))

if __name__ == '__main__':
    app = QApplication()

    form = Form()
    form.show()

    sys.exit(app.exec_())