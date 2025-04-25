# Cuando hablamos de bucles o mejor conocido como loops existen muchos tipos de bucles
# por ejemplo en java script estan los bucles for, while, do while, for in y for of
# y con respectivos metodos que forman parte de los bucles aunque se pueden ejecutar 
# en otros temas como por ejemplo los arrays o mejor conocido como las listas

# en python los arrays son asi

a = ["hola mundo", 1, 2, 3, 4, 5] # etc etc

# en java script por ejemplo los arrays son asi

# let lista = [1, 2, 3, 4, 5];

# console.log(lista) # 1, 2, 3, 4, 5 

# en python existe nada mas y nada menos que el bucle for y el bucle while

# el bucle for es para saber cuando iteraciones (repeticiones) se va a saber
# de antemano

#ejemplo:

for i in range(5):
    
    print(i) # este bucle llega hasta el 4 porque por defecto esta en el 0
    
# dentro del bucle podemos crear una variable sin la necesidad de hacer esto

x = "hola mundo"

for x in range(5):
    
    print(x) # aqui es donde esta malo es decir que en este ejemplo podemos ver
    
    
# como intentamos que "hola mundo" se repita 5 veces y da otro resultado es mejor
# hacer el bucle y crear la variable dentro del bucle como en la linea 23 hasta
# el 25

# ahora el bucle while es cuando se sabe que se va a ejecutar el bucle cuando
# no hay ningun error. Ejemplo:

contador = 0

while contador < 0:
    
    print("el contador es: {contador}")
    
    contador = contador + 2
    
    print("terminamos")
    
    # Nota: En resumen el tema hablo de los bucles y sus tipos en python y
    # muchos otros lenguajes de programacion como java script, ruby, php, C++ ...
    
    # Si pueden pensarlo pueden programarlo!