import numpy as np
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		uic.loadUi('calculate_pH.ui', self)
		self.buttonCalculate.clicked.connect(self.calculate_pH)

	def calculate_pH(self,):
		
		self.concentration = float(self.inputValue.text())
		self.pH = -np.round(np.log10(self.concentration), 2)
		self.labelSolution.setText(str(self.pH))
		self.update()

	def update(self):
		self.labelSolution.adjustSize()
		
		
def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec())
	
window()