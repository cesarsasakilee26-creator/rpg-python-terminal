import pytest
from src.models.personagem import Guerreiro
from src.models.item import Arma, Armadura

def test_atacar_guerreiro():
    guerreiro = Guerreiro("Conan")
    espada = Arma("Espada Longa", "Espada", "Uma espada longa e afiada, perfeita para combates corpo a corpo.", 100, 5.0, 10)
    armadura = Armadura("Armadura de Couro", "Armadura", "Uma armadura leve feita de couro, oferece proteção básica.", 50, 3.0, 5)
    
    dano_base_original = guerreiro.dano_base
    vida_original = guerreiro.vida
    mana_original = guerreiro.mana
    
    armadura.usar(guerreiro)
    espada.usar(guerreiro)
    
    dano_causado = guerreiro.atacar()
    



    
    assert dano_causado == dano_base_original + espada.dano, f"Esperado: {dano_base_original + espada.dano}, Obtido: {dano_causado}" #Espera que o dano seja o dano base + o dano da arma equipada
    
    assert guerreiro.arma_equipada is espada, f"Esperado: {espada}, Obtido: {guerreiro.arma_equipada}" #Verifica se a arma equipada é a espada
    
    assert guerreiro.armadura_equipada is armadura, f"Esperado: {armadura}, Obtido: {guerreiro.armadura_equipada}" #Verifica se a armadura equipada é a armadura de couro
    
    assert guerreiro.vida == vida_original, f"Esperado: {vida_original}, Obtido: {guerreiro.vida}" #Verifica se a vida do guerreiro é equivalente ao atribuido no construtor do personagem
    
    assert guerreiro.mana == mana_original, f"Esperado: {mana_original}, Obtido: {guerreiro.mana}" #Verifica se a mana do guerreiro é equivalente ao atribuido no construtor do personagem


    
def test_receber_dano_nao_cura():
    guerreiro = Guerreiro("Conan")
    armadura = Armadura("Armadura de Ferro", "Armadura", "Uma armadura pesada feita de ferro, oferece excelente proteção.", 100, 10.0, 20)

    armadura.usar(guerreiro)
    vida_inicial = guerreiro.vida

    guerreiro.receber_dano(10)  # Dano menor que a defesa da armadura


    assert guerreiro.vida == vida_inicial, f"Esperado: {vida_inicial}, Obtido: {guerreiro.vida}"  # Verifica se a vida do guerreiro não aumentou após receber dano menor que a defesa da armadura
 
def test_receber_dano_com_armadura():
    guerreiro = Guerreiro("Conan")
    armadura = Armadura("Armadura de Ferro", "Armadura", "Uma armadura pesada feita de ferro, oferece excelente proteção.", 100, 10.0, 20)

    armadura.usar(guerreiro)
    vida_inicial = guerreiro.vida

    guerreiro.receber_dano(30) # Dano maior que a defesa da armadura

    assert guerreiro.vida == vida_inicial - (30 - armadura.defesa), f"Esperado: {vida_inicial - (30 - armadura.defesa)}, Obtido: {guerreiro.vida}"  # Verifica se a vida do guerreiro diminuiu corretamente após receber dano maior que a defesa da armadura


