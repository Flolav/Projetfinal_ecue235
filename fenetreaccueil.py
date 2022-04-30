# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:08:27 2022

@author: flola
"""

import sys 
from PyQt5.QtWidgets import (QGridLayout,QLabel,QApplication,QPushButton,QVBoxLayout,QWidget,QHBoxLayout,QLineEdit,QTextEdit)
from PyQt5 import QtGui
from PyQt5 import QtCore
from fenetreimport import importer
import time

#Classes de la page de bienvenue
class View_pagebienvenue(QWidget):

    def __init__(self,fprec):
        super().__init__()
        self.f2=fprec
        self.importer = importer(self)
        if __name__ == '__main__':
            self.hide()
            self.f2.show()
            
        
        
        self.photo=QLabel(self)
        self.photo.setPixmap(QtGui.QPixmap('photomed.jpg'))
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.nom=QLabel(self)
        self.nom.setText("O'Médecin")
        self.nom.setAlignment(QtCore.Qt.AlignCenter)
        self.bonjour=QLabel(self)
        self.bonjour.setText('Bienvenue, nous sommes là pour vous aider!')
        self.bonjour.setAlignment(QtCore.Qt.AlignCenter)


        self.create_btn=QPushButton('Créer un dossier')
        self.importer_btn=QPushButton('Importer un dossier')

        self.init_ui()
        self.show()

    def init_ui(self):
        self.photo.move(100,20)
        
        v_layout=QVBoxLayout()
        h_layout=QHBoxLayout()
        
       
        h_layout.addWidget(self.create_btn)
        h_layout.addWidget(self.importer_btn)

        v_layout.addWidget(self.photo)
        v_layout.addWidget(self.nom)
        v_layout.addWidget(self.bonjour)
        v_layout.addLayout(h_layout)

        self.create_btn.clicked.connect(self.create_click)
        self.importer_btn.clicked.connect(self.importer_click)

        self.setLayout(v_layout)
        self.setWindowTitle("Acceuil")

    def create_click(self):
        self.hide()
        self.f2.show()
        
    def importer_click(self):
        self.hide()

        

        self.f2.show()
        self.importer.show()
        
