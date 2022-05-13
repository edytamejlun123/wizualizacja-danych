import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# plt.plot([1,2,3,4])
# plt.ylabel('jakieś liczby')
# plt.show()
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
# plt.axis([0, 6, 0, 20])
# plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
# # plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
# # plt.axis([0, 6, 0, 20])
# # plt.show()

# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
# plt.show()

x = np.linspace(0, 2, 100)
plt.plot(x, x, label="liniowa")
plt.plot(x, x**2, label="kwadratowa")
plt.plot(x, x**3, label="sześcienna")
plt.xlabel('etykieta x')
plt.ylabel("etykieta y")
plt.title("Prosty wykres")
plt.legend()
plt.savefig('wykres matplot.png')
plt.show()
im1 = Image.open('wykres matplot.png')
im1 = im1.convert('RGB')
im1.save('nowy.jpg')