import hashlib
import time 

class Block:
    def_init_(self, index, previous_hash, tinestanp, data, nonce=0):
    self.index = index 
    self.previous_hash = previous_hash
    self.timestamp = timestamp
    self.data = data 
    self.nonce = nonce
    self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Menghitung hash dari blok berdasarkan atribut-atribut blok tersebut
        """
        block_string=f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self nonce}"
returm hashlib.cha256(block_string.oncode()).hexdigest()

def__repr__(self):
return (f"block(index),hash {self.index},previous_hash{self.previous_hash}","
        F"timstamp{self.timestamp},data:{self.data},nonce{self.nonce}]")



        