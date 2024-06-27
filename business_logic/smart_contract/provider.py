import json
from web3 import Web3
import os
from django.conf import settings
import time

# Initialize web3 with Infura URL

from django.conf import settings
infura_url = settings.INFURA_URL
contract_address = Web3.to_checksum_address(os.getenv('CONTRACT_ADDRESS'))
wallet_address = Web3.to_checksum_address(os.getenv('WALLET_ADDRESS'))
private_key = settings.PRIVATE_KEY

web3 = Web3(Web3.HTTPProvider(infura_url))

# Load contract ABI
with open('/Users/timothy/Desktop/Kingdom_Projects/quiz-api/business_logic/smart_contract/dumb_ques.json', 'r') as abi_file:  # Replace with your ABI file path
    contract_abi = json.load(abi_file)


# account = web3.eth.account.create()

# # Get the address and private key
# wallet_address = account.address
# private_key = account._private_key.hex()

print(f'Wallet Address: {wallet_address}')
print(f'Private Key: {private_key}')


# Contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def save_game_scores(team_name, score, from_address, private_key):
    from_address = Web3.to_checksum_address(from_address)
    nonce = web3.eth.get_transaction_count(from_address)

    # Estimate gas limit
    estimated_gas = contract.functions.saveGameScores(team_name, score).estimate_gas({'from': from_address})
    

    # Adjust the gas price and gas limit
    gas_price = web3.to_wei('10', 'gwei')  # Lower gas price
    gas_limit = estimated_gas + 50000
    txn = contract.functions.saveGameScores(team_name, score).build_transaction({
        'chainId': 11155111,  # Sepolia Testnet chain ID
        'gas': gas_limit,
        'gasPrice': gas_price,
        'nonce': nonce,
        'from': from_address
    })

    signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.to_hex(tx_hash)

def get_all_game_details():
    return contract.functions.getAllGameDetails().call()


import time

def wait_for_confirmation(tx_hash):
    print("Waiting for transaction confirmation...")
    while True:
        tx_receipt = web3.eth.get_transaction_receipt(tx_hash)
        if tx_receipt is not None:
            print("Transaction confirmed!")
            break
        time.sleep(10) 
