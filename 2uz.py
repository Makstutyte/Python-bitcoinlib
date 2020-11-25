from bitcoin.rpc import RawProxy
import binascii
import hashlib
import struct
import sys


if (len(sys.argv) > 1):
    blockheight = int(sys.argv[1])
else:
    blockheight = 277316

p = RawProxy()

blockhash = p.getblockhash(blockheight)
block = p.getblock(blockhash)

print("")
print(str(blockheight) + " block hash:               " + block['hash'])

def little_endian_int(value):
    # endian = struct.pack('<I', value).encode('hex')
    endian = struct.pack('<I', value)
    hex = binascii.hexlify(endian)
    return hex 

def little_endian_string(value):
    # bin = value.decode('hex')
    bin = binascii.unhexlify(value)
    hex = bin[::-1]
    endian = binascii.hexlify(hex)
    return endian

version = little_endian_string(block['versionHex'])

previous_hash = little_endian_string(block['previousblockhash'])

merkle_root = little_endian_string(block['merkleroot'])

time = little_endian_int(block['time'])

bits = little_endian_string(block['bits'])

nonce = little_endian_int(block['nonce'])

header_hex = version + previous_hash + merkle_root + time + bits + nonce

header_bin = header_hex.decode('hex')
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest() 
hash = hash[::-1].encode('hex_codec') 

print(str(blockheight) + " calculated hash:          " + hash)
print("")

if (block['hash'] == hash):
    print("Hashes match")
else:
    print("Hashes mismatch")
print("")