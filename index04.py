# El manejo de excepciones habla del control que se le da al error es decir que podemos mantener
# el control bajo un error dentro de los manejos de excepciones esta el try, except y el finally


# Imaginemos que el try, except y el finally son condicionales if, elif, else en el cual pueden
# ejecutar un mensaje 

# Su sintaxis es lo siguiente:

print("vamos a ver como son los errores bajo control")

try:
    
    NumeroDecimal = 10.6
    
    NumeroEntero = int(NumeroDecimal)
    
    print("El valor del numero decimal es ahora: ", NumeroEntero)
    
except ValueError:
    
    print("Error encontrado")
    
    
    # Otro ejemplo mas sencillo ahora usando el try except y finally
    
    # El usuario tiene que ingresar un numero decimal para convertirlo en numero entero
    
try:
    
    IngresarTexto = float(input("Ingrese el numero decimal: "))
    
    TextoIngresado = int(IngresarTexto)
    
    print("La conversion del numero es: ", TextoIngresado)
    
except:
        
    print("Error malisimo")
    
finally:
    
    print("El programa acabo por favor intente mas tarde")
    
    
    # El finally es opcional, es decir, que podemos colocar ya sea que el programa tenga un error
    # el finally quiere decir esto: Python hagas lo que hagas debes ejecutar el codigo por favor