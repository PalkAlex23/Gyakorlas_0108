def leghosszabb():
    szo = input("\tKérem adjon meg egy szót: ")
    szo2 = input("\tKérem adjon meg egy másik szót: ")
    print("I/a.")
    if len(szo2) > len(szo):
        print(f"\tA hosszabb szó: {szo2}.")
    elif len(szo) == len(szo2):
        print("\tEgyenlő hosszúak.")
    else:
        print(f"\tA hosszabb szó: {szo}.")
    kulonbseg = abs(len(szo) - len(szo2))
    print("I/d.")
    print(f"\tA szavak hosszának a különbsége: {kulonbseg}")
