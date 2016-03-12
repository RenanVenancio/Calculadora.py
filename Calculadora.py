print "Este programa es una CALCULADORA"
Nombre = raw_input("por favor Ingrese Nombre de Usuario: ")
print Nombre + str(" :a continuacion se le muestran las operaciones que puede realizar por favor elija el numero que corresponde a la operacion que desee: ")
print "1 Suma"
print "2 Resta"
print "3 Multiplicacion"
print "4 Division"
print "5 Potencia"
Numero = input ("ingrese el numero de su operacion:")
if Numero == 1:
	print "Usted a selecionado la operacion Suma" 
elif Numero == 2:
	print "Usted a selecionado la operacion Resta"
elif Numero == 3:
	print "Usted a selecionado la operacion Multiplicacion"
elif Numero == 4:
	print "Usted a selecionado la operacion Division"
elif Numero == 5:
	print "Usted a selecionado la operacion Potencia"
else:
	print "Numero erronero"
if Numero == 1:
	def suma():
		A = input ("Ingrese valor de A: ")
		B = input ("ingrese valor de B: ")
		print A + B
	suma()
if Numero == 2:
	def resta():
		A = input ("ingrese valor de A: ")
		B = input ("ingrese valor de B: ")
		print A - B
	resta()
if Numero == 3:
	def multiplicacion():
		A = input ("ingrese valor de A: ")
		B = input ("ingrese valor de B: ")
		print A * B
	multiplicacion()
if Numero == 4:
	def division():
		A = input ("ingrese valor de A: ")
		B = input ("ingrese valor de B: ")
		print A / B
	division()
if Numero == 5:
	def potencia():
		A = input ("ingrese valor de A: ")
		print A * A
	potencia()
print "Gracias por utilizar este Programa tan dificil que me llevo dos horas en Resolverlo"