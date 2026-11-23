from abc import ABC, abstractmethod
from src.models.inventario import Inventario
from src.models.item import Arma,Armadura
from src.models.monstro import Monstro
from time import sleep
class Personagem(ABC):
    def __init__(self, nome_personagem:str, vida:int, mana:int, dano_base):
        self.nome_personagem = nome_personagem
        self.vida_maxima = vida
        self.mana_maxima = mana
        self.vida = vida
        self.mana = mana
        self.inventario = Inventario()
        self.arma_equipada = None
        self.armadura_equipada = None
        self.dano_base = dano_base
        
    @abstractmethod 
    def atacar(self) -> int: 
        pass
        
    def esta_vivo(self) -> bool:
         return self.vida > 0


    def tem_mana(self) -> bool:
         return self.mana > 0
    
    @abstractmethod
    def usar_habilidade(self) -> int:
        pass

    @property
    def vida(self):
            return self._vida

    @vida.setter
    def vida(self,valor):
        if valor < 0:
                print("ERRO! VIDA NÃO PODE SER MENOR QUE 0, AJUSTANDO PARA 0!")
                self._vida = 0
        
        elif valor > self.vida_maxima:
                print("ERRO! VIDA NÃO PODE SER MAIOR QUE A VIDA MÁXIMA, AJUSTANDO PARA A VIDA MÁXIMA!")
                self._vida = self.vida_maxima
        else:
                self._vida = valor

    def receber_dano(self, dano:int):
         if self.armadura_equipada:
                dano_efetivo = max(dano - self.armadura_equipada.defesa, 0)
                self.vida -= dano_efetivo
        
         else:
                self.vida -= dano

class Guerreiro(Personagem):
    def __init__(self, nome_personagem:str):
        super().__init__(nome_personagem = nome_personagem, vida = 120, mana = 20, dano_base = 50 )

    def atacar(self) -> int:
        if self.arma_equipada:
             dano = self.dano_base + self.arma_equipada.dano
        else:
             dano = self.dano_base

        return dano

    def usar_habilidade(self) -> int:
        return 25


class Mago(Personagem):
    def __init__(self, nome_personagem:str):
        super().__init__(nome_personagem = nome_personagem, vida = 90, mana = 80, dano_base= 20)
        
    def atacar(self) -> int:
        if self.arma_equipada:
             dano = self.dano_base + self.arma_equipada.dano
        else:
             dano = self.dano_base

        return dano
    
    def usar_habilidade(self) -> int:
        return 25


class Arqueiro(Personagem):
    def __init__(self, nome_personagem:str):
        super().__init__(nome_personagem = nome_personagem, vida = 95, mana = 30, dano_base= 40)

    def atacar(self) -> int:
        if self.arma_equipada:
             dano = self.dano_base + self.arma_equipada.dano
        else:
             dano = self.dano_base

        return dano

    def usar_habilidade(self) -> int:
        return 25
