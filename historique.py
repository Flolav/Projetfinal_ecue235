# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:44:03 2022

@author: flola
"""

import sys
from PyQt5.QtWidgets import (QFormLayout, QRadioButton, QGridLayout, QLabel,
                             QApplication, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QTextEdit)
from PyQt5 import QtGui


class fenetre_hist(QWidget):

    def __init__(self, fprec,p,n,a):
        super().__init__()
        self.f2=fprec
        self.p=p
        self.n=n
        self.a=a
        self.init_ui()
        

    def init_ui(self):

        # Définir les widgets
        
        self.lbl = QLabel('Nom')
        self.nom = QLineEdit(self)
        self.nom.setReadOnly(True)
        # Fixer la taille de la ligne de texte
        #self.nom.setFixedWidth(200)
        self.nom.setText(self.n)
        # Aligner le titre du texte et le texte
        self.lbl.setBuddy(self.nom)
        
        self.lbl2 = QLabel('Prénom')
        self.prenom = QLineEdit(self)
        self.prenom.setReadOnly(True)
        #self.prenom.setFixedWidth(200)
        self.prenom.setText(self.p)
        
        self.lbl3 = QLabel('Age')
        self.age = QLineEdit(self)
        self.age.setReadOnly(True)
        #self.age.setFixedWidth(200)
        self.age.setText(self.a)
        
        self.lbl4 = QLabel('Symptômes et Ordonnances')
        self.symp = QTextEdit(' ')
        self.symp.setReadOnly(True)

        self.fermer_btn = QPushButton('Fermer')
        

        # Organiser la fenêtre
        # Organiser la fenêtre
        # Patie en haut à gauche
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        # aligner verticalement les textes
        p_layout = QVBoxLayout()

        v_layout.addWidget(self.lbl)
        v_layout.addWidget(self.lbl2)
        v_layout.addWidget(self.lbl3)


        p_layout.addWidget(self.nom)
        p_layout.addWidget(self.prenom)
        p_layout.addWidget(self.age)

        
        h_layout.addLayout(v_layout)
        h_layout.addLayout(p_layout)
        
        #alignement texte et fermer
        t_layout = QVBoxLayout()
        j_layout = QHBoxLayout()

        j_layout.addWidget(self.lbl4)
        j_layout.addWidget(self.symp)
        
        t_layout.addLayout(j_layout)
        t_layout.addWidget(self.fermer_btn)
        
        #On regroupe tout
        global_layout = QVBoxLayout()
        global_layout.addLayout(h_layout)
        global_layout.addLayout(t_layout)

        self.setLayout(global_layout)
        self.setWindowTitle('Historique')

        self.fermer_btn.clicked.connect(self.fermer_click)
        
        #Trouver le bon fichier patient
        
        titre=self.n+' '+self.p+'.txt'
        print(titre)
        f = open(titre, 'r')
        l=''
        #Trouver l'ordonnance dans le fichier
        datafile = f.read()
        fichier=datafile.split('\n')
        print(fichier)
        for i in range(len(fichier)):
            if '*'==fichier[i]:
                g1=fichier[i+1:]
                print(g1)
                for k in range(len(g1)):
                    l+=g1[k]+'\n'
                break
        #Remplir le texte de la liste des ordonnances            
        self.symp.setText(l)
        
        f.close()

    def fermer_click(self):
        self.hide()
        self.f2.show()

 