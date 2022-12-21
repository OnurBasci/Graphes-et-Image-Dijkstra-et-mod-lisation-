import numpy as np
from matplotlib import pyplot as plt

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import numpy as np


"""def on_button_clicked():
	alert = QMessageBox()
	alert.setText('You clicked the button!')
	alert.exec()"""

from random import choice


def gui():
	class MainWindow(QMainWindow):
		def __init__(self):
			super().__init__()
			self.title = 'PyQt5 textbox - pythonspot.com'
			self.left = 50
			self.top = 50
			self.width = 400
			self.height = 140
			self.initUI()

		def initUI(self):
			self.setWindowTitle(self.title)
			self.setGeometry(self.left, self.top, self.width, self.height)

			# Create textbox
			self.textbox = QLineEdit(self)
			self.textbox.move(20, 20)
			self.textbox.resize(280, 40)

			# Create a button in the window
			self.button = QPushButton('Show text', self)
			self.button.move(20, 80)

			# connect button to function on_click
			self.button.clicked.connect(self.on_click)
			self.show()

		@pyqtSlot()
		def on_click(self):
			textboxValue = self.textbox.text()
			QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
								 QMessageBox.Ok)
			self.textbox.setText("")

	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	app.exec()


def show(img, path):
	"""takes an numpy image array and draws the path"""
	img_cpy = np.copy(img)
	for couple in path:
		img_cpy[couple[0], couple[1]] = 150
	plt.matshow(img_cpy)
	plt.show()


def show_steps(img, path):
	"""takes an numpy image array and draws the path and aslo the steps"""
	img_cpy = np.copy(img)
	for couple in path:
		img_cpy[couple[0], couple[1]] = 150
		plt.matshow(img_cpy)
		plt.waitforbuttonpress(0)  # this will wait for indefinite time
		plt.close()
	plt.matshow(img_cpy)
	plt.show()