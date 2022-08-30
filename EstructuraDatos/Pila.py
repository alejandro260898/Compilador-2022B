class Pila:
    def __init__(self):
        self.items = []
        
    def top(self):
        return self.items[len(self.items) - 1]
    
    def push(self, item):
        self.items.append(item)
        return item
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def empty(self):
        return self.items.clear()
    
    def showYourself(self):
        return self.items