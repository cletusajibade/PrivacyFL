# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    pdList = ['True', 'False']
    dpAlgo = ['Gamma', 'Laplace']

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.simOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.simOutput.setObjectName("simOutput")
        self.horizontalLayout.addWidget(self.simOutput)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.num_server = QtWidgets.QLineEdit(self.frame)
        self.num_server.setObjectName("num_server")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.num_server)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.num_client = QtWidgets.QLineEdit(self.frame)
        self.num_client.setObjectName("num_client")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.num_client)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.num_iterations = QtWidgets.QLineEdit(self.frame)
        self.num_iterations.setObjectName("num_iterations")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.num_iterations)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lenPerIteraration = QtWidgets.QLineEdit(self.frame)
        self.lenPerIteraration.setObjectName("lenPerIteraration")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.lenPerIteraration)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lengthOfDataset = QtWidgets.QLineEdit(self.frame)
        self.lengthOfDataset.setObjectName("lengthOfDataset")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.lengthOfDataset)
        self.verticalLayout_2.addWidget(self.frame)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName("formLayout")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.useDpPrivacy = QtWidgets.QComboBox(self.groupBox_3)
        self.useDpPrivacy.addItems(self.pdList)
        self.useDpPrivacy.setCurrentIndex(1)
        self.useDpPrivacy.setObjectName("useDpPrivacy")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.useDpPrivacy)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.privacyAlgo = QtWidgets.QComboBox(self.groupBox_3)
        self.privacyAlgo.addItems(self.dpAlgo)
        self.privacyAlgo.setCurrentIndex(0)
        self.privacyAlgo.setObjectName("privacyAlgo")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.privacyAlgo)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.epsilon = QtWidgets.QLineEdit(self.groupBox_3)
        self.epsilon.setObjectName("epsilon")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.epsilon)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.alpha = QtWidgets.QLineEdit(self.groupBox_3)
        self.alpha.setObjectName("alpha")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.alpha)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.mean = QtWidgets.QLineEdit(self.groupBox_3)
        self.mean.setObjectName("mean")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.mean)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.frame_2 = QtWidgets.QFrame(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.saveParams = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.saveParams.sizePolicy().hasHeightForWidth())
        self.saveParams.setSizePolicy(sizePolicy)
        self.saveParams.setObjectName("saveParams")
        self.horizontalLayout_3.addWidget(self.saveParams)
        self.editAllConfig = QtWidgets.QPushButton(self.frame_2)
        self.editAllConfig.setObjectName("editAllConfig")
        self.horizontalLayout_3.addWidget(self.editAllConfig)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnRunSim = QtWidgets.QPushButton(self.groupBox_2)
        self.btnRunSim.setMaximumSize(QtCore.QSize(16777215, 32))
        self.btnRunSim.setObjectName("btnRunSim")
        self.btnRunSim.clicked.connect(self.runSim)
        self.horizontalLayout_2.addWidget(self.btnRunSim)
        self.stopSim = QtWidgets.QPushButton(self.groupBox_2)
        self.stopSim.setObjectName("stopSim")
        self.horizontalLayout_2.addWidget(self.stopSim)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionRun_Simulation = QtWidgets.QAction(MainWindow)
        self.actionRun_Simulation.setCheckable(False)
        self.actionRun_Simulation.setObjectName("actionRun_Simulation")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_Application = QtWidgets.QAction(MainWindow)
        self.actionExit_Application.setObjectName("actionExit_Application")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menuFile.addAction(self.actionRun_Simulation)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_Application)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PrivacyFL v2.0"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.groupBox.setTitle(_translate("MainWindow", "SimulationParamters"))
        self.label.setText(_translate("MainWindow", "No. of Server"))
        self.num_server.setText(_translate(
            "MainWindow", str(config.NUM_SERVERS)))
        self.label_2.setText(_translate("MainWindow", "No. of Clients"))
        self.num_client.setText(_translate(
            "MainWindow", str(config.NUM_CLIENTS)))
        self.label_3.setText(_translate("MainWindow", "No. Iterations"))
        self.num_iterations.setText(_translate(
            "MainWindow", str(config.ITERATIONS)))
        self.label_4.setText(_translate("MainWindow", "Lenth per Iteration"))
        self.lenPerIteraration.setText(_translate(
            "MainWindow", str(config.len_per_iteration)))
        self.label_5.setText(_translate("MainWindow", "Length of Dataset"))
        self.lengthOfDataset.setText(_translate(
            "MainWindow", str(config.LEN_TEST)))
        self.groupBox_3.setTitle(_translate(
            "MainWindow", "Privacy Parameters"))
        self.label_10.setText(_translate("MainWindow", "Use DP Privacy"))
        self.label_6.setText(_translate("MainWindow", "Privacy Algorithm"))
        self.label_7.setText(_translate("MainWindow", "Epsilon"))
        self.epsilon.setText(_translate("MainWindow", str(config.epsilon)))
        self.label_8.setText(_translate("MainWindow", "Alpha"))
        self.alpha.setText(_translate("MainWindow", str(config.alpha)))
        self.label_9.setText(_translate("MainWindow", str(config.mean)))
        self.mean.setText(_translate("MainWindow", "0"))
        self.saveParams.setText(_translate("MainWindow", "Save Parameters"))
        self.editAllConfig.setText(_translate("MainWindow", "Edit All Config"))
        self.btnRunSim.setText(_translate("MainWindow", "Run Simulation"))
        self.stopSim.setText(_translate("MainWindow", "Stop Simulation"))
        self.actionRun_Simulation.setText(
            _translate("MainWindow", "Run Simulation"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit_Application.setText(
            _translate("MainWindow", "Exit Application"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
