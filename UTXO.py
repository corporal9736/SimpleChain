"""
本文件中包含了UTXO类，是所有交易的最基本元素
"""

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
import os

class UTXO:
    '''
    address：用显式的random值生成一个不可见的私钥，再生成一个公钥，公钥的十六进制表示即为address
    cash：当前address的余额
    '''
    address:hex
    cash:float
    def __init__(self,random,cash,curve=ec.SECT571R1()):
        privateKey = ec.derive_private_key(random,curve)
        publicKey = privateKey.public_key()
        self.address = publicKey.public_bytes(Encoding.X962,PublicFormat.UncompressedPoint).hex()
        self.cash = cash
    def enough(self,amount):
        '''
        用于检查账户中的余额是否足够转账，amount代表需求的金额
        '''
        return self.cash > amount
    



