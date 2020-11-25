# Python-bitcoinlib

## Installation instructions
To run the program code you need:

1. Download the program code
2. Download python:
 <br />[python](https://www.python.org/downloads/)
3. Install the python-bitcoinlib library: 
  <br /> `pip install python-bitcoinlib`
4. To perform code calculoation, you must have access to the Bitcoin full node 
5. Whe connected to Bitcoin full node, compile program code using
   <br /> `python` and the name of the choosen python file, for example:
   * test files
     *   <br /> `python 1.py`
     *   <br /> `python 2.py`
     *   <br /> `python 3.py`
   * task files
     *   <br /> `python 1uz.py`
     *   <br /> `python 2uz.py`
     
## Test files perform following actions
* 1.py - finds out the number of blocks in the bitcoin-core node
   * Terminal equivalent command → bitcoin-cli getblockchaininfo
* 2.py - derives the values of certain specific transaction
* 3.py - counts all specific block transaction transfers (outputs) 

## Task files perform following actions
* 1uz.py - program that calculates transaction fee of any given Bitcoin transaction (by providing its hash)
   * default transaction hash - 0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2
 ![1uz](/png/1.png)

* 2uz.py - program that retrieves the specified block header information and "checks" that the block hash is correct (the block is specified by providing its blockheight)
   * default blockheight - 277316
![2uz](/png/2.png)




