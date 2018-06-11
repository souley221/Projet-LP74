'''
Created on 29 mai 2018

@author: pinguin
'''

import views
    
app = views.Application()                       
app.master.title('Cellule de production flexible')
app.master.geometry('800x600')
app.master.config(menu=app.createMenuBar())
app.mainloop()
