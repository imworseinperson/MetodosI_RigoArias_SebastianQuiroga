import numpy as np
import matplotlib.pyplot as plt

class Mineral:
    def __init__(self, nombre: str, dureza: str, lustre: str, 
                 rompimiento_por_fractura: bool, color: str, 
                 composicion: str, sistema_cristalino: str, 
                 specific_gravity: float) -> None:
        
        self.comp = composicion
        self.spgra = specific_gravity
        self.name = nombre
        self.dur = dureza
        self.romp = rompimiento_por_fractura
        self.system = sistema_cristalino
        self.col = color

        pass

    def silicato(self)->bool:
        return ("Si" in self.comp) and ("O" in self.comp)
    
    def densidad(self)->float:
        return(self.spgra*1000)
    
    def colorcomun(minerales: np.array)->None:
        dic = {}
        keys = []
        for i in range(len(minerales)):
            if minerales[i].col not in keys:
                dic[minerales[i].col] = 1
            else:
                dic[minerales[i].col] += 1
            keys = list(dic.keys())
        values = list(dic.values())
        plt.pie(values, labels=keys, colors=keys)
        plt.show()
        pass

    def dro(self)->None:
        
        if self.romp:
            rtn = ("La dureza del mineral " + self.name + " es de " + self.dur + 
                   " en la escala de Mohs, se rompe por fractura y su sistema de organización de átomos es " + 
                   self.system + ".")
        else:
            rtn = ("La dureza del mineral " + self.name + " es de " + self.dur + 
                   self.system + ".")
            
        print(rtn)

        pass