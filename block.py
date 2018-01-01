import hashlib


class Block(object):
    def __init__(self, blockNumber, data, previousHash):
        self.blockNumber = blockNumber
        self.nonce = 0
        self.data = data
        self.previousHash = previousHash
        
        self.hash = hashlib.new("sha256")
        self.hash.update(str(self.blockNumber).encode("utf-8"))
        self.hash.update(str(self.nonce).encode("utf-8"))
        self.hash.update(self.data.encode("utf-8"))
        self.hash.update(str(self.previousHash).encode("utf-8"))
    
        # self.mine()
    
    def getHash(self):
        """ Return le hash en str """
        return self.hash.hexdigest()

    def mine(self):
        """ Incrémente nonce jusqu'à ce que les 4 premiers caractères du hash soient 0000 """
        while self.isValid() != True:
            self.nonce += 1
            
            self.hash.update(str(self.blockNumber).encode("utf-8"))
            self.hash.update(str(self.nonce).encode("utf-8"))
            self.hash.update(self.data.encode("utf-8"))
            
            print("Hash : {}".format(self.getHash()))
        
        print("Is valid for nonce {0}".format(self.nonce))

    def isValid(self):
        """ Si les 4 premiers cractères sont 0000 return True, sinon le hash n'est pas valide et on incrémente nonce """
        container = list(str(self.getHash()))
        if container[0] == "0" and container[1] == "0" and container[2] == "0" and container[3] == "0":
            return True
        else:
            return False


if __name__ == "__main__":
    monPremierBlock = Block(1, "bonjour ", "")
    print(monPremierBlock.data)


