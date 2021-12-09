def main():

   numeros = [ i+1 for i in range(30) if i%2 != 0 ]
   print(numeros)

if __name__ == '__main__':
    main()