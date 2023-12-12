print ("Ingresa tu salario actual: ")
salario = int(input())

if salario < 15000:
    incremento_quince = salario * 1.15
    print ("Tu salario final con incremento para el próximo año es de " , incremento_quince)
else:
    incremento_veinte = salario * 1.20
    print ("Tu salario final con incremento para el próximo año es de " , incremento_veinte)
