#!/usr/bin/python3

import random
import time

print("Witamy w kolejnym losowaniu totolotka. Za moment maszyna wylosuje sześć kul.")
print("Twoim zadaniem jest trafienie jak najwięcej liczb.\n")

progress_bar = ""
hash = "◯ "

print("Losuję kule...")

for x in range(6):
    progress_bar += hash
    print(f'{progress_bar}\r', end="")
    time.sleep(1)
print()

liczby = random.sample(range(1, 61), 6) # Komputer losuje 6 liczb z przedziału 1-60
liczby_disp = ' '.join(map(str, liczby))

first_num = int(input("Podaj pierwszą liczbę: "))
sec_num = int(input("Podaj drugą liczbę: "))
third_num = int(input("Podaj trzecią liczbę: "))
fourth_num = int(input("Podaj czwartą liczbę: "))
fifth_num = int(input("Podaj piątą liczbę: "))
sixth_num = int(input("Podaj szóstą liczbę: "))

my_list = [first_num, sec_num, third_num, fourth_num, fifth_num, sixth_num] # Nowa lista z wyborami gracza
odgadniete_liczby = [] # Pusta tablica, w której znajdą się odgadnięte liczby

for i in my_list:
    if i in liczby:
        odgadniete_liczby.append(i) # Jeżeli dana liczba znajduje się w tablicy wylosowanej przez komputer, ma ją dodać do listy odgadniete_liczby

if len(odgadniete_liczby) == 0:
    print("Nie udało Ci się odgadnąć żadnej liczby.")
    print("Wylosowane liczby to:", liczby_disp)
    exit()

wynik = ' '.join(map(str, odgadniete_liczby)) # Konwertujemy tablicę na tekst, w którym każda trafiona liczba jest oddzielona spacją
print("Wylosowano następujące liczby:", liczby_disp)
print("Tyle liczb trafiłeś:", len(odgadniete_liczby), "To:", wynik, end=" ")
print()