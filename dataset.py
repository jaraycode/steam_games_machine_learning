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
        
        for element in entrada:
            if isinstance(element, float):
                if math.isnan(element):
                    continue
                else:
                    salida.append(element)
            else:
                salida.append(element)

        return salida


prueba = extraerJSON("Dataset/steam_games.json", "r")

resultado = prueba.extraer("utf-8")

for a in resultado:
        print(a['developer'], type(a['developer']))