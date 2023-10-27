import json
import math
      
class extraerJSON:
    
    def __init__(self, dir, modo):
        self.dir=dir
        self.modo=modo
    
    def extraer(self, enco) -> []:
        salida = []
        with open(self.dir, self.modo, encoding=enco) as f:
            for line in f:
                salida.append(json.loads(line))
        return salida
    
    def limpiar(self, entrada:[]) -> []:
        salida = []
        index = 0
        isgood = True
        # Mantener estructura de diccionario pero verificando que los datos estén limpios
        for element in entrada:
            for value in element.values():
                if isinstance(value, float):
                    if math.isnan(value):
                        isgood = False
            if isgood:
                salida.append(entrada[index])
                index+=1
            else:
                isgood = True
                index+=1

        return salida

prueba = extraerJSON("Dataset/steam_games.json", "r")
my = {}
resultado = prueba.extraer("utf-8")
resultado = prueba.limpiar(resultado)
for a in resultado:
        print(a['developer'], type(a['developer']))