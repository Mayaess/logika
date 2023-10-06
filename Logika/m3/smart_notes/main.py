from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget,  QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)

import json

def saveToFile():
    with open('notes.json', 'w', encoding='utf8') as file:
        json.dump(notes, file, ensure_ascii=False, sort_keys=True, indent=4)

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

field_tag = QLineEdit()
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
col2.addWidget(btn_note_save)

col2.addWidget(lb_tags)
col2.addWidget(lst_tags)

col2.addWidget(field_tag)

row2 = QHBoxLayout()
row2.addWidget(btn_tag_add)
row2.addWidget(btn_tag_unpin)

col2.addLayout(row2)
col2.addWidget(btn_tag_search)


def show_note():
    key = lst_notes.currentItem().text()
    field_text.setText(notes[key]['текст'])

    lst_tags.clear()
    lst_tags.addItems(notes[key]['теги'])

def save_note():
    key = lst_notes.currentItem().text()
    notes[key]['текст'] = field_text.toPlainText()

    saveToFile()

def add_note():
    note_name, ok = QInputDialog.getText(window, "Створювання замітки", "Назва замітки")

    if note_name and ok:
        notes[note_name] = {'текст': '  ', "теги": []}
        lst_notes.addItem(note_name)


def delete_note():
    key = lst_notes.currentItem().text()
    del notes[key]
    saveToFile()

    field_text.clear()
    lst_tags.clear()
    lst_notes.clear()
    lst_notes.addItems(notes)

def add_tag():
    key = lst_notes.currentItem().text()
    tag = field_tag.text()

    notes[key]["теги"].append(tag)

    lst_tags.addItem(tag) 

    saveToFile()

def unpin_tag():
    key = lst_notes.currentItem().text()
    tag = lst_tags.currentItem().text()

    notes[key]["теги"].remove(tag)

    lst_tags.clear()
    lst_tags.addItems(notes[key]["теги"]) 


    saveToFile()



def search_tag():
    tag = field_tag.text()
    
    if 'Шукати замітки за тегом' == btn_tag_search.text():
        filtered_notes = {}

        for key in notes:
            if tag in notes[key]["теги"]:
                filtered_notes[key] = notes[key]

        btn_tag_search.setText('Скинути пошук')

        lst_notes.clear()
        lst_notes.addItems(filtered_notes)
        lst_tags.clear()
        field_text.clear()

    elif 'Скинути пошук' == btn_tag_search.text():
        btn_tag_search.setText('Шукати замітки за тегом' )

        lst_notes.clear()
        lst_notes.addItems(notes)
        lst_tags.clear()
        field_text.clear()



btn_tag_add.clicked.connect(add_tag)
btn_tag_unpin.clicked.connect(unpin_tag)
btn_tag_search.clicked.connect(search_tag)


lst_notes.itemClicked.connect(show_note)
btn_note_save.clicked.connect(save_note)
btn_note_delete.clicked.connect(delete_note)
btn_note_create.clicked.connect(add_note)

with open('notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

lst_notes.addItems(notes)

window.setLayout(layout_notes)
window.show()
app.exec_()