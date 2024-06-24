from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class PCB:
    PID: Optional[int] = field(default=None)
    Dir: Optional[int] = field(default=None)
    Tipo: Optional[int] = field(default=None)
    x: Optional[int] = field(default=None)
    y: Optional[int] = field(default=None)
    Ancho: Optional[int] = field(default=None)
    Alto: Optional[int] = field(default=None)
    Color: Optional[int] = field(default=None)
    Hora: Optional[int] = field(default=None)
    Retardo: Optional[int] = field(default=None)

class cola:
    def __init__(self):
        self.len = 0
        end = 0
        self.lista = []
        
    def meter(self, elemento):
        self.lista.append(elemento)
        self.len += 1
        
    def sacar(self):
        return self.lista.pop(0)
        self.len -= 1

    def longitud(self):
        return self.len