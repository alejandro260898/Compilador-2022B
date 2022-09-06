from Compilador.Lexema import Lexema


class Pila:
    def __init__(self):
        self.items = []
        
    def top(self) -> Lexema:
        return self.items[len(self.items) - 1]
    
    def push(self, item:Lexema):
        self.items.append(item)
        return item
    
    def pop(self) -> Lexema:
        return self.items.pop()
    
    def isEmpty(self) -> bool:
        return self.items == []
    
    def empty(self) -> None:
        self.items.clear()
    
    def showYourself(self) -> list:
        return self.items