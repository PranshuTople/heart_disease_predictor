# -*- coding: utf-8 -*-
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 672, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem2)
        self.label_age = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_age.setObjectName("label_age")
        self.horizontalLayout_1.addWidget(self.label_age)
        self.spinBox_age = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_age.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_age.setObjectName("spinBox_age")
        self.horizontalLayout_1.addWidget(self.spinBox_age)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem3)
        self.label_gender = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_gender.setObjectName("label_gender")
        self.horizontalLayout_1.addWidget(self.label_gender)
        self.comboBox_gender = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_gender.sizePolicy().hasHeightForWidth())
        self.comboBox_gender.setSizePolicy(sizePolicy)
        self.comboBox_gender.setObjectName("comboBox_gender")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.horizontalLayout_1.addWidget(self.comboBox_gender)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.label_bp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_bp.setObjectName("label_bp")
        self.horizontalLayout_2.addWidget(self.label_bp)
        self.spinBox_bp = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_bp.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_bp.setMaximum(999)
        self.spinBox_bp.setObjectName("spinBox_bp")
        self.horizontalLayout_2.addWidget(self.spinBox_bp)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label_cp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_cp.setObjectName("label_cp")
        self.horizontalLayout_2.addWidget(self.label_cp)
        self.comboBox_cp = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_cp.sizePolicy().hasHeightForWidth())
        self.comboBox_cp.setSizePolicy(sizePolicy)
        self.comboBox_cp.setObjectName("comboBox_cp")
        self.comboBox_cp.addItem("")
        self.comboBox_cp.addItem("")
        self.comboBox_cp.addItem("")
        self.comboBox_cp.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_cp)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.label_chol = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_chol.setObjectName("label_chol")
        self.horizontalLayout_3.addWidget(self.label_chol)
        self.spinBox_chol = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_chol.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_chol.setMaximum(999)
        self.spinBox_chol.setObjectName("spinBox_chol")
        self.horizontalLayout_3.addWidget(self.spinBox_chol)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.label_fbs = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_fbs.setObjectName("label_fbs")
        self.horizontalLayout_3.addWidget(self.label_fbs)
        self.spinBox_fbs = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_fbs.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_fbs.setMaximum(999)
        self.spinBox_fbs.setObjectName("spinBox_fbs")
        self.horizontalLayout_3.addWidget(self.spinBox_fbs)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.label_restecg = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_restecg.setObjectName("label_restecg")
        self.horizontalLayout_4.addWidget(self.label_restecg)
        self.comboBox_restecg = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_restecg.setObjectName("comboBox_restecg")
        self.comboBox_restecg.addItem("")
        self.comboBox_restecg.addItem("")
        self.comboBox_restecg.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_restecg)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.label_maxhrt = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_maxhrt.setObjectName("label_maxhrt")
        self.horizontalLayout_4.addWidget(self.label_maxhrt)
        self.spinBox_maxhrt = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_maxhrt.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_maxhrt.setMaximum(999)
        self.spinBox_maxhrt.setObjectName("spinBox_maxhrt")
        self.horizontalLayout_4.addWidget(self.spinBox_maxhrt)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem16)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem17)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem18)
        self.label_exang = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_exang.setObjectName("label_exang")
        self.horizontalLayout_5.addWidget(self.label_exang)
        self.comboBox_exang = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_exang.sizePolicy().hasHeightForWidth())
        self.comboBox_exang.setSizePolicy(sizePolicy)
        self.comboBox_exang.setObjectName("comboBox_exang")
        self.comboBox_exang.addItem("")
        self.comboBox_exang.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_exang)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem19)
        self.label_oldpeak = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_oldpeak.setObjectName("label_oldpeak")
        self.horizontalLayout_5.addWidget(self.label_oldpeak)
        self.doubleSpinBox_oldpeak = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox_oldpeak.setMinimumSize(QtCore.QSize(50, 0))
        self.doubleSpinBox_oldpeak.setDecimals(1)
        self.doubleSpinBox_oldpeak.setObjectName("doubleSpinBox_oldpeak")
        self.horizontalLayout_5.addWidget(self.doubleSpinBox_oldpeak)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem20)
        self.label_thal = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_thal.setObjectName("label_thal")
        self.horizontalLayout_5.addWidget(self.label_thal)
        self.comboBox_thal = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_thal.setObjectName("comboBox_thal")
        self.comboBox_thal.addItem("")
        self.comboBox_thal.addItem("")
        self.comboBox_thal.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_thal)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem21)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem22)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem23)
        self.label_slope = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_slope.setObjectName("label_slope")
        self.horizontalLayout_6.addWidget(self.label_slope)
        self.comboBox_slope = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_slope.setObjectName("comboBox_slope")
        self.comboBox_slope.addItem("")
        self.comboBox_slope.addItem("")
        self.comboBox_slope.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_slope)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem24)
        self.label_coves = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_coves.setObjectName("label_coves")
        self.horizontalLayout_6.addWidget(self.label_coves)
        self.comboBox_coves = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_coves.setObjectName("comboBox_coves")
        self.comboBox_coves.addItem("")
        self.comboBox_coves.addItem("")
        self.comboBox_coves.addItem("")
        self.comboBox_coves.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_coves)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem25)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem26)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem27)
        self.analyseButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.analyseButton.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.analyseButton.setFont(font)
        self.analyseButton.setAutoFillBackground(False)
        self.analyseButton.setStyleSheet("background-color:green;\n"
"color:white;\n"
"border-radius:13px;\n"
"font:bold 14px;\n"
"padding: 6px;")
        self.analyseButton.setObjectName("analyseButton")
        self.horizontalLayout_7.addWidget(self.analyseButton)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem28)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem29 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem29)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.analyseButton.clicked.connect(self.show_result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Heart Disease Predictor"))
        MainWindow.setWindowIcon(QtGui.QIcon(appctxt.get_resource('icon.png')))
        self.label_title.setText(_translate("MainWindow", "Heart Disease Predictor"))
        self.label_age.setText(_translate("MainWindow", "Enter Age:"))
        self.label_gender.setText(_translate("MainWindow", "Gender:"))
        self.comboBox_gender.setPlaceholderText(_translate("MainWindow", "Select Gender"))
        self.comboBox_gender.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox_gender.setItemText(1, _translate("MainWindow", "Female"))
        self.label_bp.setText(_translate("MainWindow", "Resting Blood Pressure:"))
        self.label_cp.setText(_translate("MainWindow", "Chest Pain Type:"))
        self.comboBox_cp.setPlaceholderText(_translate("MainWindow", "Chest Pain Type"))
        self.comboBox_cp.setItemText(0, _translate("MainWindow", "Typical Angina"))
        self.comboBox_cp.setItemText(1, _translate("MainWindow", "Atypical Angina"))
        self.comboBox_cp.setItemText(2, _translate("MainWindow", "Non-anginal Pain"))
        self.comboBox_cp.setItemText(3, _translate("MainWindow", "Asymptomatic"))
        self.label_chol.setText(_translate("MainWindow", "Serum Cholestoral in mg/dl:"))
        self.label_fbs.setText(_translate("MainWindow", "Fasting Blood Sugar in mg/dl:"))
        self.label_restecg.setText(_translate("MainWindow", "Resting Electrocardiographic Results:"))
        self.comboBox_restecg.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_restecg.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_restecg.setItemText(2, _translate("MainWindow", "2"))
        self.label_maxhrt.setText(_translate("MainWindow", "Maximum Heart Rate Achieved:"))
        self.label_exang.setText(_translate("MainWindow", "Exercise Induced Angina:"))
        self.comboBox_exang.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_exang.setItemText(1, _translate("MainWindow", "No"))
        self.label_oldpeak.setText(_translate("MainWindow", "Oldpeak:"))
        self.label_thal.setText(_translate("MainWindow", "Thalassemia:"))
        self.comboBox_thal.setItemText(0, _translate("MainWindow", "Normal"))
        self.comboBox_thal.setItemText(1, _translate("MainWindow", "Fixed Defect"))
        self.comboBox_thal.setItemText(2, _translate("MainWindow", "Reversable Defect"))
        self.label_slope.setText(_translate("MainWindow", "Slope of the peak exercise ST segment"))
        self.comboBox_slope.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_slope.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_slope.setItemText(2, _translate("MainWindow", "2"))
        self.label_coves.setText(_translate("MainWindow", "Number of major vessels colored by Flourosopy"))
        self.comboBox_coves.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_coves.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_coves.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_coves.setItemText(3, _translate("MainWindow", "3"))
        self.analyseButton.setText(_translate("MainWindow", "Analyse Report"))

    def show_result(self):
        msg = QMessageBox()
        msg.setWindowTitle('Result of Analysis')
        msg.setWindowIcon(QtGui.QIcon(appctxt.get_resource('icon.png')))
        msg.setText('Congratulations! You will not have a Heart Disease :)')
        msg.setIcon(QMessageBox.Information)

        x = msg.exec_()

if __name__ == "__main__":
    import sys
    #app = QtWidgets.QApplication(sys.argv)
    appctxt = ApplicationContext()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(appctxt.app.exec_())
