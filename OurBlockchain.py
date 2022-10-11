import hashlib
import glob

class Block:
    def __init__(self, message, hash_of_past):
        self.message=message
        self.hash_of_past=hash_of_past
    def save(self, dir):
        f=open(dir+'/'+str(self.hash_of_past)+'.txt', 'w')
        f.write(self.message)
        f.close()
    def __hash__(self):
        return hashlib.sha256(self.message.encode()).__hash__()





class Blockchain:

    def __init__(self):
        self.dir = 'blocks'
        self.data='data'
        self.blocks=[]
        for path in glob.glob(self.dir+'/**.txt'):
            print(path)
    def add_block(self, message):

        if len(self.blocks)!=0:
            message+=('/n'+str(self.blocks[len(self.blocks)-1].__hash__()))
            block=Block(message, self.blocks[len(self.blocks)-1].__hash__())
        else:
            message += ('/n' + '1')
            block = Block(message, 1)
        self.blocks.append(block)
        block.save(self.dir)
        f=open(self.data+'/hash_of_past.txt', 'w')
        f.write(str(block.__hash__()))
        f.close()


blockchain=Blockchain()
blockchain.add_block("sdfjsdjf")
blockchain.add_block('oshfdiuhfu')

print(blockchain.blocks[1])