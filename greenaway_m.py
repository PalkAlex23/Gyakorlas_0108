import greenaway_o


def beolvas():
    lista = []
    beFajl = open("fajlok/greenaway.txt", "r", encoding="utf-8")
    beFajl.readline()
    sorok = beFajl.readlines()
    for index in range(0, len(sorok), 1):
        tisztitottSor = sorok[index].strip()
        daraboltSor = tisztitottSor.split("-")
        konyvem = greenaway_o.Film(daraboltSor[0], daraboltSor[1])
        lista.append(konyvem)
    return lista


def kiir(lista):
    for index in range(0, len(lista), 1):
        print(lista[index])


def filmekszama(lista: list):
    print("III/b.")
    print(f"\tA filmek száma: {len(lista)}")


def d(lista: list):
    print("III/d.")
    talalat = True
    index = 0
    while index < len(lista) or talalat:
        if "szakács" in lista[index].cim.lower():
            talalat = False
        index += 1

    if not talalat:
        print(f'\tVan olyan film, amiben szerepel a "szakács" szó.')
    else:
        print(f'\tNincs olyan film, amiben szerepel a "szakács" szó.')
