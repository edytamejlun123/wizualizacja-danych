import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()

# ts.plot()
# plt.show()

# dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']}
#
# df = pd.DataFrame(dane)
#
# grupa = df.groupby('Kontynent').agg({'Populacja': ['sum']})
# print(grupa)
# # grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Populacja w mld',
# #            rot=0, title='Populacja dla kontynentów')
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynent')
# wykres.set_ylabel('Populacja w mld')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja na kotynentach')
# plt.savefig('wykres.png')
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
#
# grupa = df.groupby('Imię i nazwisko').agg(
#     {'Wartość zamówienia': ['sum']})
#
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
#            fontsize=20, figsize=(8,8), colors=['red', 'green'])
# plt.legend(loc='upper left')
# plt.show()

# df = pd.DataFrame(ts)
# print(df)
#
# df['Średnia krocząca'] = df.rolling(window=100).mean()
# df.plot()
# plt.legend(['Wartości', 'Średnia z n-elementów'])
# plt.show()

# #Zad. 1
# dzieci = {'Rok': [2001, 2002, 2003, 2004, 2005, 2006],
#         'Ilość': [1234, 2332, 2234, 1221, 2223, 3432]}
# df = pd.DataFrame(dzieci)
#
# grupa = df.groupby('Rok').agg({'Ilość': ['sum']})
# print(grupa)
# grupa.plot(kind='bar', xlabel='Rok', ylabel='Ilość',
#            rot=0, title='Liczba Urodzonych Dzieci')
# plt.show()
#ZAD.1
# df = pd.read_excel('imiona.xlsx')
# df.head()
#
# print(df)
#
# grupa = df.groupby('Rok').agg({'Liczba': ['sum']})
# print(grupa)
# grupa.plot(kind='line', xlabel='Rok', ylabel='Ilość')
# plt.show()

# #ZAD.2
# df = pd.read_excel('imiona.xlsx')
#
# print(df)
# grupa = df.groupby('Plec').agg({'Liczba': ['sum']})
# print(grupa)
# grupa.plot(kind='bar', xlabel = 'Plec', ylabel = 'ilosc')
# plt.show()

#ZAD.3

#zad.4
