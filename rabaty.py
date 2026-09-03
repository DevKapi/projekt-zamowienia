PROGI = [(1000, 0.10), (500, 0.05), (100, 0.02)]


def oblicz_rabat(kwota):
    for prog, rabat in PROGI:
        if kwota > prog:
            return rabat
    return 0.0


def cena_po_rabacie(kwota):
    return round(kwota * (1 - oblicz_rabat(kwota)), 2)
