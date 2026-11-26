import pytest

from src.models.personagem import Guerreiro
from src.models.habilidades import GritoDeGuerra

def test_habilidade_reduz_mana_GritoDeGuerra():
    guerreiro = Guerreiro("Conan")
    mana_atual = guerreiro.mana
    habilidade = GritoDeGuerra(20)
    habilidade.usar(guerreiro)
    mana_utilizada = habilidade.custo_mana

    assert guerreiro.mana == mana_atual - mana_utilizada, f"Esperado:{mana_atual - mana_utilizada}, Obtido:{mana_atual}"

def test_proibir_uso_habilidade_sem_mana_GritodeGuerra():
    guerreiro = Guerreiro("Conan")
    habilidade = GritoDeGuerra(20)
    guerreiro.mana = habilidade.custo_mana - 1
    mana_atual = guerreiro.mana
    
    resultado = habilidade.usar(guerreiro)
    assert guerreiro.mana == mana_atual, f"Esperado {mana_atual}, Obtido {guerreiro.mana}"
    assert resultado["efeito"] == "Nenhum", f"Esperado: Nenhum, Obtido: {resultado['efeito']}"

