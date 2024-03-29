# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1184, 851)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(660, 30, 501, 801))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.titre_livre = QtWidgets.QLabel(self.groupBox)
        self.titre_livre.setGeometry(QtCore.QRect(30, 10, 451, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.titre_livre.setFont(font)
        self.titre_livre.setAlignment(QtCore.Qt.AlignCenter)
        self.titre_livre.setObjectName("titre_livre")
        self.chapitre_titre = QtWidgets.QLabel(self.groupBox)
        self.chapitre_titre.setGeometry(QtCore.QRect(120, 80, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chapitre_titre.setFont(font)
        self.chapitre_titre.setAlignment(QtCore.Qt.AlignCenter)
        self.chapitre_titre.setObjectName("chapitre_titre")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 750, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.aller = QtWidgets.QPushButton(self.groupBox)
        self.aller.setGeometry(QtCore.QRect(340, 750, 111, 28))
        self.aller.setObjectName("aller")
        self.zone_texte_chapitre = QtWidgets.QTextBrowser(self.groupBox)
        self.zone_texte_chapitre.setGeometry(QtCore.QRect(40, 120, 431, 611))
        self.zone_texte_chapitre.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.zone_texte_chapitre.setObjectName("zone_texte_chapitre")
        self.suite = QtWidgets.QComboBox(self.groupBox)
        self.suite.setGeometry(QtCore.QRect(160, 750, 151, 22))
        self.suite.setObjectName("suite")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 601, 80))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.choix_livre = QtWidgets.QComboBox(self.groupBox_2)
        self.choix_livre.setGeometry(QtCore.QRect(140, 20, 361, 22))
        self.choix_livre.setObjectName("choix_livre")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 110, 601, 161))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(50, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(310, 10, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(30, 60, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.nom = QtWidgets.QLineEdit(self.groupBox_3)
        self.nom.setGeometry(QtCore.QRect(92, 60, 131, 22))
        self.nom.setObjectName("nom")
        self.nouvelle_partie = QtWidgets.QPushButton(self.groupBox_3)
        self.nouvelle_partie.setGeometry(QtCore.QRect(20, 120, 201, 28))
        self.nouvelle_partie.setObjectName("nouvelle_partie")
        self.charger_partie = QtWidgets.QComboBox(self.groupBox_3)
        self.charger_partie.setGeometry(QtCore.QRect(290, 40, 201, 22))
        self.charger_partie.setObjectName("charger_partie")
        self.sauvegarder = QtWidgets.QPushButton(self.groupBox_3)
        self.sauvegarder.setGeometry(QtCore.QRect(290, 80, 201, 28))
        self.sauvegarder.setObjectName("sauvegarder")
        self.supprimer = QtWidgets.QPushButton(self.groupBox_3)
        self.supprimer.setGeometry(QtCore.QRect(290, 120, 201, 28))
        self.supprimer.setObjectName("supprimer")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 280, 601, 541))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(330, 310, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.bourse = QtWidgets.QSpinBox(self.groupBox_4)
        self.bourse.setGeometry(QtCore.QRect(460, 310, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bourse.setFont(font)
        self.bourse.setObjectName("bourse")
        self.zone_texte_object_speciaux = QtWidgets.QTextEdit(self.groupBox_4)
        self.zone_texte_object_speciaux.setGeometry(QtCore.QRect(30, 396, 251, 131))
        self.zone_texte_object_speciaux.setObjectName("zone_texte_object_speciaux")
        self.repas = QtWidgets.QTextEdit(self.groupBox_4)
        self.repas.setGeometry(QtCore.QRect(320, 436, 261, 91))
        self.repas.setObjectName("repas")
        self.zone_texte_object = QtWidgets.QTextEdit(self.groupBox_4)
        self.zone_texte_object.setGeometry(QtCore.QRect(30, 220, 251, 121))
        self.zone_texte_object.setObjectName("zone_texte_object")
        self.descipline1 = QtWidgets.QComboBox(self.groupBox_4)
        self.descipline1.setGeometry(QtCore.QRect(340, 110, 241, 22))
        self.descipline1.setObjectName("descipline1")
        self.descipline4 = QtWidgets.QComboBox(self.groupBox_4)
        self.descipline4.setGeometry(QtCore.QRect(340, 220, 241, 22))
        self.descipline4.setObjectName("descipline4")
        self.descipline5 = QtWidgets.QComboBox(self.groupBox_4)
        self.descipline5.setGeometry(QtCore.QRect(340, 260, 241, 22))
        self.descipline5.setObjectName("descipline5")
        self.descipline3 = QtWidgets.QComboBox(self.groupBox_4)
        self.descipline3.setGeometry(QtCore.QRect(340, 180, 241, 22))
        self.descipline3.setObjectName("descipline3")
        self.descipline2 = QtWidgets.QComboBox(self.groupBox_4)
        self.descipline2.setGeometry(QtCore.QRect(340, 140, 241, 22))
        self.descipline2.setObjectName("descipline2")
        self.arme2 = QtWidgets.QComboBox(self.groupBox_4)
        self.arme2.setGeometry(QtCore.QRect(70, 140, 191, 22))
        self.arme2.setObjectName("arme2")
        self.arme1 = QtWidgets.QComboBox(self.groupBox_4)
        self.arme1.setGeometry(QtCore.QRect(70, 110, 191, 22))
        self.arme1.setObjectName("arme1")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(30, 80, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(370, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(30, 110, 55, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(30, 140, 21, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(280, 80, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(380, 400, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(50, 360, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(50, 180, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(300, 110, 21, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(300, 140, 21, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(300, 180, 21, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(300, 220, 21, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(300, 260, 21, 20))
        self.label_22.setObjectName("label_22")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titre_livre.setAccessibleName(_translate("MainWindow", "titre_livre"))
        self.titre_livre.setText(_translate("MainWindow", "Titre du livre"))
        self.chapitre_titre.setAccessibleName(_translate("MainWindow", "chapitre_titre"))
        self.chapitre_titre.setText(_translate("MainWindow", "Chapitre 0"))
        self.label_3.setText(_translate("MainWindow", "Lire la suite :"))
        self.aller.setAccessibleName(_translate("MainWindow", "aller"))
        self.aller.setText(_translate("MainWindow", "Aller"))
        self.zone_texte_chapitre.setAccessibleName(_translate("MainWindow", "zone_texte_chapitre"))
        self.suite.setAccessibleName(_translate("MainWindow", "suite"))
        self.label_4.setText(_translate("MainWindow", "Choix du livre "))
        self.choix_livre.setAccessibleName(_translate("MainWindow", "choix_livre"))
        self.label_5.setText(_translate("MainWindow", "Nouvelle partie"))
        self.label_6.setText(_translate("MainWindow", "Charger une partie"))
        self.label_7.setText(_translate("MainWindow", "Nom :"))
        self.nom.setAccessibleName(_translate("MainWindow", "nom"))
        self.nouvelle_partie.setText(_translate("MainWindow", "Nouvelle partie"))
        self.charger_partie.setAccessibleName(_translate("MainWindow", "charger_partie"))
        self.sauvegarder.setAccessibleName(_translate("MainWindow", "sauvegarder"))
        self.sauvegarder.setText(_translate("MainWindow", "Sauvegarder"))
        self.supprimer.setAccessibleName(_translate("MainWindow", "supprimer"))
        self.supprimer.setText(_translate("MainWindow", "Supprimer"))
        self.label_8.setText(_translate("MainWindow", "Fiche du personnage :"))
        self.label_9.setText(_translate("MainWindow", "Bourse"))
        self.bourse.setAccessibleName(_translate("MainWindow", "bourse"))
        self.zone_texte_object_speciaux.setAccessibleName(_translate("MainWindow", "zone_texte_object_speciaux"))
        self.repas.setAccessibleName(_translate("MainWindow", "repas"))
        self.zone_texte_object.setAccessibleName(_translate("MainWindow", "zone_texte_object"))
        self.descipline1.setAccessibleName(_translate("MainWindow", "descipline1"))
        self.descipline4.setAccessibleName(_translate("MainWindow", "descipline4"))
        self.descipline5.setAccessibleName(_translate("MainWindow", "descipline5"))
        self.descipline3.setAccessibleName(_translate("MainWindow", "descipline3"))
        self.descipline2.setAccessibleName(_translate("MainWindow", "descipline2"))
        self.arme2.setAccessibleName(_translate("MainWindow", "arme2"))
        self.arme1.setAccessibleName(_translate("MainWindow", "arme_1"))
        self.label_10.setText(_translate("MainWindow", "Armes"))
        self.label_11.setText(_translate("MainWindow", "Nom"))
        self.label_12.setText(_translate("MainWindow", "1."))
        self.label_13.setText(_translate("MainWindow", "2."))
        self.label_14.setText(_translate("MainWindow", "Disciplines Kai"))
        self.label_15.setText(_translate("MainWindow", "Repas"))
        self.label_16.setText(_translate("MainWindow", "Objects spéciaux"))
        self.label_17.setText(_translate("MainWindow", "Objects "))
        self.label_18.setText(_translate("MainWindow", "1."))
        self.label_19.setText(_translate("MainWindow", "2."))
        self.label_20.setText(_translate("MainWindow", "3."))
        self.label_21.setText(_translate("MainWindow", "4."))
        self.label_22.setText(_translate("MainWindow", "5."))