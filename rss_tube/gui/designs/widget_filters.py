# Form implementation generated from reading ui file 'rss_tube/gui/designs\widget_filters.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_new = QtWidgets.QPushButton(Form)
        self.pb_new.setObjectName("pb_new")
        self.verticalLayout.addWidget(self.pb_new)
        self.pb_edit = QtWidgets.QPushButton(Form)
        self.pb_edit.setObjectName("pb_edit")
        self.verticalLayout.addWidget(self.pb_edit)
        self.pb_delete = QtWidgets.QPushButton(Form)
        self.pb_delete.setObjectName("pb_delete")
        self.verticalLayout.addWidget(self.pb_delete)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(0, 5))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.pb_top = QtWidgets.QPushButton(Form)
        self.pb_top.setObjectName("pb_top")
        self.verticalLayout.addWidget(self.pb_top)
        self.pb_up = QtWidgets.QPushButton(Form)
        self.pb_up.setObjectName("pb_up")
        self.verticalLayout.addWidget(self.pb_up)
        self.pb_down = QtWidgets.QPushButton(Form)
        self.pb_down.setObjectName("pb_down")
        self.verticalLayout.addWidget(self.pb_down)
        self.pb_bottom = QtWidgets.QPushButton(Form)
        self.pb_bottom.setObjectName("pb_bottom")
        self.verticalLayout.addWidget(self.pb_bottom)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pb_new.setText(_translate("Form", "New"))
        self.pb_edit.setText(_translate("Form", "Edit"))
        self.pb_delete.setText(_translate("Form", "Delete"))
        self.pb_top.setText(_translate("Form", "Move to Top"))
        self.pb_up.setText(_translate("Form", "Move Up"))
        self.pb_down.setText(_translate("Form", "Move Down"))
        self.pb_bottom.setText(_translate("Form", "Move to Bottom"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
