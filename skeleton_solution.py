from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from datetime import datetime

rpcuser='quaker_quorum'
rpcpassword='franklin_fought_for_continental_cash'
rpcport=8332
rpcip='3.134.159.30'

rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, rpcip, rpcport))

#Question 1 - Hash of genesis block
print("Question 1:")
commands = [ [ "getblockhash", height] for height in range(1) ]
block_hashes = rpc_connection.batch_(commands)
blocks = rpc_connection.batch_([ [ "getblock", h ] for h in block_hashes ])
block_times = [ block["time"] for block in blocks ]
print(blocks)

#Question 2 - Timestamp of genesis block
print("Question 2:")
timestamp = datetime.utcfromtimestamp(block_times[0])
print(timestamp)

#Question 3 - Blockcount
print("Question 3:")
initial_index = 685

commands = [ [ "getblockhash", height] for height in range(initial_index, initial_index+10) ]
block_hashes = rpc_connection.batch_(commands)
blocks = rpc_connection.batch_([ [ "getblock", h ] for h in block_hashes ])
block_times = [ block["time"] for block in blocks ]

i = 0
while i < len(blocks):
    j = i + initial_index
    print("Index: ", j)
    print(blocks[i])
    print(datetime.utcfromtimestamp(block_times[i]))
    i = i + 1

