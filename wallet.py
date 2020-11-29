"""
本文件中包含了Wallet类，是用户端的基本组件
"""

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
import os
import copy
import other
from UTXO import UTXO
class Wallet:
    ID:hex
    Random:list
    curve:ec.EllipticCurve
    data:dict
    def __init__(self):
        """
        curve：加密使用的曲线名称
        data：一个dict，key为os.urandom生成16位随机串的int形式，
        value为一个UTXO，包含一个地址（公钥）和一个余额（默认为0）
        address:钱包本身的地址
        """
        self.curve = ec.SECT571R1()
        originRandom = int.from_bytes(os.urandom(16),'big')
        self.data={originRandom:UTXO(originRandom,0)}
        self.Random = [originRandom]
        self.ID = ec.generate_private_key(self.curve).public_key().public_bytes(Encoding.X962,PublicFormat.UncompressedPoint).hex()
    def generateUTXO(self,cash=0):
        """
        生成一对UTXO并添加到钱包的序列中,余额默认为0
        """
        Random = int.from_bytes(os.urandom(16),'big')
        self.data[Random] = UTXO(Random,cash)
        self.Random.append(Random)
    def update(self):
        keys = copy.deepcopy(list(self.data.keys()))
        for i in keys:
            if(self.data[i].cash == 0):
                self.data.pop(i)
                self.Random.remove(i)
        if not self.data:
            self.generateUTXO()
    def getBalance(self)->float:
        self.update()
        balance = 0
        for i in self.data.keys():
            balance += self.data[i].cash
        return balance
    def show(self):
        self.update()
        for i in self.data.keys():
            print(i,self.data[i].cash)
    def trans(self,moneyNeed:int):
        if self.getBalance()<moneyNeed:
            raise other.InsufficientError
        else:
            pass#TODO


wallet = Wallet()
wallet.generateUTXO(10)
wallet.generateUTXO(20)
wallet.generateUTXO(2.5)
wallet.trans(100)
wallet.show()