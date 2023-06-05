"""Înlocuiți un subșir de caractere
Scrieți un program care primește o propoziție, un subșir de caractere țintă
și un subșir de caractere de înlocuire ca intrare (din consola)
și înlocuiește toate aparițiile subșirului de caractere țintă cu subșirul de caractere de înlocuire."""


def inlocuieste_subsir(propozitie, sub_sir_tinta, sub_sir_inlocuire):
    propozitie_noua = propozitie.replace(sub_sir_tinta, sub_sir_inlocuire)
    return propozitie_noua

propozitie = input("Introduceți propoziția: ")
sub_sir_tinta = input("Introduceți subșirul țintă: ")
sub_sir_inlocuire = input("Introduceți subșirul de înlocuire: ")

propozitie_modificata = inlocuieste_subsir(propozitie, sub_sir_tinta, sub_sir_inlocuire)
print("Propoziția modificată:", propozitie_modificata)