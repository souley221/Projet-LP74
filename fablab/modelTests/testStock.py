'''
Created on 31 mai 2018

@author: solly
'''



import unittest
from models.cellules import Stock
import os

class TestStock(unittest.TestCase):
    '''Test class application'''
    
    def setUp(self):
        '''Initialisation de la classe
        '''
        cpath = os.getcwd()
        self.store_file_path = os.path.join(cpath, 'data_test')
        self.iStock = Stock(self.store_file_path)
        print('This store path:', self.store_file_path)
        self.piece_data = self.iStock.load_yaml(os.path.join(self.store_file_path,'stock_pieces.yaml'))
        self.machine_data = self.iStock.load_yaml(os.path.join(self.store_file_path,'stock_machines.yaml'))
    
    def test_loadyaml(self):
        '''Test load yaml file
        '''
        
        self.assertEqual(self.piece_data['Store']['Bielle']['quantite'], 2)
    
    def testAjouterPiece(self):
        '''Test la fonction ajouter piece
        '''
        ret = self.iStock.AjouterPiece('VIDE', 20)
        self.assertTrue(ret)
    
    def testGetAllPieces(self):
        '''Retourne toutes les pieces present dans le store
        '''
        ret = self.iStock.getAllPieces()
        expected = ['Bielle', 'CageDeRoulement', 'CarterDePompe', 'Courroie', 'Ecrou', 'Goupille']
        self.assertEqual(ret, expected)
    
    def testUsePiece(self):
        '''
        '''
        ret = self.iStock.UsePiece('Bielle', 0)
        self.assertTrue(ret)
    
    def testGetAllMachines(self):
        '''Retourne toutes les Machines presente dans le store
        '''
        ret = self.iStock.getAllMachins()
        expected = ['assemblage', 'limage',  'decoupage',  'tournage', 'transport']
        self.assertEqual(ret, expected)
    
    def testGetMachine1(self):
        '''Retourne une machine present dans le store
        '''
        ret = self.iStock.getMachin('assemblage')
        self.assertTrue(ret)

    def testGetMachine2(self):
        '''Retourne une machine present dans le store
        '''
        ret = self.iStock.getMachin('nonExist')
        self.assertFalse(ret)