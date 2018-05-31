'''
Created on 29 mai 2018

@author: solly
'''

import tkinter as tk

import os

class Fenetre():
    
    def __init__(self, name):
        '''Initialisation
        '''
        self.name = name
     
    def createWindow(self):
        '''Creation fenetre
        '''
        fenetre = tk.Tk(baseName="Machine de fab")
        fenetre.title(self.name)
        p = tk.PanedWindow(fenetre, orient=tk.HORIZONTAL)
        p.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=2, padx=2)
        
        
        produitFinisFrame = tk.Frame(fenetre, borderwidth=2, relief=tk.GROOVE)
        cellulesFrame = tk.Frame(fenetre, borderwidth=2, relief=tk.GROOVE)
        cellulesFrame.pack(side=tk.RIGHT, padx=30, pady=30)
        produitFinisFrame.pack(side=tk.RIGHT, padx=30, pady=30)
        
        
        p.add(cellulesFrame)
        p.add(produitFinisFrame)
        
        p.pack()
        
        #Label(produitFinis, text="Produits finis").pack(padx=10, pady=10)
        fenetre['bg']='gray'
        cellulesLabelFrame = self.createLabelFrame(cellulesFrame, "CELLULES")
        
        
        
        produitfinisLabelFrame = self.createLabelFrame(produitFinisFrame, "PRODUITS FINIS")
        self.addImage(cellulesLabelFrame, os.path.join("assimagepng.png"), 250, 250)

        return fenetre

    def createLabelFrame(self, fenetre, labelname, position=''):
        '''Creation du label frame
        '''
        label = tk.LabelFrame(fenetre, text=labelname,  padx=20, pady=20)
        label.pack(fill="both", expand="yes", anchor=tk.NW)
        tk.Label(label, text="LES DIFFERENTES MACHINES DE FABRICATION").pack()
        
        return label 
    
    def addImage(self, fenetre, filename, taille1, taille2):
        '''
        Add image to a canvas
        '''
        photo = tk.PhotoImage(file=filename)
        canvas = tk.Canvas(fenetre, width=taille1, height=taille2)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.pack()
        tk.mainloop()
        
        