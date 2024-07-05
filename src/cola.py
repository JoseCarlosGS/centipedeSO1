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
    Salud: Optional[int] = field(default=2)

class cola:
    def __init__(self):
        self.lista = []
        
    def meter(self, elemento):
        self.lista.append(elemento)
        
    def sacar(self):
        if len(self.lista) > 0:
            return self.lista.pop(0)
        else:
            return None
  
    def first(self):
        return self.lista[0]
    
    def __iter__(self):
        self._indice = 0  # Reiniciar el índice al comienzo de la iteración
        return self
    
    def __next__(self):
        if self._indice < len(self.lista):
            resultado = self.lista[self._indice]
            self._indice += 1
            return resultado
        else:
            raise StopIteration