
''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
app = QApplication([])

btn_OK = QPushButton('Відповісти')
btn_sleep = QPushButton('Відпочити')
btn_menu = QPushButton('Меню')


lb_question = QLabel('')

box_minutes = QSpinBox()
box_minutes.setValue(5)

RadioGroupBox = QGroupBox("Варіанти відповідей")

RadioGroup = QButtonGroup()

radio_btn1 = QRadioButton('')
radio_btn2 = QRadioButton('')
radio_btn3 = QRadioButton('')
radio_btn4 = QRadioButton('')

RadioGroup.addButton(radio_btn1)
RadioGroup.addButton(radio_btn2)
RadioGroup.addButton(radio_btn3)
RadioGroup.addButton(radio_btn4)

layout_answer1 = QHBoxLayout()
layout_answer2 = QVBoxLayout()
layout_answer3 = QVBoxLayout()

layout_answer2.addWidget(radio_btn1)
layout_answer2.addWidget(radio_btn2)

layout_answer3.addWidget(radio_btn3)
layout_answer3.addWidget(radio_btn4)

layout_answer1.addLayout(layout_answer2)
layout_answer1.addLayout(layout_answer3)

RadioGroupBox.setLayout(layout_answer1)

AnsGroupBox = QGroupBox()
lb_result = QLabel('')
lb_correct = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignCenter, stretch=2)

AnsGroupBox.setLayout(layout_res)

AnsGroupBox.hide()

layout_card = QVBoxLayout()
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_sleep)
layout_line1.addWidget(box_minutes)
layout_line1.addWidget(QLabel('хвилин'))

layout_line2.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK)
layout_line4.addStretch(1)

layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
layout_card.addLayout(layout_line4)



# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно 
# кнопка прибирає вікно і повертає його після закінчення таймера
# введення кількості хвилин
# кнопка відповіді "Ок" / "Наступний"
# текст питання

# Опиши групу перемикачів

# Опиши панень з результатами

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card

# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
def show_result():
    ''' показати панель відповідей '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Наступне пититання")

def show_question():
    ''' показати панель запитань '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Відповісти")
    RadioGroup.setExclusive(False)
    radio_btn1.setChecked(False)
    radio_btn2.setChecked(False)
    radio_btn3.setChecked(False)
    radio_btn4.setChecked(False)
    RadioGroup.setExclusive(True)