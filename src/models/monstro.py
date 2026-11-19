class Monstro:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            print("ERRO! VIDA NÃO PODE SER MENOR QUE 0, AJUSTANDO PARA 0!")
            self._vida = 0
        else:
            self._vida = valor

    def receber_dano(self, dano):
        dano_efetivo = max(dano - self.defesa, 0)
        self.vida -= dano_efetivo

    def atacar(self):
        return self.ataque