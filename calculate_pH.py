import numpy as np
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		uic.loadUi('calculate_pH.ui', self)
		self.buttonCalculate.clicked.connect(self.calculate_pH)

	def calculate_pH(self):
		'''
		Calculates the pH of a solution. It takes the value of the concentration in the label concentration

		-- Update
		The value of the pH in the label solution 
		'''
		
		# Gets the value from concentration and converts into a float
		self.concentration = float(self.inputValue.text())
		# calculates the pH
		self.pH = -np.round(np.log10(self.concentration), 2)
		# Set the label solution to pH
		self.labelSolution.setText(str(self.pH))

		# updates the value of the label solution
		self.update()

	def update(self):
		'''
		Updates the values of the labels
		'''
		# updates label solution
		self.labelSolution.adjustSize()
		
		
def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec())
	
window()