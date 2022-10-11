from blockchain import Blockchain

blockchain=Blockchain()

blockchain.new_block(2321, 829789273863782)
print(blockchain.hash(blockchain.last_block))
print(blockchain.last_block)