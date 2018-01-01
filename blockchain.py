from block import Block
import hashlib, sys

# Mettre dans while code da la fonction allowToCreate

class Blockchain(object):
    def __init__(self):
        # On stock les blocks dans ce tableau
        self.blocks = []
        # On incrémente le numéro de block à chaque nouvelle instanciation
        self.blockNumber = 0
        # On stock le hash courant pour le fournir en paramètre à la création du nouveau block
        self.currentHash = ""
    
        #self.allowToCreateNextBlock()
    
        repeat = "o"
        
        while repeat == "o":
            self.allowToCreateNextBlock()
            repeat = str(input("Voulez vous créer un nouveau block ? o/n : "))
            
            if len(self.blocks) > 3:
                self.blocks[-2].data == "New data"
                print(self.blocks[-2].data) # Enlever après test
                print("Je suis dans la boucle et je change les données") # Enlever après test
    
    def allowToCreateNextBlock(self):
        """ Permet de créer un nouveau block si le block courant et les blocks précédents sont valides sinon """
        # Si les blocks précédents sont corrompus alors le hash des blocks suivants ne sont plus valides
        if len(self.blocks) == 0 or self.blocks[-1].isValid() == True and self.previousBlocksAreValid() == True:
            self.blockNumber += 1
            self.currentData = str(input("Insert data for block {0} : ".format(self.blockNumber)))
            self.blocks.append(Block(self.blockNumber, self.currentData, self.currentHash))
            self.blocks[-1].mine()

    def previousBlocksAreValid(self):
        """ Renvoie true si les blocks précédents sont valides """
        # USE THE MERKEL TREE POUR VERIFIER L'AUTHENTICITE DES BLOCKS PRÉCÉDENTS
        for block in self.blocks:
            if block.isValid():
                # print("Le block est valide")
                return True
            else:
                # print("Le block n'est pas valide")
                sys.stderr.write("Block number {0} is corrupt".format())
                # block.mine()
                return False

    def merkelTree(self):
        """ Cette fonction a pour but de s'assurer que les blocks précédents sont inchangés, et de remplacer la fonction previousBlocksAreValid """
        

def displayBlockInfo(blockchain):
    print("-"*72)
    for block in blockchain.blocks:
        print("Block number {0} \nnonce : {1} \nhash : {2} \nData : ".format(block.blockNumber, block.nonce, block.getHash(), block.data))
        print("-"*72)


maBlockchain = Blockchain()
displayBlockInfo(maBlockchain)
