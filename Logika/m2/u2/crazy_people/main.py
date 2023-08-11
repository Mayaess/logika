from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton

app = QApplication([])
main_win = QWidget()

text = QLabel("Який зріст в Зеленського?")

radio_btn1 = QRadioButton("180")
radio_btn2 = QRadioButton("175")
radio_btn3 = QRadioButton("170")
radio_btn4 = QRadioButton("165")

line = QVBoxLayout()

hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()

hline1.addWidget(text, alignment=Qt.AlignCenter)
hline2.addWidget(radio_btn1, alignment=Qt.AlignCenter)
hline2.addWidget(radio_btn2, alignment=Qt.AlignCenter)
hline3.addWidget(radio_btn3, alignment=Qt.AlignCenter)
hline3.addWidget(radio_btn4, alignment=Qt.AlignCenter)

line.addLayout(hline1)
line.addLayout(hline2)
line.addLayout(hline3)

def win():
    victory = QMessageBox()
    victory.setText("Молодець")
    victory.exec_()

def lose():
    victory = QMessageBox()
    victory.setText("Неправильно")
    victory.exec_()

radio_btn3.clicked.connect(win)

radio_btn1.clicked.connect(lose)
radio_btn2.clicked.connect(lose)
radio_btn4.clicked.connect(lose)

main_win.setLayout(line)

main_win.show()
app.exec_()