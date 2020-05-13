from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from initializer import Initializer

import random
import datetime
import config
import numpy as np
import fileinput


class AppMainWindow(QMainWindow):
    def __init__(self):
        # Main window
        super(AppMainWindow, self).__init__()

        self.pdList = ['True', 'False']
        self.dpAlgo = ['Gamma', 'Laplace']

        self.setObjectName("MainWindow")
        self.resize(1000, 700)

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.simOutput = QPlainTextEdit(self.centralwidget)
        self.simOutput.setObjectName("simOutput")
        self.horizontalLayout.addWidget(self.simOutput)
        self.setCentralWidget(self.centralwidget)

        # Menu bar
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)

        # Status bar
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # DockWidget
        self.dockWidget = QDockWidget(self)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        # Group box
        self.groupBox = QGroupBox(self.dockWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QFrame(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout_2 = QFormLayout(self.frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)
        self.num_server = QLineEdit(self.frame)
        self.num_server.setObjectName("num_server")
        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.num_server)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)
        self.num_client = QLineEdit(self.frame)
        self.num_client.setObjectName("num_client")
        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.num_client)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)
        self.num_iterations = QLineEdit(self.frame)
        self.num_iterations.setObjectName("num_iterations")
        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.num_iterations)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)
        self.lenPerIteration = QLineEdit(self.frame)
        self.lenPerIteration.setObjectName("lenPerIteration")
        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lenPerIteration)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_5)
        self.lengthOfDataset = QLineEdit(self.frame)
        self.lengthOfDataset.setObjectName("lengthOfDataset")
        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lengthOfDataset)
        self.verticalLayout_2.addWidget(self.frame)
        self.groupBox_3 = QGroupBox(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName("formLayout")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_10)

        # Use privacy policy
        self.useDpPrivacy = QComboBox(self.groupBox_3)
        self.useDpPrivacy.addItems(self.pdList)
        self.useDpPrivacy.setCurrentIndex(1)
        self.useDpPrivacy.setObjectName("useDpPrivacy")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.useDpPrivacy)
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        # privacyAlgo
        self.privacyAlgo = QComboBox(self.groupBox_3)
        self.privacyAlgo.addItems(self.dpAlgo)
        self.privacyAlgo.setCurrentIndex(0)
        self.privacyAlgo.setObjectName("privacyAlgo")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.privacyAlgo)
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)
        self.epsilon = QLineEdit(self.groupBox_3)
        self.epsilon.setObjectName("epsilon")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.epsilon)
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)
        self.alpha = QLineEdit(self.groupBox_3)
        self.alpha.setObjectName("alpha")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.alpha)
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_9)
        self.mean = QLineEdit(self.groupBox_3)
        self.mean.setObjectName("mean")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.mean)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.frame_2 = QFrame(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnSaveParams = QPushButton(self.frame_2)
        self.btnSaveParams.clicked.connect(self.save_app_config)
        self.btnSaveParams.clicked()
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSaveParams.sizePolicy().hasHeightForWidth())
        self.btnSaveParams.setSizePolicy(sizePolicy)
        self.btnSaveParams.setObjectName("btnSaveParams")
        self.horizontalLayout_3.addWidget(self.btnSaveParams)

        # Button Edit All Config
        self.btnEditAllConfig = QPushButton(self.frame_2)
        self.btnEditAllConfig.setObjectName("btnEditAllConfig")
        self.horizontalLayout_3.addWidget(self.btnEditAllConfig)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.dockWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnRunSim = QPushButton(self.groupBox_2)
        self.btnRunSim.setMaximumSize(QSize(16777215, 32))
        self.btnRunSim.setObjectName("btnRunSim")
        self.btnRunSim.clicked.connect(self.run_simulation)
        self.horizontalLayout_2.addWidget(self.btnRunSim)
        self.btnStopSim = QPushButton(self.groupBox_2)
        self.btnStopSim.setObjectName("btnStopSim")
        self.horizontalLayout_2.addWidget(self.btnStopSim)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.addDockWidget(Qt.DockWidgetArea(1), self.dockWidget)
        self.actionRun_Simulation = QAction(self)
        self.actionRun_Simulation.setCheckable(False)
        self.actionRun_Simulation.setObjectName("actionRun_Simulation")
        self.actionExit = QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_Application = QAction(self)
        self.actionExit_Application.setObjectName("actionExit_Application")
        self.actionExit_2 = QAction(self)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menuFile.addAction(self.actionRun_Simulation)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_Application)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslate_ui()
        QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle("PrivacyFL v2.0")
        self.menuFile.setTitle("File")
        self.groupBox.setTitle("SimulationParameters")
        self.label.setText("No. of Servers")
        self.num_server.setText(str(config.NUM_SERVERS))
        self.label_2.setText("No. of Clients")
        self.num_client.setText(str(config.NUM_CLIENTS))
        self.label_3.setText("No. Iterations")
        self.num_iterations.setText(str(config.ITERATIONS))
        self.label_4.setText("Lenth per Iteration")
        self.lenPerIteration.setText(str(config.len_per_iteration))
        self.label_5.setText("Length of Dataset")
        self.lengthOfDataset.setText(str(config.LEN_TEST))
        self.groupBox_3.setTitle("Privacy Parameters")
        self.label_10.setText("Use DP Privacy")
        self.label_6.setText("Privacy Algorithm")
        self.label_7.setText("Epsilon")
        self.epsilon.setText(str(config.epsilon))
        self.label_8.setText("Alpha")
        self.alpha.setText(str(config.alpha))
        self.label_9.setText("Mean")
        self.mean.setText(str(config.mean))
        self.btnSaveParams.setText("Save Parameters")
        self.btnEditAllConfig.setText("Edit All Config")
        self.btnRunSim.setText("Run Simulation")
        self.btnStopSim.setText("Stop Simulation")
        self.actionRun_Simulation.setText("Run Simulation")
        self.actionExit.setText("Exit")
        self.actionExit_Application.setText("Exit Application")
        self.actionExit_2.setText("Exit")

    def run_simulation(self):
        random.seed(0)
        np.random.seed(0)
        initializer = Initializer(num_clients=config.NUM_CLIENTS, iterations=config.ITERATIONS,
                                  num_servers=config.NUM_SERVERS)
        # can use any amount of iterations less than config.ITERATIONS but the
        # initializer has only given each client config.ITERATIONS datasets for training.
        a = datetime.datetime.now()
        initializer.run_simulation(config.ITERATIONS, server_agent_name='server_agent0')
        b = datetime.datetime.now()

    def save_app_config(self):
        num_server = int(self.num_server.text())
        num_iterations = int(self.num_iterations.text())
        num_client = int(self.num_client.text())
        len_per_iteration = int(self.lenPerIteration.text())
        length_of_dataset = int(self.lengthOfDataset.text())
        epsilon = float(self.epsilon.text())
        alpha = int(self.alpha.text())
        mean = int(self.mean.text())
        use_dp_privacy = self.useDpPrivacy.currentText()
        privacy_algo = self.privacyAlgo.currentText()

        for line in fileinput.input("config.py", inplace=True):
            if 'NUM_CLIENTS' in line:
                if line.split()[0] == 'NUM_CLIENTS':
                    print('{} {}'.format('NUM_CLIENTS =',
                                         str(num_client) + '\n'), end='')
                else:
                    print('{}'.format(line), end='')

            elif 'NUM_SERVERS' in line:
                if line.split()[0] == 'NUM_SERVERS':
                    print('{} {}'.format('NUM_SERVERS =',
                                         str(num_server) + '\n'), end='')
                else:
                    print('{}'.format(line), end='')

            elif 'ITERATIONS' in line:
                if line.split()[0] == 'ITERATIONS':
                    print('{} {}'.format('ITERATIONS =',
                                         str(num_iterations) + '\n'), end='')
                else:
                    print('{}'.format(line), end='')

            elif 'len_per_iteration' in line:
                if line.split()[0] == 'len_per_iteration':
                    print('{} {}'.format('len_per_iteration =',
                                         str(len_per_iteration) + '\n'), end='')
                else:
                    print('{}'.format(line), end='')

            elif 'LEN_TEST' in line:
                if line.split()[0] == 'LEN_TEST':
                    print('{} {}'.format('LEN_TEST =',
                                         str(length_of_dataset) + '\n'), end='')
                else:
                    print('{}'.format(line), end='')

            elif 'epsilon' in line:
                if line.split()[0] == 'epsilon':
                    print('{} {}'.format('epsilon =',
                                         str(epsilon) + '\n'), end='')
                else:
                    print('{}'.format(line), end='')

            elif 'alpha' in line:
                if line.split()[0] == 'alpha':
                    print('{} {}'.format('alpha =',
                                         str(alpha) + '\n'), end='')
                else:
                    print('{}'.format(line), end='')

            elif 'mean' in line:
                if line.split()[0] == 'mean':
                    print('{} {}'.format('mean =',
                                         str(mean) + '\n'), end='')
                else:
                    print('{}'.format(line), end='')

            elif 'DP_ALGORITHM' in line:
                if line.split()[0] == 'DP_ALGORITHM':
                    print('{}'.format(
                        'DP_ALGORITHM = "' + privacy_algo + '"\n'), end='')
                else:
                    print('{}'.format(line), end='')

            elif 'USE_DP_PRIVACY' in line:
                if line.split()[0] == 'USE_DP_PRIVACY':
                    print('{} {}'.format('USE_DP_PRIVACY =',
                                         use_dp_privacy + '\n'), end='')
                else:
                    print('{}'.format(line), end='')

            else:
                print('{}'.format(line), end='')
