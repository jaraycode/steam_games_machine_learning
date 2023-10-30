import pandas as pd
import numpy as np
from ast import literal_eval # Nos ayudará a evaluar la información desorganizada en los archivos user_reviews y users_items
import json

# Empezamos obteniendo los datos de los archivos .json
# Para mayor facilidad cada dataframe tendrá un nombre significativo por el archivo
# Respectivamente: games, reviews, u_items

json1 = "Dataset/user_reviews.json"
json2 = "Dataset/users_items.json"
json3 = "Dataset/steam_games.json"

# Teniendo en consideración que steam_games cumple con el formato
games = pd.read_json(json3, lines=True) # Ya tenemos nuestro set extraido del archivo original para poder trabajar con él

# Los otros dos tienen errores con su formato, entonces hacemos lo siguiente
with open(json1, "r", encoding="utf-8") as file1:
    rows = [literal_eval(row) for row in file1.readlines()]

reviews = pd.DataFrame(rows)

with open(json2, "r", encoding="utf-8") as file1:
    rows = [literal_eval(row) for row in file1.readlines()]

u_items = pd.DataFrame(rows)

# Ahora podemos observarlos
print(games)
print(reviews)
print(u_items)


# Limpieza de los datos
# Iniciamos con librarnos de la informacion faltante de games
games = games.dropna()

