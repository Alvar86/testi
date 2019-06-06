luku = int(input("Anna luku:\n"))

if luku > 0:
    print ("Luku on positiivinen")
    if luku > 10:
        print ("Luku on suurempi kuin 10")
elif luku < 0:
    print ("Luku on negatiivinen")
    if luku < -10:
        print ("Luku on pienempi kuin -10")
else:
    print ("luku 0 ei ole positiivinen eikä negatiivinen")
print ("Ohjelman suoritus päättyy")