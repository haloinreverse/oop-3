from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from matrix import Matrix


class TInterface(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.save_size_pb.clicked.connect(self.save_new_size)
        self.__matrix = Matrix()
        self.__size = 2
        self.save_matrix()


    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(800, 600)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.size_label = QLabel(self.centralwidget)
        self.size_label.setObjectName(u"size_label")

        self.gridLayout.addWidget(self.size_label, 0, 0, 1, 1)

        self.det_pb = QPushButton(self.centralwidget)
        self.det_pb.setObjectName(u"det_pb")

        self.gridLayout.addWidget(self.det_pb, 3, 1, 1, 1)

        self.size_le = QLineEdit(self.centralwidget)
        self.size_le.setObjectName(u"size_le")

        self.gridLayout.addWidget(self.size_le, 0, 1, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)

        self.transpose_pb = QPushButton(self.centralwidget)
        self.transpose_pb.setObjectName(u"transpose_pb")

        self.gridLayout.addWidget(self.transpose_pb, 3, 0, 1, 1)

        self.save_matrix_pb = QPushButton(self.centralwidget)
        self.save_matrix_pb.setObjectName(u"save_matrix_pb")

        self.gridLayout.addWidget(self.save_matrix_pb, 2, 0, 1, 3)

        self.rank_pb = QPushButton(self.centralwidget)
        self.rank_pb.setObjectName(u"rank_pb")

        self.gridLayout.addWidget(self.rank_pb, 3, 2, 1, 1)

        self.save_size_pb = QPushButton(self.centralwidget)
        self.save_size_pb.setObjectName(u"save_size_pb")

        self.gridLayout.addWidget(self.save_size_pb, 0, 2, 1, 1)

        self.result_label = QLabel(self.centralwidget)
        self.result_label.setObjectName(u"result_label")

        self.gridLayout.addWidget(self.result_label, 4, 0, 1, 1)

        self.result_le = QLineEdit(self.centralwidget)
        self.result_le.setObjectName(u"result_le")

        self.gridLayout.addWidget(self.result_le, 4, 1, 1, 1)

        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Matrix", None))
        self.size_label.setText(QCoreApplication.translate("main_window", u"\u0420\u0430\u0437\u043c\u0435\u0440:", None))
        self.det_pb.setText(QCoreApplication.translate("main_window", u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("main_window", u"1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("main_window", u"2", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("main_window", u"1", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("main_window", u"2", None));

        self.size_le.setText('2')

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("main_window", u"1", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("main_window", u"0", None));
        ___qtablewidgetitem6 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("main_window", u"0", None));
        ___qtablewidgetitem7 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("main_window", u"1", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.transpose_pb.setText(QCoreApplication.translate("main_window", u"\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.save_matrix_pb.setText(QCoreApplication.translate("main_window", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043c\u0430\u0442\u0440\u0438\u0446\u0443", None))
        self.rank_pb.setText(QCoreApplication.translate("main_window", u"\u0420\u0430\u043d\u0433", None))
        self.save_size_pb.setText(QCoreApplication.translate("main_window", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.result_label.setText(QCoreApplication.translate("main_window", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:", None))
    # retranslateUi

    def save_matrix(self):
        for i in range(self.__size):
            for j in range(self.__size):
                self.__matrix[i][j] = self.tableWidget.item(i, j)



    def save_new_size(self):
        if self.size_le.text() != "":
            new_size = int(self.size_le.text())
            old_size = self.__size
            self.__size = new_size
            self.tableWidget.setColumnCount(self.__size)
            self.tableWidget.setRowCount(self.__size)
            

            new_matrix = [[0 for j in range(new_size)] for i in range(new_size)]
            for i in range(new_size):
                for j in range(new_size):
                    if (i >= old_size) or (j >= old_size):
                        self.tableWidget.setItem(i, j, QTableWidgetItem())
                        self.tableWidget.item(i, j).setText('0')






