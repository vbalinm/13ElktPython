import random
lista =[]
def veletlen():
    hossz = 20
    for item in range(hossz):
        lista.append(random.randint(1,50))
    
    return lista

def kiirVeletlen():
    for i in range(20):
        print(veletlen()[i])

def kiir():
    for item in lista:
        print(item)

def osszeAd():
    sum = 0
    for item in veletlen():
        sum = sum + item
    return sum

def legnagyobbElem():
    max = 0

    for item in lista:
        if item > max:
            max = item

    return max        

veletlen()
kiir()
print()
print(f"A lista elemeinek az összege: {osszeAd()}")
print(f"A lista elemeinek a legnagyobb értéke: {legnagyobbElem()}")
#kiirVeletlen()