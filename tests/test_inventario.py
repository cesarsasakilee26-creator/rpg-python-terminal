import pytest
from src.models.inventario import Inventario
from src.models.item import Arma

def test_adicionar_item_inventario():
    inventario = Inventario()

    espada = Arma("Espada Longa", "Espada", "Descrição...", 100, 5.0, 10)

    inventario.adicionar_item(espada)

    assert inventario.tem_item(espada), f"Esperado: {espada} estar no inventario, mas não está."
    assert inventario.quantidade_itens == 1, f"Esperado: 1 item no inventario, mas há {inventario.quantidade_itens}."


def test_remover_item_inventario():
    inventario = Inventario()

    espada = Arma("Espada Longa", "Espada", "Descrição...", 100, 5.0, 10)
    inventario.adicionar_item(espada)
    inventario.remover_item(espada)

    assert not inventario.tem_item(espada), f"Esperado: {espada} não estar no inventario, mas ainda está."