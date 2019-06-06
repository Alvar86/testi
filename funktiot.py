
def tulosta(nimi_funktiossa, kertaa):
    for i in range(kertaa): 
        print ("terve", nimi_funktiossa)
    print ("Tassa tervehdykset")

def main():
    nimi = input ("Kerro nimesi:\n")
    lkm = int(input("Kuinka monta kertaa haluat sinua tervehdittavan?\n"))
                    

    tulosta(nimi, lkm)
    
    print ("main-funktio suoritettu")
    
main()