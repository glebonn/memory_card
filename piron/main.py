from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

app = QApplication([])
wid = QWidget()
card_width, card_height = 600, 500
wid.setWindowTitle("Memory Card")
wid.resize(600, 500)
wid.move(0,0)



wid.setLayout(layout_card)
wid.show()
app.exec_()
