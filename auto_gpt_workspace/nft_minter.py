class NFT:
    def __init__(self, token_id, asset_file):
        self.token_id = token_id
        self.asset_file = asset_file
        self.metadata = {}

    def set_metadata(self, key, value):
        self.metadata[key] = value

    def __str__(self):
        return f'Token ID: {self.token_id}, Asset file: {self.asset_file}, Metadata: {self.metadata}'

def hash_asset(asset_file):
    #TODO: Implement fast hashing method
    return hash(asset_file) % (10 ** 6)

def mint_nft(asset_file):
    # hash the file
    file_hash = hash_asset(asset_file)
    # generate the token id
    token_id = hash(file_hash)
    # create the NFT and add to collection
    nft = NFT(token_id, asset_file)
    nft_collection.add(nft)
    return nft