import pytest
from src.models.personagem import Guerreiro
from src.models.item import Arma, Armadura, Pocao_Cura


def test_pocao_de_cura():
    guerreiro = Guerreiro("Conan")
    pocao = Pocao_Cura(cura=30)

    vida_inicial = guerreiro.vida
    pocao.usar(guerreiro)

    assert guerreiro.vida == vida_inicial + 30, f"Esperado: {vida_inicial + 30}, Obtido: {guerreiro.vida}"  # Verifica se a vida do guerreiro aumentou corretamente após usar a poção de cura




def test_cura_nao_excede_vida_maxima():
    guerreiro = Guerreiro("Conan")
    pocao = Pocao_Cura(cura=200) # Cura maior que a vida maxima do guerreiro

    vida_inicial = guerreiro.vida
    pocao.usar(guerreiro)
    
    assert guerreiro.vida > vida_inicial, f"Esperado: vida do guerreiro aumentada, Obtido: {guerreiro.vida}"  # Verifica se a vida do guerreiro aumentou após usar a poção de cura

    assert guerreiro.vida == guerreiro.vida_maxima, f"Esperado: {guerreiro.vida_maxima}, Obtido: {guerreiro.vida}"  # Verifica se a vida do guerreiro não excedeu a vida máxima após usar a poção de cura