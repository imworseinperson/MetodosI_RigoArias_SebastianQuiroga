import numpy as np
import mineral as mn

def crear(minerales:str)->np.ndarray:
    data = open(minerales, encoding="utf-8")
    linea = data.readline()
    linea = data.readline().strip("\n")
    arreglo_minerales = np.array([])
    while linea != "":
        miner = linea.split('\t')
        miner2 = mn.Mineral(miner[0], miner[1], miner[5], bool(miner[2]), 
                            miner[3], miner[4], miner[7], float(miner[6]))
        arreglo_minerales = np.append(arreglo_minerales, miner2)
        linea = data.readline().strip("\n")
    data.close()

    return arreglo_minerales

arr = crear("Taller 1\minerales.txt")
mn.Mineral.colorcomun(arr)