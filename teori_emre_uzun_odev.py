import math as m
import numpy as np
import matplotlib.pyplot as plt

a = 0
t_liste = list()
for i in range(50):
    t_liste.append(a)
    a += 0.01

liste_x_t_1 = list()
liste_x_t_2 = list()
a = np.csingle((-1)**(1/2))

for t in t_liste:
    x_t_1 = (0.1033*m.sin(9.67*t)) + (1.23*(10**-4)/a) * (m.sin(9.047*a*t))
    x_t_2 = (-3.454)*(10**-3)*(m.sin(9.67*t)) + (3.7*(10**-3/2)/a) * (m.sin(9.047*a*t))
    
    liste_x_t_1.append(x_t_1)
    liste_x_t_2.append(x_t_2)
plt.figure(figsize = (8,6))

plt.subplot(2,2,1)
plt.plot(t_liste, liste_x_t_1)
plt.xlabel("Time[s]")
plt.ylabel("X(t)")
plt.title("X(t) vs Time")

plt.subplot(2,2,2)
plt.plot(t_liste, liste_x_t_2)
plt.xlabel("Time[s]")
plt.ylabel("X(t)")
plt.title("X(t) vs Time")


plt.figure(figsize=(8,6))
plt.plot(t_liste, liste_x_t_1)
plt.plot(t_liste, liste_x_t_2)
plt.xlabel("Time[s]")
plt.ylabel("X(t)")
plt.title("X(t) vs Time")
plt.show()