'''
Created on 31 mai 2018

@author: solly
'''


import unittest
from fablab.application import Fenetre
import os
from models.cellules import Stock, Recette, Cellule

class TestCellule(unittest.TestCase):
    '''Test class application'''

    def setUp(self):
        '''Set up the test
        '''
        cpath = os.getcwd()
        self.store_file_path = os.path.join(cpath, 'data_test')
        iStock = Stock(self.store_file_path)
        
        dictRecette = { 'tache1': 'Bielle assembler CageDeRoulement',
                        'tache2': 'CarterDePompe decouper'
                        }
        
        self.iRecette = Recette('nomProduit', dictRecette, iStock)

        self.iCellule = Cellule(self.iRecette)
        
    
    def testGoForProduction(self):
        '''Test la fonction go production
        '''
        ret = self.iCellule.goForProduction()
        print(ret)
        