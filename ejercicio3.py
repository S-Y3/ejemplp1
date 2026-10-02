print("   Universidad Catolica De Oriente")
print("Facultad de Ingenieria")
archivo = open("saludo.py", "r+")
nom=input("Ingrese su nombre: ")
nota=input("Ingrese su nota: ")
for linea in archivo.readlines():
    print(linea)

archivo = open("saludo.py", "r+")
contenido = archivo.read()
final_de_archivo = archivo.tell()

archivo.write(nom + " " + nota + " ")
archivo.write("\n")


archivo.seek(final_de_archivo)
nuevo_contenido = archivo.read()

print (nuevo_contenido)
archivo.close()
