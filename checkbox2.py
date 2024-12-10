from PyQt5 import QtWidgets
import js

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = js.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.sum)
        self.ui.pushButton_2.clicked.connect(self.clear)
        
    def sum(self):
        try:
            a = float(self.ui.checkBox.text())
            b = float(self.ui.checkBox_2.text())
            e = a * b
            
            if self.ui.checkBox.isChecked():
                e *= 2
            if self.ui.checkBox_2.isChecked():
                e /= 2
            if self.ui.checkBox_3.isChecked():
                e *= e

            self.ui.label_2.setText(f'Площадь: {e}')
        except:
            QtWidgets.QMessageBox.critical(window, 'Error', 'Неверный выбор', buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)
    
    def clear(self):
        self.ui.lineEdit_2.clear
        self.ui.lineEdit.clear
        self.ui.checkBox.setChecked(False)
        self.ui.checkBox_2.setChecked(False)
        self.ui.checkBox_3.setChecked(False)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

#Gaisin ebiDoebi horoshie sushi (bi4 legendarniy - set rollov)