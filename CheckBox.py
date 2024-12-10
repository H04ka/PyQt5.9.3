from PyQt5 import QtWidgets
import jk

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = jk.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.checker)
        self.ui.pushButton_2.clicked.connect(self.clear)

    def checker(self):
       
            if self.ui.checkBox.isChecked():
                self.ui.label.setText("Здарова")
            if self.ui.checkBox.isChecked and self.ui.checkBox_2.isChecked():
                self.ui.label.setText("Здарова X2")
            if self.ui.checkBox_2.isChecked():
               self.ui.label_2.setText("Пока ")
            if self.ui.checkBox.isChecked and self.ui.checkBox_2.isChecked and self.ui.checkBox_3.isChecked():
                self.ui.label.setText("Ulta pudga")
                self.ui.label_2.setText("Ulta pudga")
                self.ui.label_3.setText("Ulta pudga")
            else:
                QtWidgets.QMessageBox.critical(window, 'Invalid choose', 'выберите любой пункт', buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)
    
    def clear(self):
        self.ui.checkBox.setChecked(False)
        self.ui.checkBox_2.setChecked(False)
        self.ui.checkBox_3.setChecked(False)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())