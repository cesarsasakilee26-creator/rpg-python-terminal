from abc import ABC, abstractmethod
from src.models.inventario import Inventario
from src.models.item import Arma,Armadura
from src.models.monstro import Monstro
from time import sleep
class Personagem(ABC):
    def __init__(self, nome_personagem:str, vida:int, mana:int, dano_base):
        self.nome_personagem = nome_personagem
        self.vida = vida
        self.mana = mana
        self.inventario = Inventario()
        self.arma_equipada = None
        self.armadura_equipada = None
        self.dano_base = dano_base
        
    @abstractmethod 
    def atacar(self) -> int: 
        pass
        
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




print("--- TESTE DE COMBATE E ARMADURA ---")
sleep(1)

# 1. Cenário: Sem armadura
lucas = Guerreiro("Lucas")
print(f"1. Vida inicial do Lucas: {lucas.vida}")
sleep(1)

print("\n[Ataque] Lucas recebeu 30 de dano SEM armadura!")
lucas.receber_dano(30)
print(f"-> Vida atual: {lucas.vida} (Deveria ser 90)")
sleep(1)

# 2. Cenário: Com armadura, dano alto
print("\n[Equipamento] Lucas equipou o Escudo de Ferro (Defesa: 15)!")
escudo = Armadura("Escudo de Ferro", "Armadura", "Proteção pesada", 100, 5.0, 15)
escudo.usar(lucas)
sleep(1)

print("\n[Ataque] Lucas recebeu 30 de dano COM armadura!")
lucas.receber_dano(30)
print(f"-> Vida atual: {lucas.vida} (Deveria ser 75, pois 30 - 15 = 15 de dano real)")
sleep(1)

# 3. Cenário: A ARMADILHA (Dano menor que a defesa)
print("\n[Ataque Fraco] Lucas recebeu apenas 10 de dano (menor que a defesa de 15)!")
lucas.receber_dano(10)
print(f"-> Vida atual: {lucas.vida} (Deveria CONTINUAR 75. Se subiu para 80, o bug da cura aconteceu!)")
sleep(1)

print("\n--- FIM DO TESTE ---")
