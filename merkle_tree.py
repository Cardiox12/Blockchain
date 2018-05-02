from functools import reduce
import hashlib

hashes = []

def createHash():
    infos = {
            "Tony": "Bellavia",
            "Cynthia": "Petit",
            "Mathilde":"Saliou",
            "Safae": "Loummou"
            }

    for prenom, nom in infos.items():
        hash = hashlib.new("sha256")
        hash.update(str(prenom).encode("utf-8"))
        hash.update(str(nom).encode("utf-8"))
        hashes.append(hash.hexdigest())


def merkle_tree(array):
    """ Need at least two nodes for merkle tree, if the number of hashes is unpair add one hash """
    #Hash dans lambda
    hash = hashlib.new("sha256")
    node = reduce(lambda x, y: str(x + y), array)
    print(node)


createHash()
# print(hashes)
print("Final hash / {0} /".format(merkle_tree(hashes)))
