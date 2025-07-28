from flask import Flask, render_template, request, jsonify
from datetime import datetime
import hashlib
import json

app = Flask(__name__)

# ------------------- Block Class -------------------

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Recalculate the hash of the block using its contents.
        """
        block_data = {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash
        }
        block_string = json.dumps(block_data, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

# ------------------- Blockchain Class -------------------

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the first block in the chain (Genesis Block).
        """
        genesis_block = Block(0, str(datetime.now()), "Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_block(self, data):
        """
        Add a new block with the given data.
        """
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), str(datetime.now()), data, last_block.hash)
        self.chain.append(new_block)

    def tamper_block(self, index, new_data):
        """
        Tamper the data of the block at a given index.
        """
        if 0 <= index < len(self.chain):
            self.chain[index].data = new_data
            # ⚠️ Note: Not updating the hash here is intentional — to detect tampering
            return True
        return False

    def is_chain_valid(self):
        """
        Check whether the blockchain is valid (untampered).
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.compute_hash():
                return False  # Tampering detected

            if current.previous_hash != previous.hash:
                return False  # Chain linkage broken

        return True

# ------------------- App & Routes -------------------

blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html', chain=blockchain.chain)

@app.route('/add_block', methods=['POST'])
def add_block():
    data = request.form['data']
    blockchain.add_block(data)
    return jsonify({"message": "Block added successfully!"})

@app.route('/tamper_block', methods=['POST'])
def tamper_block():
    index = int(request.form['index'])
    new_data = request.form['new_data']
    success = blockchain.tamper_block(index, new_data)
    if success:
        return jsonify({"message": f"Block {index} tampered with new data."})
    return jsonify({"message": "Invalid block index."})

@app.route('/validate_chain', methods=['GET'])
def validate_chain():
    is_valid = blockchain.is_chain_valid()
    return jsonify({"is_valid": is_valid})

@app.route('/get_chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append({
            'index': block.index,
            'timestamp': block.timestamp,
            'data': block.data,
            'hash': block.hash,
            'previous_hash': block.previous_hash
        })
    return jsonify(chain_data)

# ------------------- Run Server -------------------

if __name__ == '__main__':
    app.run(debug=True)
