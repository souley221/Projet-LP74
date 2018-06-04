'''
Created on 29 mai 2018

@author: solly
'''

import yaml
import os

def dump_to_yaml(filename, data):
    '''Dump a dictionary data into yaml file
    '''
    with open(filename, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
        return 'Dump is OK'
    return 'Error while dumping data to yaml'

class Cellule():
    '''Classe contenant nos differentes machine 
    de fabrication
    '''
    def __init__(self, iRecette):
        '''
            Initialisation de la classe Cellule
            @param machinName: Nom de la machine a utilise
            @param machinImage: Image de la machine
        '''
        #Machine et piece necessaire pour la fabrication de notre produit finis
        self.pieceFabrication = iRecette.retrievePartPiece()
        self.machineFabrication = iRecette.retrieveMachins()
        
        #Machines et pieces presentes dans le stock
        self.storePieces = iRecette.storePieces
        self.storeMachins = iRecette.storeMachins
        
    def goForProduction(self):
        '''Retoune true si la fabrication est possible 
                Fabrication possible si toutes les pieces et machines impliquees sont presentes dans le stock
        '''
        piecesFabrication = self.pieceFabrication
        machinesFabrication = self.machineFabrication
        
        storePieces = self.storePieces
        storeMachins= self.storeMachins
        
        not_present_pieces = []
        not_present_machins = []
        
        print('Machines Necessaire Fabrication:', machinesFabrication)
        print('Pieces Necessaire Fabrication:', piecesFabrication)
        print('-------------------------------------------------------------')
        print('Pieces dans store: ',storePieces)
        print('Machines dans store: ',storeMachins)
        print('--------------------------------------------------------------')
        for val in piecesFabrication:
            if val not in storePieces:
                print('Cette piece nest pas present:', val)
                not_present_pieces.append(val)
        for val in machinesFabrication:
            if val not in storeMachins:
                print('Cette machine nest pas present:', val)
                not_present_machins.append(val)
        
        if not not_present_machins and not_present_pieces:
            return True
        return False
    
    



class Recette():
    '''Classe contenant mes recettes et permettant de faire le produit
    '''
    def __init__(self, nomProduitFinis, dictRecette, iStock):
        '''Initialisation de la classe Recette
        @param idictRecette: Dictionnaire contenant le id de la tache et 
        son procede de fabrication
        @example: dictRecette:{'tache1': 'partpiece1 assembler partpiece2',
                                'tache2': 'pp2 couper'}
        @param: iStock:  Instance du stock (Permet de recuperer les donnees du st
        '''
        self.nomProduitFinis = nomProduitFinis
        self.dictRecette = dictRecette
        self.storePieces = iStock.getAllPieces()
        self.storeMachins =  iStock.getAllMachins()
    
    def setFinalRecette(self):
        '''Construit le dictionnaire final avec le 
        nom du produit et la liste des tache correspondante
        '''
        final_store_dict = {self.nomProduitFinis:{dictRecette}}
        return final_store_dict
    
    def retrieveMachins(self):
        '''Retourne toutes les machines necessaire pour fabriquer 
        le produit
        '''
        listTache = []
        nomMachine = []
        nomActions = []
        for tsk in self.dictRecette:
            listTache.append(self.dictRecette[tsk].split(' '))

        for listT in listTache:
            nomActions.append(listT[1])

        #Construire le nom de machine
        for nomA in nomActions:
            if nomA.endswith('er') and nomA !='transporter':
                nomM = nomA.strip('er')+'age'
                nomMachine.append(nomM)
            if nomA in ['transport', 'transporter']:
                nomMachine.append('transporteur')
        return nomMachine
        
    def retrievePartPiece(self):
        '''Recuperer les differents part pieces utilise lors de la fabrication
        '''
        listTache = []
        listPiece = []
        
        for tsk in self.dictRecette:
            listTache.append(self.dictRecette[tsk].split(' '))
        for listT in listTache:
            if len(listT)>2:
                listPiece.append(listT[0])
                listPiece.append(listT[2])
            if len(listT)==2 and listT[0] not in listTache:
                listPiece.append(listT[0])

        return list(set(listPiece))


class Stock():
    '''Classe gerant le stock des part pieces
    '''
    def __init__(self, store_path):
        '''Initialisation de la classe Stock
        Le stock est un fichier yaml contenant les donnees
        '''
        
        self.piecestore_path = os.path.join(store_path,'stock_pieces.yaml')
        self.machinestore_path = os.path.join(store_path, 'stock_machines.yaml')
        
        self.piece_store_data = self.get_piece_store_data()
        self.machine_store_data = self.get_machine_store_data()
    
    def load_yaml(self, filename):
        '''Load store data yaml file
        '''
        with open(filename) as stream:
            yaml_data = yaml.load(stream)
        return yaml_data

    def get_piece_store_data(self):
        '''Get all data from the pieces store
        '''
        store_data = self.load_yaml(self.piecestore_path)
        return store_data

    def get_machine_store_data(self):
        '''Get all data from the pieces store
        '''
        store_data = self.load_yaml(self.machinestore_path)
        return store_data
            
    def AjouterPiece(self, nomPiece, qte=1):
        '''Ajouter une nouvelle piece dans le store
        '''
        if nomPiece in self.piece_store_data['Store']:
            self.piece_store_data['Store'][nomPiece]['quantite'] += qte
        else:
            self.piece_store_data['Store'][nomPiece]={'quantite': qte}
        dump_ret = dump_to_yaml(self.piecestore_path, self.piece_store_data)
        if dump_ret == 'Dump is OK':
            return True
        return False
    
        
    def getAllPieces(self):
        '''Retourne toutes les pieces present dans le store
        '''
        pieceList = []
        store_data = self.piece_store_data
        
        for key in store_data['Store']:
            pieceList.append(key)
        return pieceList

    def UsePiece(self, nomPiece, qte=1):
        '''Utilise une piece si elle est presente dans le store
        lors de la fabrication dun produit finis
        '''
        if nomPiece not in self.piece_store_data['Store']:
            raise ('Piece non presente')
        elif self.piece_store_data['Store'][nomPiece]['quantite'] < qte:
            raise ('Quantite insuffisante')
        
        self.piece_store_data['Store'][nomPiece]['quantite'] -=qte
        dump_ret = dump_to_yaml(self.piecestore_path, self.piece_store_data)
        if dump_ret == 'Dump is OK':
            return True
        return False
    
    def getMachin(self, machinName):
        '''Retourne une machine dont le nom est donne en parametre 
        @param machinName: Le nom de la machine cherche
        '''
        store_data = self.machine_store_data
        
        if machinName not in store_data['Store']:
            return False
        return True
    
    def getAllMachins(self):
        '''Recupere toutes les machines
        '''
        machinList = []
        store_data = self.machine_store_data
        
        for key in store_data['Store']:
            machinList.append(key)
        return machinList
    
    def AjouterMachine(self, nomMachine, qte=1):
        '''Ajouter une nouvelle piece dans le store
        '''
        if nomMachine in self.machine_store_data['Store']:
            self.machine_store_data['Store'][nomMachine]['quantite'] += qte
        else:
            self.machine_store_data['Store'][nomMachine]={'quantite': qte}
        dump_ret = dump_to_yaml(self.machinestore_path, self.machine_store_data)
        if dump_ret == 'Dump is OK':
            return True
        return False
        