import random
import string

longitud = int(input("ingrese la cantidad de caracteres para la contraseña entre 8 y 16: "))

numero=input("quieres que incluya numeros? Y/N: ")
if numero.lower() == "y":
    numero = True
elif numero.lower() == "n":
    numero = False
else:
    print(F"parametro no valido")

mayusculas = input("¿Quieres que incluya mayusculas? Y/N: ")
if mayusculas.lower() == "y":
    mayusculas = True
elif mayusculas.lower() == "n":
    mayusculas = False
else:
    print(F"parametro no valido")

simbolos = input("¿Quieres que incluya simbolos? Y/N: ")

def generador_contrasenas(longitud,num,may,sim):
    if longitud>=8 and longitud<=16:
        caracteres=[]
        if num:
            caracteres+=list(string.digits) #para almazenar los numeros
        if may:
            caracteres+=list(string.ascii_uppercase) #para almazenar las mayusculas
        if sim:
            caracteres+=list(string.punctuation) #para almazenar los digitos
        password ="".join(random.choices(caracteres,k=longitud))
        return password
    else:
        print(f"Error debes ingresar una cantidad entre 8 y 16.")

password= generador_contrasenas(longitud=longitud,num=numero,may=mayusculas,sim=simbolos)
print(password)


