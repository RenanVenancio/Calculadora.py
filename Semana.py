import os
import sys 
import time

print "A continuacion se le presenta unsa serie de programas por favor complete lo que se le pide"
print ""
Nombre = raw_input("Por favor ingrese un nombre de Usuario: ")
print ""
def menusemana():
	print "                        ***********"
	print"                        * SEMANA  *"
	print "                        ***********"
	print ""
	print "INSTRUCIONES:"
	print Nombre +  " a continuacion se le presentan numeros que corresponde a los dias de la semana porfavor"
	print ("   ingrese un numero del 1-7 y se le mostrara que dia corresponde a ese numero ")
menusemana()
print "  "
def numero():
	print "-----"
	print "- 1 -"
	print "- 2 -"
	print "- 3 -"
	print "- 4 -"
	print "- 5 -"
	print "- 6 -"
	print "- 7 -"
	print "-----"
numero ()
print ""


def semana():
	Seleccion = raw_input("por favor ingrese el numero deseado: ")
	print ""
	if Seleccion.isalpha() == True:
		print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
		print "disculpe las molestias no puede ingresar letras intentelo nuevamente"
		print "--------------------------------------------------------------------"
		numero()
		semana()
	else:
		if Seleccion == "1":
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "usted a seleccionado el dia DOMINGO"
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		elif Seleccion == "2":
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "usted a seleccionado el dia LUNES"
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		elif Seleccion == "3":
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print " usted a seleccionado el dia MARTES"
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		elif Seleccion == "4":
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "usted a seleccionado el dia MIERCOLES"
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		elif Seleccion == "5":
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "usted a seleccionado el dia JUEVES"
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		elif Seleccion == "6":
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "usted a seleccionado el dia VIERNES"
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		elif Seleccion == "7":
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "usted a seleccionado el dia SABADO"
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
semana()
print ""
print ""
print "                                       /////////////////////"
print "                                  A completado el programa semana "
print "                                       /////////////////////"
print ""
print ""
print ""
print "                                       ECUACION"
print"                              _____________________________"

def ecua():
 	print "INSTRUCCIONES:"
 	print Nombre + ": operaremos una ecuacion"
ecua()
print "6 * L /2"
L = input ("ingrese valor de L: ")
M = 6 * L / 2 
print ("Su resultado es: ") + str (M)
print "                                       /////////////////////"
print "                                A completado el programa Ecuacion "
print "                                       /////////////////////"
print ""
print""
print""
print "                                            PERSONAL"
print "                                      _____________________"
print "INSTRUCCIONES:"
print Nombre + " complete las preguntas:"
print" "
def datos():
	Completo = raw_input("Ingrese nombre completo: ")
	nacimiento = input ("Ingrese fecha de nacimiento : ")
	anio = input ("ingrese anio actual: ")
	Edad = anio - nacimiento
	print ("su edad es de: " ) + str (Edad)
	estado = raw_input ("ingrese su estado Civil: ")
	direccion = raw_input ("Ingrese su residencia: ")
datos()
print "a completado el formulario exitosamente"

print"                                              TIEMPO"
print "INSTRUCCIONES"\
print Nombre + " observe lo que se muestra:" 
print 
print "HOLA COMO STAS"
