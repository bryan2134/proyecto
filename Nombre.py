def main():


    nombre = str(input("Ingresa tu nombre:"))
    apellidos = str(input("Ingresa primer apellido:"))
    apellido = str(input("Ingresa segundo apelledio:"))
    print("Tu nombre es:", nombre + apellidos[:2] + apellido[:2])

if __name__ == '__main__':
    main()