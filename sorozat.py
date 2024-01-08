from random import randint


def veletlen(szam1: int, szam2: int):
    print("II/a.")
    print("\t", end="")
    lista = []
    if szam1 < szam2:
        kisebb = szam1
        nagyobb = szam2
    else:
        kisebb = szam2
        nagyobb = szam1
    for i in range(1, 15, 1):
        velszam = randint(szam1, szam2)
        lista.append(velszam)
    velszam = randint(szam1, szam2)
    lista.append(velszam)
    for index in range(0, len(lista)):
        print(lista[index], end="%")
    return lista


def legkisebb(lista):
    kiFajl = open("fajlok/legkisebb.txt", "w", encoding="utf-8")
    print("\nII/b.")
    print("\tA legkisebb elem:", end="")
    print("\tA legkisebb elem:", end="", file=kiFajl)
    minErtek = lista[0]
    for index in range(1, len(lista)):
        if lista[index] < minErtek:
            minErtek = lista[index]
    print(f" {str(minErtek)}.")
    print(f" {str(minErtek)}.", file=kiFajl)
