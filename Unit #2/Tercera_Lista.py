#una lista con 5 inputs: Nombre, Escuela, Carrera, Domicilio, Edad
ListaDatos = []
print("Lista de Datos")

dato1 = input("Ingresa tu Nombre: ")
ListaDatos.append(dato1)

dato2 = input("Ingresa tu Edad: ")
ListaDatos.append(dato2)

dato3 = input("Ingresa tu Domicilio: ")
ListaDatos.append(dato3)

dato4 = input("Ingresa el nombre de la escuela: ")
ListaDatos.append(dato4)

dato5 = input("Ingresa a la carrera elegida: ")
ListaDatos.append(dato5)


print("\n📌 Tus datos son:")
for dato in ListaDatos:
    print(f"- {dato}")
print("\n✅ ¡Lista creada con éxito!")