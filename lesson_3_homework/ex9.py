"""Eliminați semnele de punctuație
Scrieți un program care primește o propoziție ca intrare (din consola) și
 elimină toate caracterele de punctuație (de exemplu, .,?!) din ea."""

def elimina_punctuatia(propozitie):
    semne_punctuatie = [".", ",", "?", "!"]
    for semn in semne_punctuatie:
        propozitie = propozitie.replace(semn, "")
    return propozitie

propozitie = input("Introduceți propoziția: ")

propozitie_modificata = elimina_punctuatia(propozitie)
print("Propoziția fără punctuație:", propozitie_modificata)



