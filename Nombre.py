def main():


    nombre = str(input("Ingresa tu nombre:"))
    apellidos = str(input("Ingresa primer apellido:"))
    apellido = str(input("Ingresa segundo apelledio:"))
    print("Tu nombre es:", nombre, "El el apellido es: ", apellidos[:2], "El apellido:", apellido[:2])

if __name__ == '__main__':
    main()