from bitcoin.rpc import RawProxy
import sys

if (len(sys.argv) > 1):
    transaction_id = sys.argv[1]
else:
    transaction_id = "0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2"

p = RawProxy()

#transaction_id = "4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d"
#transaction_id = "0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2"

raw_tx = p.getrawtransaction(transaction_id)
decoded_tx = p.decoderawtransaction(raw_tx)

tx_value = 0

for output in decoded_tx['vout']:
    tx_value = tx_value + output['value']

prev_tran = ""

input_value = 0
transaction_payment = 0

print(" ")
print("Total intputs : ")

for output in decoded_tx['vin']:
    input_tx_id = output['txid']
    input_vout_index = output['vout']

    input_raw_tx = p.getrawtransaction(input_tx_id)
    input_decoded_tx = p.decoderawtransaction(input_raw_tx)

    input_value = input_value + input_decoded_tx['vout'][input_vout_index]['value']

print(input_value)
transaction_payment = input_value - tx_value

print(" ")
print("Total outputs : ")
print(tx_value)

print(" ")
print("Transaction fees : ")
print(transaction_payment)
print(" ")

