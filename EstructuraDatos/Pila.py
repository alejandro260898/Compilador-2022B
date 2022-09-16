from Compilador.Nodo import Nodo

class Pila:
    def __init__(self):
        self.items = []
        
    def top(self) -> Nodo:
        return self.items[len(self.items) - 1]
    
    def push(self, item:Nodo):
        self.items.append(item)
        return item
    
    def pop(self) -> Nodo:
        return self.items.pop()
    
    def isEmpty(self) -> bool:
        return self.items == []
    
    def empty(self) -> None:
        self.items.clear()
    
    def showYourself(self) -> list:
        itemsStr = ""
        for item in self.items:
            itemsStr += str(item) if type(item) == int else item.dameSimbolo()
            itemsStr += '|'
        return itemsStr[:-1]