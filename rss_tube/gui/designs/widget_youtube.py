# Form implementation generated from reading ui file 'rss_tube/gui/designs\widget_youtube.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(601, 479)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_thumbnail = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_thumbnail.sizePolicy().hasHeightForWidth())
        self.label_thumbnail.setSizePolicy(sizePolicy)
        self.label_thumbnail.setMinimumSize(QtCore.QSize(480, 270))
        self.label_thumbnail.setMaximumSize(QtCore.QSize(480, 270))
        self.label_thumbnail.setMouseTracking(True)
        self.label_thumbnail.setText("")
        self.label_thumbnail.setObjectName("label_thumbnail")
        self.horizontalLayout_3.addWidget(self.label_thumbnail)
        self.frame_3 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 270))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 270))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_title = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setText("")
        self.label_title.setWordWrap(True)
        self.label_title.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_meta = QtWidgets.QFormLayout()
        self.formLayout_meta.setObjectName("formLayout_meta")
        self.label_static_meta_author = QtWidgets.QLabel(self.frame)
        self.label_static_meta_author.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_static_meta_author.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_static_meta_author.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_static_meta_author.setObjectName("label_static_meta_author")
        self.formLayout_meta.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_static_meta_author)
        self.label_meta_author = QtWidgets.QLabel(self.frame)
        self.label_meta_author.setText("")
        self.label_meta_author.setOpenExternalLinks(True)
        self.label_meta_author.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_meta_author.setObjectName("label_meta_author")
        self.formLayout_meta.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_meta_author)
        self.label_static_meta_website = QtWidgets.QLabel(self.frame)
        self.label_static_meta_website.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_static_meta_website.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_static_meta_website.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_static_meta_website.setObjectName("label_static_meta_website")
        self.formLayout_meta.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_static_meta_website)
        self.label_meta_website = QtWidgets.QLabel(self.frame)
        self.label_meta_website.setText("")
        self.label_meta_website.setOpenExternalLinks(True)
        self.label_meta_website.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_meta_website.setObjectName("label_meta_website")
        self.formLayout_meta.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_meta_website)
        self.label_static_meta_views = QtWidgets.QLabel(self.frame)
        self.label_static_meta_views.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_static_meta_views.setObjectName("label_static_meta_views")
        self.formLayout_meta.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_static_meta_views)
        self.label_meta_views = QtWidgets.QLabel(self.frame)
        self.label_meta_views.setText("")
        self.label_meta_views.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_meta_views.setObjectName("label_meta_views")
        self.formLayout_meta.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_meta_views)
        self.horizontalLayout_2.addLayout(self.formLayout_meta)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pb_audio = QtWidgets.QPushButton(self.frame)
        self.pb_audio.setMinimumSize(QtCore.QSize(35, 35))
        self.pb_audio.setMaximumSize(QtCore.QSize(35, 16777215))
        self.pb_audio.setText("")
        self.pb_audio.setObjectName("pb_audio")
        self.gridLayout_2.addWidget(self.pb_audio, 1, 3, 1, 1)
        self.pb_play = QtWidgets.QPushButton(self.frame)
        self.pb_play.setMinimumSize(QtCore.QSize(90, 35))
        self.pb_play.setObjectName("pb_play")
        self.gridLayout_2.addWidget(self.pb_play, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.label_player_status = QtWidgets.QLabel(self.frame)
        self.label_player_status.setText("")
        self.label_player_status.setObjectName("label_player_status")
        self.gridLayout_2.addWidget(self.label_player_status, 1, 1, 1, 1)
        self.label_date = QtWidgets.QLabel(self.frame)
        self.label_date.setText("")
        self.label_date.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_date.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_date.setObjectName("label_date")
        self.gridLayout_2.addWidget(self.label_date, 0, 0, 1, 4)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_description = QtWidgets.QTextBrowser(self.frame)
        self.label_description.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_description.sizePolicy().hasHeightForWidth())
        self.label_description.setSizePolicy(sizePolicy)
        self.label_description.setMinimumSize(QtCore.QSize(0, 40))
        self.label_description.setReadOnly(True)
        self.label_description.setOpenExternalLinks(True)
        self.label_description.setObjectName("label_description")
        self.verticalLayout.addWidget(self.label_description)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_static_meta_author.setText(_translate("Form", "Author"))
        self.label_static_meta_website.setText(_translate("Form", "Website"))
        self.label_static_meta_views.setText(_translate("Form", "Views"))
        self.pb_audio.setToolTip(_translate("Form", "Play audio only"))
        self.pb_play.setText(_translate("Form", "Play"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
