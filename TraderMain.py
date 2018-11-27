# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TraderMain.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(520, 660, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lblStockName = QtGui.QLabel(Dialog)
        self.lblStockName.setGeometry(QtCore.QRect(30, 40, 89, 25))
        self.lblStockName.setObjectName(_fromUtf8("lblStockName"))
        self.cmbStockSymbol = QtGui.QComboBox(Dialog)
        self.cmbStockSymbol.setEnabled(True)
        self.cmbStockSymbol.setGeometry(QtCore.QRect(200, 40, 60, 22))
        self.cmbStockSymbol.setCurrentText(_fromUtf8(""))
        self.cmbStockSymbol.setObjectName(_fromUtf8("cmbStockSymbol"))
        self.lblNewsPriceSource = QtGui.QLabel(Dialog)
        self.lblNewsPriceSource.setGeometry(QtCore.QRect(30, 90, 131, 16))
        self.lblNewsPriceSource.setObjectName(_fromUtf8("lblNewsPriceSource"))
        self.cmbNewsPriceSource = QtGui.QComboBox(Dialog)
        self.cmbNewsPriceSource.setGeometry(QtCore.QRect(200, 90, 211, 22))
        self.cmbNewsPriceSource.setCurrentText(_fromUtf8(""))
        self.cmbNewsPriceSource.setObjectName(_fromUtf8("cmbNewsPriceSource"))
        self.lblDateRange = QtGui.QLabel(Dialog)
        self.lblDateRange.setGeometry(QtCore.QRect(30, 140, 91, 16))
        self.lblDateRange.setObjectName(_fromUtf8("lblDateRange"))
        self.dateFrom = QtGui.QDateEdit(Dialog)
        self.dateFrom.setGeometry(QtCore.QRect(30, 180, 110, 22))
        self.dateFrom.setObjectName(_fromUtf8("dateFrom"))
        self.lblTo = QtGui.QLabel(Dialog)
        self.lblTo.setGeometry(QtCore.QRect(180, 180, 21, 16))
        self.lblTo.setObjectName(_fromUtf8("lblTo"))
        self.dateTo = QtGui.QDateEdit(Dialog)
        self.dateTo.setGeometry(QtCore.QRect(220, 180, 110, 22))
        self.dateTo.setObjectName(_fromUtf8("dateTo"))
        self.btnGenerateNewsPriceFile = QtGui.QPushButton(Dialog)
        self.btnGenerateNewsPriceFile.setGeometry(QtCore.QRect(30, 220, 141, 23))
        self.btnGenerateNewsPriceFile.setObjectName(_fromUtf8("btnGenerateNewsPriceFile"))
        self.btnSelectExistingFile = QtGui.QPushButton(Dialog)
        self.btnSelectExistingFile.setGeometry(QtCore.QRect(30, 280, 141, 23))
        self.btnSelectExistingFile.setObjectName(_fromUtf8("btnSelectExistingFile"))
        self.btnTrain = QtGui.QPushButton(Dialog)
        self.btnTrain.setGeometry(QtCore.QRect(30, 320, 141, 23))
        self.btnTrain.setObjectName(_fromUtf8("btnTrain"))
        self.btnTest = QtGui.QPushButton(Dialog)
        self.btnTest.setGeometry(QtCore.QRect(30, 360, 141, 23))
        self.btnTest.setObjectName(_fromUtf8("btnTest"))
        self.lblAccuracy = QtGui.QLabel(Dialog)
        self.lblAccuracy.setGeometry(QtCore.QRect(230, 320, 51, 16))
        self.lblAccuracy.setObjectName(_fromUtf8("lblAccuracy"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 420, 511, 121))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.txtAccuracy = QtGui.QLineEdit(Dialog)
        self.txtAccuracy.setGeometry(QtCore.QRect(290, 320, 101, 20))
        self.txtAccuracy.setObjectName(_fromUtf8("txtAccuracy"))
        self.lblTestResults = QtGui.QLabel(Dialog)
        self.lblTestResults.setGeometry(QtCore.QRect(30, 400, 111, 16))
        self.lblTestResults.setObjectName(_fromUtf8("lblTestResults"))
        self.btnHelp = QtGui.QPushButton(Dialog)
        self.btnHelp.setGeometry(QtCore.QRect(460, 560, 75, 23))
        self.btnHelp.setObjectName(_fromUtf8("btnHelp"))
        self.btnClose = QtGui.QPushButton(Dialog)
        self.btnClose.setGeometry(QtCore.QRect(370, 560, 75, 23))
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.btnReport = QtGui.QPushButton(Dialog)
        self.btnReport.setGeometry(QtCore.QRect(280, 560, 75, 23))
        self.btnReport.setObjectName(_fromUtf8("btnReport"))

        self.retranslateUi(Dialog)
        self.cmbStockSymbol.setCurrentIndex(-1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblStockName.setText(_translate("Dialog", "Stock Symbol", None))
        self.lblNewsPriceSource.setText(_translate("Dialog", "News and Price Source", None))
        self.lblDateRange.setText(_translate("Dialog", "Date Range", None))
        self.lblTo.setText(_translate("Dialog", "To", None))
        self.btnGenerateNewsPriceFile.setText(_translate("Dialog", "&Generate News-Price File", None))
        self.btnSelectExistingFile.setText(_translate("Dialog", "&Select Existing File", None))
        self.btnTrain.setText(_translate("Dialog", "&Train Algorithm", None))
        self.btnTest.setText(_translate("Dialog", "Execute &Correlation Test", None))
        self.lblAccuracy.setText(_translate("Dialog", "Accuracy", None))
        self.lblTestResults.setText(_translate("Dialog", "Correlation Results", None))
        self.btnHelp.setText(_translate("Dialog", "&Help", None))
        self.btnClose.setText(_translate("Dialog", "&Close", None))
        self.btnReport.setText(_translate("Dialog", "Report", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

