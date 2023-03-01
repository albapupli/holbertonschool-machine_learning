#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

people = np.array(["Farrah", "Fred", "Felicia"])
w = 0.5
apple = np.array([fruit, fruit, fruit, fruit])
banana = np.array([fruit, fruit, fruit, fruit])
peach = np.array([fruit, fruit, fruit, fruit])
orange = np.array([fruit, fruit, fruit, fruit])

fig, ax = plt.subplots()
bottom = np.zeros(3)


plt.bar(people, apple, color = 'r')
plt.bar(people, banana, bottom=apple, color='y')
plt.bar(people, orange, bottom=apple+banana, color='#ff8000')
plt.bar(people, peach, bottom=apple+banana+orange, color='#ffe5b4')
#plt.xlabel("Teams")
plt.ylabel("Quantity of Fruit")
plt.legend(["apples", "bananas", "oranges", "peaches"])
plt.title("Number of Fruit per Person")
plt.show()
