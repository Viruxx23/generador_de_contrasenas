"""
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
"""
from random import choice
import string

def generador_contraseñas(tamaño=8, mayusculas=False, numeros=False, simbolos=False):
    caracteres = string.ascii_letters
    if tamaño< 8 or tamaño > 16:
        print(f"error el tamaño permitido es de 8-16 caracteres")
        return None
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
        
    # Elegir caracteres aleatorios de la lista de caracteres
    contraseña = "".join((choice(caracteres)) for i in range(tamaño))
    return contraseña

print(generador_contraseñas(15, True, True, True))

