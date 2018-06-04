'''
Created on 31 mai 2018

@author: solly
'''
from models.cellules import Recette, Stock
import os
'''
Created on 31 mai 2018

@author: solly
'''


import unittest

class TestRecette(unittest.TestCase):
    '''Test class Recette'''

    
    def setUp(self):
        '''Set Up the application
        '''
        cpath = os.getcwd()
        self.store_file_path = os.path.join(cpath, 'data_test')
        iStock = Stock(self.store_file_path)
        
        dictRecette = { 'tache1': 'pp1 assembler pp2',
                            'tache2': 'pp1 decouper',
                            'tache3':'pp0 limer',
                            'tache4': 'pp0 transporter'
                        }
        
        self.iRecette = Recette('nomProduit', dictRecette, iStock)
    
    def testretrieveMachins(self):
        '''Tester la fonction retrieve machine
        '''
        ret = self.iRecette.retrieveMachins()
        expected = ['assemblage', 'decoupage', 'limage', 'transporteur']
        self.assertEqual(expected, ret)
    
    def testretrievePieces(self):
        '''Tester la fonction retrieve Pieces
        '''
        ret = self.iRecette.retrievePartPiece()
        expected = ['pp2', 'pp1', 'pp0']
        self.assertListEqual(sorted(expected), sorted(ret))
        
