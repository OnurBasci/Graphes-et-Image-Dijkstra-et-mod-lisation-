import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QFileDialog
from PyQt5.QtCore import Qt, QEvent
from PyQt5 import QtGui
from uiv5 import Ui_mainWindow

from util import toValuedGraphe, read_imag
from Astar import A_star
from interface import show, show_steps
from dijkstra import dijkstra


class MyMainWindow(QMainWindow, Ui_mainWindow):
	def __init__(self, parent=None):
		self.image_path = "default_img.png"
		self.graphe, self.img = toValuedGraphe(self.image_path, 1)
		super(MyMainWindow, self).__init__(parent)
		qApp.installEventFilter(self)
		self.setupUi(self)
		self.horizontalSlider.setValue(10)
		self.intensityValue = self.horizontalSlider.value()
		self.buttonChercher.clicked.connect(self.getFileName)
		self.buttonAstar.clicked.connect(self.setA_starActive)
		self.buttonDijkstra.clicked.connect(self.setDijkstraActive)
		self.show()


	def eventFilter(self, obj, event):
		if event.type() == QEvent.KeyPress:
			if event.key() == Qt.Key_Escape:
				self.close()
		return super(MyMainWindow, self).eventFilter(obj, event)

	def clickButton(self):
		sender = self.sender()
		self.statusBar().showMessage(sender.text() + ' was pressed')

	def getFileName(self):
		file_filter = 'Data File (*.png *.jpg *.jpeg);'
		response = QFileDialog.getOpenFileName(
			parent=self,
			caption='Select a data file',
			directory=os.getcwd(),
			filter=file_filter,
			initialFilter='Excel File (*.xlsx *.xls)'
		)
		#change the path
		self.image_path = response[0]
		#change the image label size
		self.img = read_imag(self.image_path)
		ratio = self.img.shape[0]/self.img.shape[1]
		self.imageLabel.resize(int(250 * 1/ratio), int(250 * ratio))
		# print the image
		self.imageLabel.setPixmap(QtGui.QPixmap(response[0]))
		return response[0]

	def setA_starActive(self):
		#get the intensity
		self.intensityValue = int(self.horizontalSlider.value()/10)

		#construct the graphe
		self.graphe, self.img = toValuedGraphe(self.image_path, self.intensityValue)

		start_point = (int(self.departEditX.text()), int(self.departEditX_2.text()))
		end_point = (int(self.departEditX_4.text()), int(self.departEditX_3.text()))

		#check if the input is valid
		if self.img.shape[0] <= start_point[0] or self.img.shape[1] <= start_point[1] or self.img.shape[0] <= end_point[0] or self.img.shape[1] <= end_point[1]:
			print(f"Les coordonnées sont superieurs à la taille de l'image ({self.img.shape[0]}, {self.img.shape[1]})")
			return

		start_int = start_point[0] * self.img.shape[1] + start_point[1]
		end_int = end_point[0] * self.img.shape[1] + end_point[1]


		path = A_star(start_int, end_int, self.graphe, self.img.shape[0], self.img.shape[1])

		#show
		if self.stepsButton.isChecked():
			show_steps(self.img, path)
		else:
			show(self.img, path)

	def setDijkstraActive(self):
		# get the intensity
		self.intensityValue = int(self.horizontalSlider.value() / 10)

		# get the coordinates
		start_point = (int(self.departEditX.text()), int(self.departEditX_2.text()))
		end_point = (int(self.departEditX_4.text()), int(self.departEditX_3.text()))

		# construct the graphe
		self.graphe, self.img = toValuedGraphe(self.image_path, self.intensityValue)

		# check if the input is valid
		if self.img.shape[0] <= start_point[0] or self.img.shape[1] <= start_point[1] or self.img.shape[0] <= end_point[0] or self.img.shape[1] <= end_point[1]:
			print(f"Les coordonnées sont superieurs à la taille de l'image ({self.img.shape[0]}, {self.img.shape[1]})")
			return

		start_int = start_point[0] * self.img.shape[1] + start_point[1]
		end_int = end_point[0] * self.img.shape[1] + end_point[1]

		path = dijkstra(self.graphe, start_int, end_int, self.img.shape[1])

		# show
		if self.stepsButton.isChecked():
			show_steps(self.img, path)
		else:
			show(self.img, path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    #test = TestClass()
    sys.exit(app.exec_())