
texto1="hola"
texto2="mundo"

textoFiuna1=texto1+""+texto2
print (textoFiuna1)


print ("El saludo es: %s %s" %(texto1,texto2))

saludoFinal2="Saludo: {x} {y}" .format(x=texto1,y=texto2)
print(saludoFinal2)


texto= "Desarrollo web profecional UTL"

print(texto)
print(texto.upper())
print(texto.lower())
print(texto.title())
print(texto.find())
print(texto.count("e"))

print(texto.replace("UTL","UTEC"))

cadenasSeparadas=texto.split(" ")
print(cadenasSeparadas)
