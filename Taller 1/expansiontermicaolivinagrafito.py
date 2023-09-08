import expansiontermicamineral as etm

grafito = etm.ExpansionTermicaMineral('Taller 1\graphite_mceligot_2016.csv')
grafito = grafito.coeficiente()
grafito[0].savefig('Taller 1\grafito.pdf')

olivina = etm.ExpansionTermicaMineral('Taller 1\olivine_angel_2017.csv')
olivina = olivina.coeficiente()
olivina[0].savefig('Taller 1\olivina.pdf')

print("Los coeficientes de expansión térmica α del olivina y del grafito son respectivamente: " + 
      str(grafito[1]) + " y " + str(olivina[1]))