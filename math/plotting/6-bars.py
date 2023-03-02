#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

people = ["Farrah", "Fred", "Felicia"]
fruit_names = {
    'apples': 'red',
    'bananas': 'yellow',
    'oranges': '#ff8000',
    'peaches': '#ffe5b4'}
i = 0

for name, color in sorted(fruit_names.items()):
    bottom_start = 0
    for j in range(i):
        bottom_start += fruit[j]
    plt.bar(
        x=np.arange(len(people)),
        height=fruit[i],
        width=0.5,
        bottom=bottom_start,
        color=color,
        label=name)
    i += 1

plt.bar
plt.xticks(np.arange(len(people)), people)
plt.yticks(np.arange(0, 81, 10))
plt.ylabel('Quantity of Fruit')
plt.title("Number of Fruit per Person")
plt.legend()
plt.show()
