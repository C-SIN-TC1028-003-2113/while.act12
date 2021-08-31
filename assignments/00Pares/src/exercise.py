def main():
    #escribe tu código abajo de esta línea
    
    a = int(input("Dame el valor de a:"))
    b = int(input("Dame el valor de b:"))

    n = a

    while (n <= b):
        if n % 2 == 0:
            print(n)
        n = n + 1

if __name__=='__main__':
    main()
