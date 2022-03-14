from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

from run_alt import *

links = {'FootLocker 1': 'https://www.footlocker.com/apigate/products/search?query=mens%20shoes:relevance:gender:Men\'s&pageSize=1&currentPage=1',
    'FootLocker 2': 'https://www.footlocker.com/apigate/pages/category/shoes',
    'Champs': 'https://www.champssports.com/apigate/products/search?query=:relevance:styleDiscountPercent:SALE&currentPage=0&pageSize=5',
    'Final Score': 'https://www.final-score.com/apigate/pages/category/shoes'
} 

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Scanner")
        self.initUI()


    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Site:")
        self.label.move(25,25)

        self.cb = QtWidgets.QComboBox(self)
        self.cb.addItems(['Champs','FootLocker 1','FootLocker 2','Final Score'])
        self.cb.currentIndexChanged.connect(self.set_link)
        self.cb.move(25,50)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Discount:")
        self.label2.move(25,75)

        self.cb2 = QtWidgets.QComboBox(self)
        self.cb2.addItems(['None','5%', '10%', '15%', '20%', '25%', '30%', '35%','40%', '45%', '50%','55%', '60%', '65%', '70%','75%', '80%', '85%', '90%', '95%'])
        self.cb2.currentIndexChanged.connect(self.set_discount)
        self.cb2.move(25,100)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('Run')
        self.btn.pressed.connect(self.pressed_run)

        self.btn.move(150, 100)

    def set_link(self):
        self.link = links[self.cb.currentText()]
        self.label.setText(self.link)

    def set_discount(self):
        self.discount = self.cb2.currentText()

    def pressed_run(self):
        run(self.link,self.discount)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
