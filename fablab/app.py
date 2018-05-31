'''
Created on 29 mai 2018

@author: pinguin
'''
import tkinter as tk
from tkinter import Canvas
from tkinter.constants import HORIZONTAL, VERTICAL


class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.paned = self.createWindowPanel()
        self.pack()
       
    
    def createWindowPanel(self):
        #Créer le layout panneaux
        paneWindow = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        paneWindow.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=0, padx=0)
        
        #Créer le panneau avec les options
        settingLabelFrame = tk.LabelFrame(paneWindow, text="Options",  padx=0, pady=0)
        settingLabelFrame.pack(fill=tk.BOTH, expand="yes")
        tk.Label(settingLabelFrame, text="Produit Fini").pack()
        self.createList(settingLabelFrame)

        #Créer le panneau avec les vues
        cellulesLabelFrame = tk.LabelFrame(paneWindow, text="Cellule",  padx=0, pady=0)
        cellulesLabelFrame.pack(fill=tk.BOTH, expand="yes")
        tk.Label(cellulesLabelFrame, text="Production").pack()
        self.createScrollableCanvas(daddy=cellulesLabelFrame)
        
        paneWindow.add(cellulesLabelFrame)
        paneWindow.add(settingLabelFrame)
        
        paneWindow.pack()
        
        return paneWindow

    def createScrollableCanvas(self, daddy):
        self.draw = Canvas(daddy, width="5i", height="5i", 
                           background="black",
                           scrollregion=(0,0,"20i","20i"))
        self.draw.scrollX = tk.Scrollbar(daddy, orient=HORIZONTAL)
        self.draw.scrollY = tk.Scrollbar(daddy, orient=VERTICAL)
        
        self.draw['xscrollcommand'] = self.draw.scrollX.set
        self.draw['yscrollcommand'] = self.draw.scrollY.set
        self.draw.scrollX['command'] = self.draw.xview
        self.draw.scrollY['command'] = self.draw.yview
        
        self.draw.create_rectangle(0, 0, "3.5i", "3.5i", fill="blue")
        self.draw.create_rectangle("10i", "10i", "13.5i", "13.5i", fill="white")
        
        self.draw.scrollX.pack(side=tk.BOTTOM, fill=tk.X)
        self.draw.scrollY.pack(side=tk.RIGHT, fill=tk.Y)
        self.draw.pack(side=tk.LEFT)
    
    def createMenuBar(self):
        menubar = tk.Menu(self)
        menu1 = tk.Menu(menubar, tearoff=0)
        menu1.add_command(label="Créer")
        menu1.add_command(label="Editer")
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=self.quit)
        menubar.add_cascade(label="Fichier", menu=menu1)
        
        menu2 = tk.Menu(menubar, tearoff=0)
        menu2.add_command(label="Couper")
        menu2.add_command(label="Copier")
        menu2.add_command(label="Coller")
        menubar.add_cascade(label="Editer", menu=menu2)
        
        menu3 = tk.Menu(menubar, tearoff=0)
        menu3.add_command(label="A propos")
        menubar.add_cascade(label="Aide", menu=menu3)
        
        return menubar

        
    def createQuitButton(self):
        self.quitButton = tk.Button(self, text='Quit',
                                    command=self.quit)            
        self.quitButton.pack()
        
    def createButton(self, text):
        self.button = tk.Button(self, text=text,
            command=self.createList)            
        self.button.pack()
        
    def createList(self, daddy):
        self.list = tk.Listbox(daddy);
        self.list.insert(tk.END, "coucou")
        self.list.insert(tk.END, "coucou")
        self.list.insert(tk.END, "coucou")
        self.list.insert(tk.END, "coucou")
        self.list.pack()
        
app = Application()                       
app.master.title('Machina')
app.master.geometry('800x600')
app.master.config(menu=app.createMenuBar())
app.mainloop()
