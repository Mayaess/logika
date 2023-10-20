import os# потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap  # оптимізована для показу на екрані картинка
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog, QLabel, 
    QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
)


#from PIL import Image, ImageFilter
#from PIL.ImageQt import ImageQt  # Для перенесення графіки з Pillow до QT
#from PIL.ImageFilter import SHARPEN

app = QApplication([])
main_win = QWidget()


btn_folder = QPushButton('Folder')
btn_left = QPushButton('Left')
btn_right = QPushButton('Right')
btn_flip = QPushButton('Flip')
btn_sharp = QPushButton('Sharp')
btn_bw = QPushButton('Bw')

lst_files = QListWidget()
lb_pic = QLabel('Picture')

layout_editor = QHBoxLayout()
row = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(lst_files)

row.addWidget(btn_left)
row.addWidget(btn_right)
row.addWidget(btn_flip)
row.addWidget(btn_sharp)
row.addWidget(btn_bw)

col2.addWidget(lb_pic)
col2.addLayout(row)

layout_editor.addLayout(col1)
layout_editor.addLayout(col2)

layout_editor.addLayout(col1, 1)
layout_editor.addLayout(col2, 4)

workdir = QFileDialog.getExistingDirectory()

print(workdir)

files_and_folders = os.listdir(workdir)

print(files_and_folders)

def filter(files):
    result = []
    ext = ['jpg', 'jpeg', 'bmp', 'gif', 'jfif', 'svg', 'png']

    for file in files:
        if file.split('.')[-1] in ext:
            result.append(file)

    return result

print(filter(files_and_folders))

main_win.setLayout(layout_editor)
main_win.show()
app.exec_()