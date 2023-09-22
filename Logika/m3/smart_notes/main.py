from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget,  QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)

import json

app = QApplication([])
window = QWidget()

field_text = QTextEdit()

lb_notes = QLabel('Список заміток')

lst_notes = QListWidget()

btn_note_create = QPushButton('Створити замітку')
btn_note_delete = QPushButton('Виділити замітку')
btn_note_save = QPushButton('Зберігти замітку')

lb_tags = QLabel('Список тегів')

lst_tags = QListWidget()

field_ефп = QTextEdit()
btn_tag_add = QPushButton('Додати тег')
btn_tag_unpin = QPushButton('Видалити тег')
btn_tag_search = QPushButton('Шукати замітки за тегом')

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)

col1.addWidget(field_text)

col2.addWidget(lb_notes)
col2.addWidget(lst_notes)

row1 = QHBoxLayout()
row1.addWidget(btn_note_create)
row1.addWidget(btn_note_delete)

col2.addLayout(row1)
col2.addLayout(btn_note_save)

def show_notes():
    key = lst_notes.selectedItems()[0].texr()
    field_text.setText(notes[key]['текст'])

lst_notes.itemClicked.connect(show_notes)

with open('notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

lst_notes.addItems(notes)

window.setLayout(layout_notes)
window.show()
app.exec_()