
#importar los archivos de otras paginas

from game_data import data

from art import logo

from random import random

print(logo)

def format_data(cuenta):

# hacer que los datos que cojamos se vean en la pantalla.

  nombre_cuenta = cuenta["name"]
  descripcion_cuenta = cuenta["description"]
  pais_cuenta = cuenta["country"]
  return(f"{nombre_cuenta}, a {descripcion_cuenta}, de {pais_cuenta} ")

# Que se cojan nombres de manera random.
cuenta_a = random.randint(data)
cuenta_b = random.randint(data)
if cuenta_a == cuenta_b:
  cuenta_b = random.choice(data)

print(f"Compara A: {format_data (account_a )} ")
print(f"Compara B: {format_data (account_a )} ")


# Preguntar al usuario por su opción.

# Checkear que el usuario tiene razon.
# Conseguir el numero de followers de cada cuenta.
# Usar el comando if para ver si el usuario tiene razon. 

# Dar feedback al usuario de su eleción.

# Mantener el score.

# Hacer que el juego se repita.

# Hacer que la cuenta en la posición B sea la nueva guess. 
