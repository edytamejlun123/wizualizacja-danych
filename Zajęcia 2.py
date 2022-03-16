#  a = 4
#  b = 4
# if a<b:
#    print("b jest wieksze")
# elif a>b:
#    print("a jest wieksze")
# else:
#    print("sa równe")
#
# a = input('wpisz liczbę: ')
# print(a)
# print(type(a))
# a = int(a)
# print(type(a))
#
#
# a = input('wpisz pierwszą liczbę: ')
# b = input('wpisz drugą liczbę: ')
# c = input('wpisz trzecią liczbę: ')
# d = input('wpisz czwartą liczbę: ')
# a = int(a)
# b=int(b)
# c=int(c)
# d=int(d)
# if(a>b)&(c>d):
#     print('liczba a jest wieksza od b i c jest wieksze od d')
# else:
#     print('a jest mniejsze od b lub c jest mniejsze od d')
#
#
# #for licznik in sekwencja:
#     #instrukcja lub blok instrukcji
# #else :
#     #instrukcja po wykonaniu pętli
#
# for i in range(1,7,1):
#     print(i)
#
# lista = ['a', 5,6,5.6]
# for a in lista:
#     print(a)
# else:
#     print('wyświetlone zostały wszystkie elementy z listy')
#
# while warunek:
#     instrukcja lub blok instrukcji, gdy warunek spełniony
# else:
#     instrukcje po pętli
# a=0
# while a<10:
#     a+=1
#     print(a)
# else:
#     print('liczba wieksza od 10')
#
# lista = [4, 6, 9, 5, 7, 2, 3]
# liczba = input('podaj liczbę: ')
# licznik=0
# while licznik<len(lista):
#     if int(liczba) - lista[licznik] == 0:
#         print('liczba ' + str(liczba) + ' - ' + str(lista[licznik]) + ' = 0' )
#         break
#     else:
#         licznik+=1
# else:
#     print('żadna z wartości nie dała odpowiedniego wyniku')
#
# lista1 = [4, 6, 8, 2, 3, 9]
# lista2 = [4, 7, 5, 2]
# suma = []
# for a in lista1:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)
#
# try:
#     instrukcje które mogą zawierać błąd
# except nazwa_błędu1:
#     instrukcja po wykryciu błędu# # except nazwa_błędu2:
#     instrukcje po wykryciu błędu2
# else:
#     wyniki gdy nie ma błędu -> do try
#
# a = input("wczytaj pierwszą liczbę: ")
# b = input("wczytaj drugą liczbę: ")
# try:
#     a = int(a)
#     b = int(b)
#     wynik = a/b
#     print(wynik)
# except ZeroDivisionError:
#     print("nie można dzielić przez 0")
# except ValueError:
#     print('nie wczytano liczby całkowitej')
#
#
# do listy:
# append, insert, extand - dodawanie
# pop, remove, del - usuwanie
# sort, reverse - sortowanie listy(tylko z liczbami)
#
#Jak dodać nowy element do slownika??????

# lista = ['a', 5, 5.5, [1,2,3]]
# słownik={'klucz':'wartość',1:30}
# #a=lista[nr_indeksu]
# print(słownik)
# print(słownik[1])
