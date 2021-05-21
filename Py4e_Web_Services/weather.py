import sys
from PyQt5.QtWidgets import *
import subprocess

app = QApplication([])
app.setStyleSheet("QPushButton { margin: 10ex; }")
button = QPushButton('Get Quote')

def on_button_clicked():
    alert = QMessageBox()
    subprocess.call('test.py', shell=True)
    alert.exec()

button.clicked.connect(on_button_clicked)
button.show()
app.exec()

