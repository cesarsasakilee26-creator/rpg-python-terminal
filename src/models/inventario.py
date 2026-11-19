class Inventario:
    def __init__(self):
        self._itens = []

    def adicionar_item(self, item) -> bool:
        if item is None:
            return False

        if item in self._itens:
            return False

        if len(self._itens) >= 20:  
            return False
        
        self._itens.append(item)
        return True

    def remover_item(self, item) -> bool:
        
        if item is None:
            return False
        
        if item not in self._itens:
            return False
        
        self._itens.remove(item)
        return True
    
    def listar_itens(self):
        for item in self._itens:
            print(f"- {item}")
            

