# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 23:26:29 2022

@author: flola
"""

import sys
from PyQt5.QtWidgets import (QFormLayout, QRadioButton, QGridLayout, QLabel,
                             QApplication, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QTextEdit)
from PyQt5 import QtGui
#from fenetrededossier_secours import dossierimport

class importer(QWidget):

    def __init__(self, fprec):
        super().__init__()
        self.f2=fprec
        #self.dossier = dossierimport(self)
        
        self.init_ui()
        #self.show()

    def init_ui(self):

        # Définir les widgets
        
        self.lbl = QLabel('Nom')
        self.nom = QLineEdit(self)
        # Fixer la taille de la ligne de texte
        #self.nom.setFixedWidth(200)
        # Aligner le titre du texte et le texte
        self.lbl.setBuddy(self.nom)
        
        self.lbl2 = QLabel('Prénom')
        self.prenom = QLineEdit(self) 
        #self.prenom.setFixedWidth(200)
        
        self.importe_btn = QPushButton('Importer')
        

        # Organiser la fenêtre
        # Organiser la fenêtre
        # Patie en haut à gauche
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        # aligner verticalement les textes
        p_layout = QVBoxLayout()

        v_layout.addWidget(self.lbl)
        v_layout.addWidget(self.lbl2)

        p_layout.addWidget(self.nom)
        p_layout.addWidget(self.prenom)
     
        h_layout.addLayout(v_layout)
        h_layout.addLayout(p_layout)
        
        #alignement nom,prénom et bouton
        t_layout = QVBoxLayout()
        
        t_layout.addLayout(h_layout)
        t_layout.addWidget(self.importe_btn)
        

        self.setLayout(t_layout)
        self.setWindowTitle('Importer')

        self.importe_btn.clicked.connect(self.imp_click)
        
    def imp_click(self):
        self.p = self.prenom.text()
        self.n = self.nom.text()
        f = open('importer.txt', 'a')
        f.truncate(0)
        f.write('*'+'\n'+self.p+'\n'+self.n)
        f.close()
        
        self.hide()
        #self.f2.show()
        #self.dossier.show()