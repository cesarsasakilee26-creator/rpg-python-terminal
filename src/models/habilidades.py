from abc import ABC, abstractmethod    
class Habilidade(ABC):
    def __init__(self, nome: str, descricao: str, custo_mana: int):
        self.nome = nome
        self.descricao = descricao
        self.custo_mana = custo_mana

    @abstractmethod
    def usar(self,  usuario: 'Personagem', alvo = 'None') -> dict:
        # Retorna um dicionario com resultado:{'dano': int, 'efeito': str, 'mensagem': str} 
        ...

    def pode_usar(self, mana_atual: int) -> bool:
        return mana_atual >= self.custo_mana


class GritoDeGuerra(Habilidade):
    def __init__(self, valor_buff: int):
        self.valor_buff = valor_buff
        super().__init__(nome="Grito de Guerra", descricao = "Aumenta o ataque por 3 turnos.", custo_mana = 20)
    def usar(self, usuario = 'Personagem', alvo=None) -> dict:
        
        
        if not self.pode_usar(usuario.mana):
            return {f'aumento de dano': 0, 'efeito': 'Nenhum', 'mensagem': f"{usuario.nome_personagem} não tem mana suficiente para usar {self.nome}."}

        usuario.mana -= self.custo_mana
        usuario.dano_base += self.valor_buff # Aumenta o ataque do por 3 turnos
        return {'aumento de Dano': self.valor_buff, 'efeito': 'Aumento de Ataque', 'mensagem': f"{usuario.nome_personagem} usou {self.nome}!"}

    