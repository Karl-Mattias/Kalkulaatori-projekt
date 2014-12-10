from PyQt4 import QtCore, QtGui
import sys
import funktsioonid
from math import sqrt


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

class Ui_MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(631, 562)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.Ekraan = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Ekraan.setFont(font)
        self.Ekraan.setFrameShape(QtGui.QFrame.Box)
        self.Ekraan.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Ekraan.setObjectName(_fromUtf8("Ekraan"))
        self.verticalLayout_3.addWidget(self.Ekraan)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btn_1 = QtGui.QPushButton(self.centralwidget)
        self.btn_1.setObjectName(_fromUtf8("btn_1"))
        self.horizontalLayout_3.addWidget(self.btn_1)
        self.btn_2 = QtGui.QPushButton(self.centralwidget)
        self.btn_2.setObjectName(_fromUtf8("btn_2"))
        self.horizontalLayout_3.addWidget(self.btn_2)
        self.btn_3 = QtGui.QPushButton(self.centralwidget)
        self.btn_3.setObjectName(_fromUtf8("btn_3"))
        self.horizontalLayout_3.addWidget(self.btn_3)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.btn_add = QtGui.QPushButton(self.centralwidget)
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.horizontalLayout_3.addWidget(self.btn_add)
        self.btn_sub = QtGui.QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(_fromUtf8("btn_sub"))
        self.horizontalLayout_3.addWidget(self.btn_sub)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.btn_4 = QtGui.QPushButton(self.centralwidget)
        self.btn_4.setObjectName(_fromUtf8("btn_4"))
        self.horizontalLayout_4.addWidget(self.btn_4)
        self.btn_5 = QtGui.QPushButton(self.centralwidget)
        self.btn_5.setObjectName(_fromUtf8("btn_5"))
        self.horizontalLayout_4.addWidget(self.btn_5)
        self.btn_6 = QtGui.QPushButton(self.centralwidget)
        self.btn_6.setObjectName(_fromUtf8("btn_6"))
        self.horizontalLayout_4.addWidget(self.btn_6)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.horizontalLayout_4.addLayout(self.horizontalLayout_7)
        self.btn_mult = QtGui.QPushButton(self.centralwidget)
        self.btn_mult.setObjectName(_fromUtf8("btn_mult"))
        self.horizontalLayout_4.addWidget(self.btn_mult)
        self.btn_divide = QtGui.QPushButton(self.centralwidget)
        self.btn_divide.setObjectName(_fromUtf8("btn_divide"))
        self.horizontalLayout_4.addWidget(self.btn_divide)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.btn_7 = QtGui.QPushButton(self.centralwidget)
        self.btn_7.setObjectName(_fromUtf8("btn_7"))
        self.horizontalLayout_5.addWidget(self.btn_7)
        self.btn_8 = QtGui.QPushButton(self.centralwidget)
        self.btn_8.setObjectName(_fromUtf8("btn_8"))
        self.horizontalLayout_5.addWidget(self.btn_8)
        self.btn_9 = QtGui.QPushButton(self.centralwidget)
        self.btn_9.setObjectName(_fromUtf8("btn_9"))
        self.horizontalLayout_5.addWidget(self.btn_9)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout_5.addLayout(self.horizontalLayout_8)
        self.btn_exp = QtGui.QPushButton(self.centralwidget)
        self.btn_exp.setObjectName(_fromUtf8("btn_exp"))
        self.horizontalLayout_5.addWidget(self.btn_exp)
        self.btn_sqrt = QtGui.QPushButton(self.centralwidget)
        self.btn_sqrt.setObjectName(_fromUtf8("btn_sqrt"))
        self.horizontalLayout_5.addWidget(self.btn_sqrt)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.btn_clear = QtGui.QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(_fromUtf8("btn_clear"))
        self.horizontalLayout_6.addWidget(self.btn_clear)
        self.btn_0 = QtGui.QPushButton(self.centralwidget)
        self.btn_0.setObjectName(_fromUtf8("btn_0"))
        self.horizontalLayout_6.addWidget(self.btn_0)
        self.btn_calc = QtGui.QPushButton(self.centralwidget)
        self.btn_calc.setObjectName(_fromUtf8("btn_calc"))
        self.horizontalLayout_6.addWidget(self.btn_calc)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.horizontalLayout_6.addLayout(self.horizontalLayout_9)
        self.btn_braco = QtGui.QPushButton(self.centralwidget)
        self.btn_braco.setObjectName(_fromUtf8("btn_braco"))
        self.horizontalLayout_6.addWidget(self.btn_braco)
        self.btn_bracc = QtGui.QPushButton(self.centralwidget)
        self.btn_bracc.setObjectName(_fromUtf8("btn_bracc"))
        self.horizontalLayout_6.addWidget(self.btn_bracc)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem13)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.btn_back = QtGui.QPushButton(self.centralwidget)
        self.btn_back.setObjectName(_fromUtf8("btn_back"))
        self.horizontalLayout_2.addWidget(self.btn_back)
        self.btn_x = QtGui.QPushButton(self.centralwidget)
        self.btn_x.setObjectName(_fromUtf8("btn_x"))
        self.horizontalLayout_2.addWidget(self.btn_x)
        self.btn_y = QtGui.QPushButton(self.centralwidget)
        self.btn_y.setObjectName(_fromUtf8("btn_y"))
        self.horizontalLayout_2.addWidget(self.btn_y)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.btn_smaller = QtGui.QPushButton(self.centralwidget)
        self.btn_smaller.setObjectName(_fromUtf8("btn_smaller"))
        self.horizontalLayout_2.addWidget(self.btn_smaller)
        self.btn_bigger = QtGui.QPushButton(self.centralwidget)
        self.btn_bigger.setObjectName(_fromUtf8("btn_bigger"))
        self.horizontalLayout_2.addWidget(self.btn_bigger)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem16 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem16)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setMinimumSize(QtCore.QSize(0, 13))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_3.addWidget(self.line_2)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.Kahend_Ekraan = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Kahend_Ekraan.setFont(font)
        self.Kahend_Ekraan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Kahend_Ekraan.setFrameShape(QtGui.QFrame.Box)
        self.Kahend_Ekraan.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Kahend_Ekraan.setObjectName(_fromUtf8("Kahend_Ekraan"))
        self.verticalLayout_3.addWidget(self.Kahend_Ekraan)
        spacerItem17 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem17)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.btn_K1 = QtGui.QPushButton(self.centralwidget)
        self.btn_K1.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_K1.setObjectName(_fromUtf8("btn_K1"))
        self.horizontalLayout_10.addWidget(self.btn_K1)
        self.btn_K2 = QtGui.QPushButton(self.centralwidget)
        self.btn_K2.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_K2.setObjectName(_fromUtf8("btn_K2"))
        self.horizontalLayout_10.addWidget(self.btn_K2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        spacerItem18 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem18)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Kalkulaator", None))
        self.label_2.setText(_translate("MainWindow", "Kümnendsüsteem", None))
        self.Ekraan.setText(_translate("MainWindow", "0", None))

        self.btn_1.setText(_translate("MainWindow", "1", None))
        self.btn_1.clicked.connect(self.add_1)
        
        self.btn_2.setText(_translate("MainWindow", "2", None))
        self.btn_2.clicked.connect(self.add_2)
        
        self.btn_3.setText(_translate("MainWindow", "3", None))
        self.btn_3.clicked.connect(self.add_3)
        
        self.btn_add.setText(_translate("MainWindow", "+", None))
        self.btn_add.clicked.connect(self.add_plus)
        
        self.btn_sub.setText(_translate("MainWindow", "-", None))
        self.btn_sub.clicked.connect(self.add_minus)
        
        self.btn_4.setText(_translate("MainWindow", "4", None))
        self.btn_4.clicked.connect(self.add_4)
        
        self.btn_5.setText(_translate("MainWindow", "5", None))
        self.btn_5.clicked.connect(self.add_5)
        
        self.btn_6.setText(_translate("MainWindow", "6", None))
        self.btn_6.clicked.connect(self.add_6)
        
        self.btn_mult.setText(_translate("MainWindow", "*", None))
        self.btn_mult.clicked.connect(self.add_mult)
        
        self.btn_divide.setText(_translate("MainWindow", "/", None))
        self.btn_divide.clicked.connect(self.add_divide)
        
        self.btn_7.setText(_translate("MainWindow", "7", None))
        self.btn_7.clicked.connect(self.add_7)
        
        self.btn_8.setText(_translate("MainWindow", "8", None))
        self.btn_8.clicked.connect(self.add_8)
        
        self.btn_9.setText(_translate("MainWindow", "9", None))
        self.btn_9.clicked.connect(self.add_9)
        
        self.btn_exp.setText(_translate("MainWindow", "a^x", None))
        self.btn_exp.clicked.connect(self.add_exp)
        
        self.btn_sqrt.setText(_translate("MainWindow", "√a", None))
        self.btn_sqrt.clicked.connect(self.add_sqrt)
        
        self.btn_clear.setText(_translate("MainWindow", "Tühista", None))
        self.btn_clear.clicked.connect(self.clear)       
        
        self.btn_0.setText(_translate("MainWindow", "0", None))
        self.btn_0.clicked.connect(self.add_0)
        
        self.btn_calc.setText(_translate("MainWindow", "Arvuta", None))
        self.btn_calc.clicked.connect(self.calc)
        
        self.btn_braco.setText(_translate("MainWindow", "(", None))
        self.btn_braco.clicked.connect(self.add_braco)
        
        self.btn_bracc.setText(_translate("MainWindow", ")", None))
        self.btn_bracc.clicked.connect(self.add_bracc)
        
        self.btn_x.setText(_translate("MainWindow", "x", None))
        self.btn_x.clicked.connect(self.add_x)
        
        self.btn_y.setText(_translate("MainWindow", "y", None))
        self.btn_y.clicked.connect(self.add_y)
        
        self.btn_smaller.setText(_translate("MainWindow", "<", None))
        self.btn_smaller.clicked.connect(self.add_smaller)
        
        self.btn_bigger.setText(_translate("MainWindow", ">", None))
        self.btn_bigger.clicked.connect(self.add_bigger)
        
        self.label.setText(_translate("MainWindow", "Kahendsüsteem", None))
        self.Kahend_Ekraan.setText(_translate("MainWindow", "0", None))
        
        self.btn_K1.setText(_translate("MainWindow", "1", None))
        self.btn_K1.clicked.connect(self.add_K1)
        
        self.btn_K2.setText(_translate("MainWindow", "0", None))
        self.btn_K2.clicked.connect(self.add_K0)

        self.btn_back.setText(_translate("MainWindow", "< ----", None))
        self.btn_back.clicked.connect(self.back)



        self.sisend = ''
        self.Ksisend=''


    def add_1(self):
        self.sisend +='1'
        self.uuenda()

    def add_2(self):
        self.sisend +='2'
        self.uuenda()

    def add_3(self):
        self.sisend +='3'
        self.uuenda()

    def add_4(self):
        self.sisend +='4'
        self.uuenda()

    def add_5(self):
        self.sisend +='5'
        self.uuenda()

    def add_6(self):
        self.sisend +='6'
        self.uuenda()

    def add_7(self):
        self.sisend +='7'
        self.uuenda()

    def add_8(self):
        self.sisend +='8'
        self.uuenda()

    def add_9(self):
        self.sisend +='9'
        self.uuenda()

    def add_0(self):
        self.sisend +='0'
        self.uuenda()

    def add_plus(self):
        if not self.duubel():
            self.sisend +='+'
            self.uuenda()

    def add_minus(self):
        if not self.duubel():
            self.sisend +='-'
            self.uuenda()

    def add_mult(self):
        if not self.duubel():
            self.sisend +='*'
            self.uuenda()

    def add_divide(self):
        if not self.duubel():
            self.sisend +='/'
            self.uuenda()

    def add_exp(self):
        if not self.duubel():
            self.sisend +='^'
            self.uuenda()

    def add_sqrt(self):
        self.sisend +='√('
        self.uuenda()

    def clear(self):
        self.sisend = '0'
        self.Ksisend='0'
        self.uuenda()
                
    def add_braco(self):
        self.sisend +='('
        self.uuenda()

    def add_bracc(self):
        self.sisend +=')'
        self.uuenda()

    def add_x(self):
        if len(self.sisend)<=1 or not self.sisend[-1] in ['x','y']:
            self.sisend +='x'
            self.uuenda()
        
    def add_y(self):
        if not self.sisend[-1] in ['x','y']:
            self.sisend +='y'
            self.uuenda()

    def add_smaller(self):
        if not self.duubel():
            self.sisend +='<'
            self.uuenda()

    def add_bigger(self):
        if not self.duubel():
            self.sisend +='>'
            self.uuenda()

    def add_K0(self):
        self.Ksisend +='0'
        self.Kuuenda()

    def add_K1(self):
        self.Ksisend +='1'
        self.Kuuenda()
    
    def duubel(self):
        return self.sisend[-1] in ['+','-','*','/','√','^']

    def calc(self):
        self.sisend=self.sisend.replace('^','**').replace('/','//').replace('√','sqrt')
        if 'x' in self.sisend and 'y' in self.sisend:
            funktsioonid.plot(self.sisend)
        self.sisend = str(int(eval(self.sisend)))
        self.uuenda()

    def uuenda(self):
        if len(self.sisend) > 1:
            if self.sisend[0] == '0':
                self.sisend = self.sisend[1:]

        try:
            self.Ksisend = funktsioonid.kahendsüsteemi(self.sisend)
            if len(self.Ksisend) > 4:
                ajutine = list(self.Ksisend)
                for e in range(len(self.Ksisend)+1):
                    if e%4==0:
                        ajutine[-e] = ' '+ajutine[-e]
                self.Ksisend = ''.join(ajutine)
                    
            self.Kahend_Ekraan.setText(_translate("MainWindow", self.Ksisend, None))
        except:
            None
        self.Ekraan.setText(_translate("MainWindow", self.sisend, None))

        


    def Kuuenda(self):
        if len(self.Ksisend) > 1:
            if self.Ksisend[0] == '0':
                self.Ksisend = self.Ksisend[1:]

        if len(self.Ksisend) > 4:
                ajutine = list(self.Ksisend.replace(' ',''))
                for e in range(len(self.Ksisend.replace(' ',''))+1):
                    if e%4==0:
                        ajutine[-e] = ' '+ajutine[-e]
                self.Ksisend = ''.join(ajutine)

        
        self.sisend = str(funktsioonid.kümnendsüsteemi(self.Ksisend.replace(' ','')))
        print(self.sisend)

        self.Kahend_Ekraan.setText(_translate("MainWindow", self.Ksisend, None))

        self.Ekraan.setText(_translate("MainWindow", self.sisend, None))


    def back(self):
        if len(self.Ksisend) <= 1:
            self.Ksisend = '0'
        elif self.Ksisend[-1] == ' ':
            self.Ksisend = self.Ksisend[0:-3]
        else:
            self.Ksisend = self.Ksisend[0:-1]
        self.Kuuenda()

    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())


