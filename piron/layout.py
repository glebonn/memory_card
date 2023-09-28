from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

group = QGroupBox("Варіанти відповідей")

bgroup = QButtonGroup()

button1 = QPushButton("Меню")
button2 = QPushButton("Відпочити")
button3 = QPushButton("Відповісти")

vopros = QLabel("")

spin = QSpinBox()
spin.setValue(12)

v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
v_line3 = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
h_line4 = QHBoxLayout()

rb1 = QRadioButton("")
rb2 = QRadioButton("")
rb3 = QRadioButton("")
rb4 = QRadioButton("")

v_line1.addWidget(rb1)
v_line1.addWidget(rb2)
v_line2.addWidget(rb3)
v_line2.addWidget(rb4)
h_line1.addWidget(button1)
h_line1.addWidget(button2)
h_line1.addWidget(spin)
h_line2.addWidget(vopros)
h_line4.addWidget(button3)

h_line3.addLayout(v_line1)
h_line3.addLayout(v_line2)
v_line3.addLayout(h_line1)
v_line3.addLayout(h_line2)
v_line3.addLayout(group)
v_line3.addLayout(h_line4)

group.setLayout(h_line3)

bgroup.addButton(rb1)
bgroup.addButton(rb2)
bgroup.addButton(rb3)
bgroup.addButton(rb4)
