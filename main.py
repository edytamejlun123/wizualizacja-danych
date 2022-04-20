import numpy as np

# #Zad. 1
# a = np.array([2,4,3])
# b = np.array([1,2,1])
# c = a.dot(b)
# print(c)

# #Zad. 2
# a = np.arange(9).reshape(3,3)
# b = np.arange(16).reshape(4,4)
# print(a)
# print(b)

# x = a[:,0]
# y = a[:,1]
# z = a[:,2]
# print('kolumna1: ')
# print(min(x))
# print('kolumna2: ')
# print(min(y))
# print('kolumna3: ')
# print(min(z))

# #Zad.3
# d = b*a
# print(d)

# #Zad. 4
# A = np.array([[1, 3, 5]])
# print(A)
# B = np.array([[1.2, 3.5, 5.2]])
# print(B)
# c = A*B
# print(c)

#Zad. 5
# macierz = np.arange(6).reshape(2,3)
# a = np.sin(macierz)
# print(macierz)
# print(a)

# #Zad.6
# macierz = np.arange(6).reshape(2,3)
# b = np.cos(macierz)
# print(macierz)
# print(b)

#Zad. 7
# c = a+b
# print(c)

#Zad. 8
m = np.arange(9).reshape(3,3)
for i in m:
    print(i[2])