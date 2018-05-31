'''
Created on 29 mai 2018

@author: solly
'''
import unittest
from fablab.application import Fenetre

class TestApplication(unittest.TestCase):
    '''Test class application'''


    def testFenetre(self):
        '''Test fenetre
        '''
        fenetre = Fenetre("Ma fenetre")
        mfn = fenetre.createWindow()
    
    def testcreateLabelframe(self):
        '''
        '''
        fn = Fenetre("MA FENETRE")
        fenetre = fn.createWindow()
        
        
        
        
    