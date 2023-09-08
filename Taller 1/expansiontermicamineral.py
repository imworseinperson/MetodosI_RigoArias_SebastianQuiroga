import numpy as np
import pandas as pd
import mineral as mn
import matplotlib.pyplot as plt

class ExpansionTermicaMineral (mn.Mineral):
    def __init__(self, archivo:str) -> None:
        data = pd.read_csv(archivo)
        self.listatem = list(data["celsius_temperature"])
        self.listavol = list(data['volume_cc'])
        pass

    def coeficiente(self):
        h = self.listatem[1]-self.listatem[0]
        listacoef = []
        for i in range(1, len(self.listatem)-1):
            coef = (self.listatem[i+1]-self.listatem[i-1])/(2*h)
            listacoef.append(coef)
        fig,axs = plt.subplots(nrows=1,ncols=2,figsize=(18,4.5))
        axs[0].scatter(self.listatem, self.listavol)
        axs[0].set_ylabel(r'Volumen (cm^3)')
        axs[0].set_xlabel('Temperatura (C)')
        axs[0].set_title('Volumen vs Temperatura')
        axs[1].scatter(self.listatem[1:9], listacoef, color='r')
        axs[1].set_ylabel(r'Coeficiente')
        axs[1].set_xlabel('Temperatura (C)')
        axs[1].set_title('Coeficiente vs Temperatura')
        return fig, np.mean(listacoef)

grafito = ExpansionTermicaMineral('Taller 1\graphite_mceligot_2016.csv')
grafito.coeficiente()