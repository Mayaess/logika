from PyQt5.Qt import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

from random import randint

app = QApplication([])
main_window = QWidget()

text = QLabel("Натисни щоб дізнатись переможця")
winner = QLabel('?')
button = QPushButton('Згенерувати')

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)

def win():
    ran = randint(1, 100)
    winner.setText(str(ran))

button.clicked.connect(win)

main_window.setLayout(line)
main_window.show()

app.exec_()
