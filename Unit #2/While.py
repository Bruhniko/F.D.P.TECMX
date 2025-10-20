# Muestra el menú principal
def MostrarMenu() -> None:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1) Saludar")
    print("2) Calcular la suma de dos números")
    print("3) Mostrar la tabla de multiplicar del 5")
    print("0) Salir")


# Solicita el nombre de usuario
def OpcionSaludar() -> None:
    Nombre = input("¿Cómo te llamas? ").strip()
    print(f"¡Hola, {Nombre}! Bienvenido/a.")


# Pide dos números, los suma y muestra el resultado
def OpcionSuma() -> None:
    try:
        NumeroA = float(input("Primer número: "))
        NumeroB = float(input("Segundo número: "))
        print(f"La suma es: {NumeroA + NumeroB}")
    except ValueError:
        print(" Debes introducir valores numéricos.")
# Marca error 

# Muestra la tabla de multiplicar del 5
def OpcionTabla() -> None:
    Numero = 5
    print(f"\nTabla del {Numero}:")
    for i in range(1, 11):
        print(f"{Numero} × {i} = {Numero * i}")


# ---------- Bucle principal del programa ----------
Continuar = True  # Controla si el programa sigue ejecutándose

while Continuar:
    MostrarMenu()  # Muestra el menú en pantalla
    Eleccion = input("Elige una opción: ").strip()

    if Eleccion == "1":
        OpcionSaludar()
    elif Eleccion == "2":
        OpcionSuma()
    elif Eleccion == "3":
        OpcionTabla()
    elif Eleccion == "0":
        print("\n ¡Hasta luego!")
        Continuar = False 
        # Finaliza el programa 
    else:
        print(" Opción no válida, intenta de nuevo.")
# Reinica el programa 
print("Programa terminado.")
