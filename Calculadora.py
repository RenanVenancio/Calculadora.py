def final():
	print " "
	print "                            ----------------------------------"
	print "                            GRACIAS POR UTILIZAR ESTE PROGRAMA"
	print "                            ----------------------------------"

def suma():
	A = input ("Por favor ingrese su primer valor: ")
	B = input ("Por favor ingrese su segundo valor: ")
	print "Sus valores suman la cantidad de: " + str(A + B)
	final()
def resta():
	A = input ("ingrese valor de A: ")
	B = input ("ingrese valor de B: ")
	print A - B
	final()
def multiplicacion():
	A = input ("ingrese valor de A: ")
	B = input ("ingrese valor de B: ")
	print A * B
	final()
def division():
	A = input ("ingrese valor de A: ")
	B = input ("ingrese valor de B: ")
	print A / B
	final()
def potencia():
	A = input ("ingrese valor de A: ")
	print A * A
	final()

def usuario():
	print "                                  ==============="
	print "                                  ---------------"
	print "                                    CALCULADORA  "
	print "                                  ---------------"
	print "                                  ==============="
	print "*******************************************************"
	Nombre = raw_input("por favor Ingrese Nombre de Usuario: ")
	print "*******************************************************"
	menu(Nombre)

def menu(usuario):
	print "INSTRUCCIONES :"
	print usuario + " :a continuacion se le muestran las operaciones que puede realizar por favor"
	print ("                 elija el numero que corresponde a la operacion que desee: ")
	print "1 Suma"
	print "2 Resta"
	print "3 Multiplicacion"
	print "4 Division"
	print "5 Potencia"
	print ""
	Numero = raw_input ("ingrese el numero de su operacion:")
	print ""


	if Numero.isalpha() == True:
		print "No puede ingresar letras intente nuevamente :)"
		menu(usuario)
	else:
		if Numero == "1":
			print "-------------------------------------"
			print "Usted a selecionado la operacion Suma" 
			print "-------------------------------------"
			suma()
		if Numero == "2":
			print "-------------------------------------"
			print "Usted a selecionado la operacion Resta"
			print "-------------------------------------"
			resta()
		if Numero == "3":
			print "-----------------------------------------------"
			print "Usted a selecionado la operacion Multiplicacion"
			print "-----------------------------------------------"
			multiplicacion()
		if Numero == "4":
			print "-----------------------------------------"
			print "Usted a selecionado la operacion Division"
			print "-----------------------------------------"
			division()
		if Numero == "5":
			print "-----------------------------------------"
			print "Usted a selecionado la operacion Potencia"
			print "-----------------------------------------"
			potencia()
		if Numero.isalpha() == True:
			print "Detenido"

usuario()