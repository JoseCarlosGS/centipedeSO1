from dataclasses import dataclass

@dataclass
class PCB:
    PID: int
    Dir:int
    Tipo:int
    x: int
    y: int
    Ancho: int
    Alto: int
    Color: int
    Hora: int
    Retardo: int

class cola:
    def __init__(self):
        len = 0
        end = 0
        lista = []
        
    def meter(self, elemento):
        self.lista.append(elemento)
        self.len += 1
        
    def sacar(self):
        return self.lista.pop()
        self.len -= 1

    def longitud(self):
        return self.len