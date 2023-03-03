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
fig = plt.figure(figsize=(12, 8))
ax0 = fig.add_subplot(3, 2, 1)
ax0.plot(y0, 'r')
ax0.set_xlim((0, 10))
ax01 = fig.add_subplot(3, 2, 2)
ax01.scatter(x1, y1, c='m')
ax01.set_title("mens height vs weight", fontsize = 'x-small')
ax01.set_xlabel("height (in)", fontsize = 'x-small')
ax01.set_ylabel("weight (lbs)", fontsize = 'x-small')
ax10 = fig.add_subplot(3, 2, 3)
ax10.plot(x2, y2)
ax10.set_xlabel("Time (years)", fontsize = 'x-small')
ax10.set_ylabel("Fraction Remaining", fontsize = 'x-small')
ax10.set_xlim(0, 28500)
ax10.set_yscale("log")
ax10.set_title("Exponential Decay of C-14", fontsize = 'x-small')
ax11 = fig.add_subplot(3, 2, 4)
ax11.plot(x3, y31, 'r--', label='C-14')
ax11.plot(x3, y32, 'g', label='Ra-226')
ax11.set_xlim((0, 20000))
ax11.set_ylim((0, 1))
ax11.legend()
ax11.set_xlabel("Time (years)", fontsize = 'x-small')
ax11.set_ylabel("Fraction Remaining", fontsize = 'x-small')
ax11.set_title("Exponential Decay of Radioactive Elements", fontsize = 'x-small')
ax2 = fig.add_subplot(3, 1, 3)
ax2.hist(student_grades, bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], edgecolor = 'black')
ax2.set_xlabel('Grades', fontsize = 'x-small')
ax2.set_ylabel('Number of Students', fontsize = 'x-small')
ax2.set_title('Project A', fontsize = 'x-small')
ax2.set_xlim((0, 100))
ax2.set_xticks(np.arange(0, 101, 10))
ax2.set_ylim((0, 30))
fig.suptitle('All in One')
plt.tight_layout()
plt.show()
