#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig = plt.figure(figsize=(6, 6), layout="constrained")
spec = fig.add_gridspec(3, 2)

ax0 = fig.add_subplot(spec[0, 0])
ax0.plot(y0, 'r')

ax01 = fig.add_subplot(spec[0, 1])
ax01.scatter(x1, y1, c='m')
ax01.set_title("mens height vs weight")
ax01.set_xlabel("height (in)")
ax01.set_ylabel("weight (lbs)")

ax10 = fig.add_subplot(spec[1, 0])
ax10.plot(x2, y2)
ax10.set_xlabel("Time (years)")
ax10.set_ylabel("Fraction Remaining")
ax10.set_xlim(0, 28500)
ax10.set_yscale("log")
ax10.set_title("Exponential Decay of C-14")

ax11 = fig.add_subplot(spec[1, 1])
ax11.plot(x3, y31, 'r--', label='C-14')
ax11.plot(x3, y32, 'g', label='Ra-226')
ax11.set_xlim(0, 20000)
ax11.set_ylim(0, 1)
ax11.legend(loc=1)
ax11.set_xlabel("Time (years)")
ax11.set_ylabel("Fraction Remaining")
ax11.set_title("Exponential Decay of Radioactive Elements")

ax2 = fig.add_subplot(spec[2, :])
ax2.set_xlabel('Grades')
ax2.set_ylabel('Number of Students')
ax2.set_title('Project A')

fig.suptitle('All in One')
