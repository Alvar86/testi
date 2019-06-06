

def summa(a, b):
    return a + b
def erotus(a, b):
    return a - b
def tulo(a, b):
    return a * b
def main():
    
    #tulos = summa(2, 4)
    luku1 = float(input("Anna luku 1:\n"))
    luku2 = float(input("Anna luku 2:\n"))

    komento = input("Valitse komento: a: summa, b: erotus, c: tulo\n") 

    if komento == "a":
        print (summa(luku1, luku2))
    elif komento == "b":
        print (erotus(luku1, luku2))
    elif komento =="c":
        print (tulo(luku1, luku2))

main()