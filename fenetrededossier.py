# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:36:16 2022

@author: flola
"""
import os
import sys
from PyQt5.QtWidgets import (QToolTip, QFormLayout, QRadioButton, QLabel,
                             QApplication, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QTextEdit)
from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from fenetreaccueil import View_pagebienvenue
from historique import fenetre_hist
from fenetreimport import importer

# Classes de la page de bienvenue


class fenetre2(QWidget):

    def __init__(self, ctrl):
        super().__init__()
        self.myCtrl = ctrl
        self.accueil = View_pagebienvenue(self)
        self.accueil.show()

        self.importer = importer(self)

        self.init_ui()
        # self.show()

    def init_ui(self):

        # Définir les widgets

        self.lbl = QLabel('Nom')
        self.nom = QLineEdit(self)
        # Fixer la taille de la ligne de texte
        self.nom.setFixedWidth(200)
        # Aligner le titre du texte et le texte
        self.lbl.setBuddy(self.nom)
        self.lbl2 = QLabel('Prénom')
        self.prenom = QLineEdit(self)
        self.prenom.setFixedWidth(200)
        self.lbl3 = QLabel('Age')
        self.age = QLineEdit(self)
        self.age.setFixedWidth(200)
        self.lbl4 = QLabel('Sexe')
        self.homme = QRadioButton('M')
        self.femme = QRadioButton('F')

        self.lbl5 = QLabel('Symptômes')
        self.symp = QTextEdit(' ')
        self.symp.setFixedWidth(300)
        self.lbl6 = QLabel('Médicaments possibles')
        self.medoc = QTextEdit(' ')
        self.medoc.setReadOnly(True)
        self.medoc.setFixedWidth(300)

        # Afficher les propositions de medicaments quand le texte symptomes est modifiés
        self.symp.textChanged.connect(self.propositionmed)

        QToolTip.setFont(QFont('Arial', 13))
        self.setToolTip('Nous sommes là pour vous <b>aider !</b>')
        self.fermer_btn = QPushButton('Fermer')
        self.fermer_btn.setFixedWidth(200)
        self.fermer_btn.setToolTip("Retourner à la page d'acceuil")
        self.enreg_btn = QPushButton('Enregistrer')
        self.enreg_btn.setFixedWidth(200)
        self.enreg_btn.setToolTip('Enregistrer les données dans un fichier')
        self.hist_btn = QPushButton('Historique')
        self.hist_btn.setFixedWidth(300)
        self.hist_btn.setToolTip("Ouvrir l'historique des ordonnances")
        self.importer_btn = QPushButton('Importer')
        self.importer_btn.setFixedWidth(300)
        self.importer_btn.setToolTip(
            "Importer les données d'un fichier existant")

        # Organiser la fenêtre
        # Patie en haut à gauche
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        # aligner verticalement les textes
        p_layout = QVBoxLayout()
        # aligner horizontalement les radios button
        radio_layout = QHBoxLayout()

        v_layout.addWidget(self.lbl)
        v_layout.addWidget(self.lbl2)
        v_layout.addWidget(self.lbl3)
        v_layout.addWidget(self.lbl4)

        radio_layout.addWidget(self.homme)
        radio_layout.addWidget(self.femme)

        p_layout.addWidget(self.nom)
        p_layout.addWidget(self.prenom)
        p_layout.addWidget(self.age)
        p_layout.addLayout(radio_layout)

        h_layout.addLayout(v_layout)
        h_layout.addLayout(p_layout)

        # Partie en bas
        basgauche_layout = QVBoxLayout()
        basdroite_layout = QVBoxLayout()
        # Aligner horizontalement les 2
        bas_layout = QHBoxLayout()

        basgauche_layout.addWidget(self.lbl5)
        basgauche_layout.addWidget(self.symp)
        basgauche_layout.addWidget(self.enreg_btn)

        basdroite_layout.addWidget(self.lbl6)
        basdroite_layout.addWidget(self.medoc)
        basdroite_layout.addWidget(self.fermer_btn)

        bas_layout.addLayout(basgauche_layout)
        bas_layout.addLayout(basdroite_layout)

        # Partie en haut à droite
        centrer_layout = QVBoxLayout()

        centrer_layout.addWidget(self.hist_btn)
        centrer_layout.addWidget(self.importer_btn)

        # Partie en haut rassemblée
        haut_layout = QHBoxLayout()

        haut_layout.addLayout(h_layout)
        haut_layout.addLayout(centrer_layout)

        # Patie à gauche
        gauche_layout = QVBoxLayout()
        gauche_layout.addLayout(basgauche_layout)
        gauche_layout.addLayout(h_layout)

        # Partie à droite
        droite_layout = QVBoxLayout()
        droite_layout.addLayout(basdroite_layout)
        droite_layout.addLayout(centrer_layout)

        # Rassembler horizontalement tout en global
        globalh_layout = QVBoxLayout()
        globalh_layout.addLayout(haut_layout)
        globalh_layout.addLayout(bas_layout)

        # Le regroupement final
        global_layout = QHBoxLayout()
        global_layout.addLayout(gauche_layout)
        global_layout.addLayout(droite_layout)
        global_layout.addLayout(globalh_layout)

        self.setLayout(global_layout)
        self.setWindowTitle('Fenêtre de dossier')

        self.fermer_btn.clicked.connect(self.fermer_click)
        self.enreg_btn.clicked.connect(self.enreg_click)
        self.hist_btn.clicked.connect(self.hist_click)
        self.importer_btn.clicked.connect(self.imp_click)

    def propositionmed(self):

        # dictionnaire des médiacaments en fonction des symptômes
        D = {}
        D['douleur'] = 'Doliprane', 'Dafalgan', 'Efferalgan'
        D['fièvre'] = 'Doliprane', 'Dafalgan', 'Efferalgan'
        D['cardiovasculaire'] = 'Kardegic'
        D['intestin'] = 'Spasfon', 'MeteoSpasmyl'
        D['vessie'] = 'Spasfon'
        D['uterus'] = 'Spasfon'
        D["brûlures d'estomac"] = "Gaviscon"
        D["indigestion"] = "Gaviscon"
        D["irritations cutanées"] = "Dexeryl"
        D["ballonnement abdominal"] = "MeteoSpasmyl"
        D["plaies"] = "Biseptine"
        D["infections de la bouche"] = "Eludril"

        l = ''
        symptome = self.symp.toPlainText()
        print(symptome)
        fichier = symptome.split(',')
        for cle in D.keys():
            for i in range(len(fichier)):
                if cle == fichier[i]:
                    med = D[cle]
                    print(med)
                    if type(med) == tuple:
                        for k in range(len(med)):
                            l += med[k]+'\n'
                    else:
                        l += med

        self.medoc.setText(l)

        # print('cle: ',cle)
        # if cle==symptome:
        #     med=D[cle]
        #     print(med)
        #     if type(med)==tuple:
        #         for i in range(len(med)):
        #             l+=med[i]+'\n'
        #     else:
        #        l+=med

    def imp_click(self):
        # Importer les données pour récupérer le nom et le prénom
        f = open('importer.txt', 'r')
        datafile = f.read()
        fichier = datafile.split('\n')
        print('fichier: ', fichier)
        self.p = fichier[1]
        self.n = fichier[2]
        f.close()
        # effacer les valeurs importées
        f = open('importer.txt', 'a')
        f.truncate(0)
        f.close()

        # Récupérer toutes les informations dans le fichier correspondant
        titre = self.n+' '+self.p+'.txt'
        print(titre)
        f = open(titre, 'r')
        datafile = f.read()
        fichier = datafile.split('\n')
        self.a = fichier[3]
        self.sexe = fichier[4]
        f.close()

        self.prenom.setText(self.p)
        self.nom.setText(self.n)
        self.age.setText(self.a)

        if self.sexe == 'femme':
            self.femme.setChecked(True)
        else:
            self.homme.setChecked(True)

    def hist_click(self):
        self.p = self.prenom.text()
        self.n = self.nom.text()
        self.a = self.age.text()
        self.histor = fenetre_hist(self, self.p, self.n, self.a)
        self.hide()
        self.histor.show()

    def enreg_click(self):
        p = self.prenom.text()
        n = self.nom.text()
        a = self.age.text()
        F = self.femme.isChecked()
        s = self.symp.toPlainText()
        self.aux = self.myCtrl.enregistrer(p, n, a, F, s)

    def fermer_click(self):
        self.hide()
        self.accueil.show()

        # t = self.texte
        # self.aux = self.myCtrl.fermer(t)


class Controller:

    def __init__(self, model):
        self.myModel = model

    def enregistrer(self, p, n, a, F, s):
        self.myModel.enr_donnees(p, n, a, F, s)


class Model:
    def __init__(self):
        self.i = 0

    def enr_donnees(self, p, n, a, F, s):
        titre = n+' '+p+'.txt'
        f = open(titre, 'a')
        # f.truncate(0)
        if F:
            genre = 'femme'
        else:
            genre = 'homme'

        # Si le fichier avec ce titre existe
        if os.path.isfile(titre):
           # if fichierexistant==True:
            f.write('\n'+'*' + '\n'+s)

        else:
            f.write('1' + '\n'+p + '\n'+n + '\n'+a + '\n'+genre)
            f.write('\n'+'*' + '\n'+s)

        f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    ctrl = Controller(model)
    view = fenetre2(ctrl)  # View_pagebienvenue()
    sys.exit(app.exec_())
