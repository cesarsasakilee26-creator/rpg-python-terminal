from abc import abstractmethod, ABC

class Item(ABC):
    def __init__(self, nome:str ,tipo:str, descricao:str, valor:int, peso:float):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.valor = valor
        self.peso = peso

    @abstractmethod
    def usar(self, alvo) -> bool:
        pass


class Pocao_Cura(Item):
    def __init__(self,cura:int):
        self.cura = cura
        super().__init__(nome = "Poção de Cura Baixo Nivel", tipo = "Poção", descricao= "Um liquido que cura um quantidade pequena da vida", valor= 25, peso= 0.5)

    def usar(self,alvo):
        alvo.vida += self.cura
        return True

class Arma(Item):
    def __init__(self, nome:str,tipo:str, descricao:str, valor:float, peso:float, dano:int):
        self.dano = dano
        super().__init__(nome, tipo, descricao, valor, peso)
        
        
    def usar(self, alvo):
        alvo.arma_equipada = self
        return True 


class Armadura(Item):
    def __init__(self,nome:str,tipo:str,descricao:str,valor:float,peso:float,defesa:int):
        self.defesa = defesa
        super().__init__(nome,tipo,descricao,valor,peso)


    def usar(self,alvo):
        alvo.armadura_equipada = self
        return True


