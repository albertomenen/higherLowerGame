
#importar los archivos de otras paginas

from game_data import data

from art import logo,vs

import random 

from replit import clear

score = 0
cuenta_b = random.choice(data)

print(logo)

# hacer que los datos que cojamos se vean en la pantalla.
def format_data(cuenta):
  
  nombre_cuenta = cuenta["name"]
  descripcion_cuenta = cuenta["description"]
  pais_cuenta = cuenta["country"]
  return(f"{nombre_cuenta}, a {descripcion_cuenta}, de {pais_cuenta} ")

# Checkear que el usuario tiene razon.

def check_answer(guess, seguidores_a, seguidores_b):
  if seguidores_a > seguidores_b:
    if guess == "a":
      return True
    else:
      return False

# Hacer que el juego se repita 

repite_juego = True

while repite_juego:


 
  
  # Que se cojan nombres de manera random.
  cuenta_a = cuenta_b
  cuenta_b = random.choice(data)
  if cuenta_a == cuenta_b:
    cuenta_b = random.choice(data)
  
  print(f"Compara A: {format_data (cuenta_a)} ")
  print(vs)
  print(f"Contra B: {format_data (cuenta_b)}")
  
  
  # Preguntar al usuario por su opción.
  
  guess = input("Quien tiene mas seguidores Teclea A o B").lower()
  
  
  # Conseguir el numero de followers de cada cuenta.
  
  def seguidores(cuenta):
    seguidores_cuenta = cuenta["follower_count"]
    return (f"{seguidores_cuenta} ")
  
  
  
  seguidores_a = seguidores(cuenta_a)
  seguidores_b = seguidores(cuenta_b)
  
  es_correcto = check_answer(guess, seguidores_a, seguidores_b)

  clear()
  
  # Dar feedback al usuario de su eleción.
  
  if es_correcto:
    score += 1
    print(f"Ganaste! Tienes {score} puntos acumulados")
  else:
    repite_juego = False
    print(f"Nop, fallaste! Tu puntuación final es {score} ")
  
  # Mantener el score.
  
  
