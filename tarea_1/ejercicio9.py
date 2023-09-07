fecha = input ("ingresa tu fecha de nacimiento en el siguiente orden dd/mm/aaaa \nteniendo en cuenta que las dd corresponden al dia, las mm al mes y las aaaa al año \ntambien puede ingresar un solo caracter\n")
dia = fecha [1:]
mes = fecha [3:5]
año = fecha [6:]

dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]

print ( "Dia", dia)
print ( "Mes", mes)
print ("Año" , año)

