import pytest
from src.models.personagem import Guerreiro
from src.models.item import Arma, Armadura, Pocao_Cura


def test_pocao_de_cura():
    guerreiro = Guerreiro("Conan")
    guerreiro.vida = 30
    pocao = Pocao_Cura(cura=30)
    
    vida_inicial = guerreiro.vida
    pocao.usar(guerreiro)

    assert guerreiro.vida == vida_inicial + 30, f"Esperado: {vida_inicial + 30}, Obtido: {guerreiro.vida}"  # Verifica se a vida do guerreiro aumentou corretamente após usar a poção de cura

def test_pocao_cura_respeita_vida_maxima():
    guerreiro = Guerreiro("Conan")
    pocao = Pocao_Cura(cura=50)
    vida_maxima = guerreiro.vida_maxima

    pocao.usar(guerreiro)

    assert guerreiro.vida == vida_maxima, f"Esperado: {vida_maxima}, Obtido: {guerreiro.vida}"  # Verifica se a vida do guerreiro não excede a vida máxima após usar a poção de cura