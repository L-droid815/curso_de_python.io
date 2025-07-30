#En python hay algo que se llama operaodores de identidad que son los que detectan cuando
#dos o mas variables apunta hacia el mismo objetivo 

#En Python los operadores de identidad son is y is not

#is devuelve False si dos variables apuntan hacia el mismo objetivo en caso contrario da True

#is not devuelve True si dos variable no apuntan hacia el mismo objetivo en caso contrario
#da False

lista1 = [1, 2, 3]

lista2 = [1, 2, 3]

#Aqui se ejecuta el metodo is en python que en este caso da false

Resultado = lista1 is lista2

print(Resultado)

#Aqui se ejecuta el metodo is not en python que en este caso da true

lista3 = [2, 4, 6]

lista4 = [8, 10, 12]

Resultado2 = lista3 is not lista4

print(Resultado2)