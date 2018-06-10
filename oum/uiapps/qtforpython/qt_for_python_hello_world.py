# hello_world.py
from PySide2.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Hello Qt for Python!")
label.show()
app.exec_()