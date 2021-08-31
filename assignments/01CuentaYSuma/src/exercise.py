def main():
    #escribe tu código abajo de esta línea
    
    c = 0   # Contador
    s = 0   # Acumulador

    while (s < 1000):
        n = int(input("Dame un número:"))

        s = s + n
        c = c + 1

    print(f'suma={s}')
    print(f'cantidad de números={c}')
    
if __name__=='__main__':
    main()
