def waliduj_email(email):
    if "@" not in email:
        return False
    if "." not in email.split("@")[-1]:
        return False
    return True


def waliduj_ilosc(ilosc):
    return isinstance(ilosc, int) and ilosc > 0


def waliduj_zamowienie(zamowienie):
    bledy = []
    if not waliduj_email(zamowienie.get("email", "")):
        bledy.append("niepoprawny email")
    if not waliduj_ilosc(zamowienie.get("ilosc", 0)):
        bledy.append("niepoprawna ilosc")
    return bledy
