def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

while True:
    print("Opciones:")
    print("Escribe 'suma' para sumar")
    print("Escribe 'resta' para restar")
    print("Escribe 'multiplicacion' para multiplicar")
    print("Escribe 'division' para dividir")
    print("Escribe 'salir' para terminar el programa")

    opcion = input(": ")

    if opcion == "salir":
        break

    if opcion in ("suma", "resta", "multiplicacion", "division"):
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if opcion == "suma":
            print("El resultado es:", suma(num1, num2))
        elif opcion == "resta":
            print("El resultado es:", resta(num1, num2))
        elif opcion == "multiplicacion":
            print("El resultado es:", multiplicacion(num1, num2))
        elif opcion == "division":
            print("El resultado es:", division(num1, num2))
    else:
        print("Opción no válida")
