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

fig, ((ax1, ax2), (ax3, ax4), (ax5)) = plt.subplot(3, 2)
fig.suptitle('All in one')
fig.rc('font', size=X-SMALL)
#1st graph
ax1.plot(y0, 'r')
ax1.show()

#2nd graph
ax2.scatter(x1, y1, c='m')
ax2.title("mens height vs weight")
ax2.xlabel("height")
ax2.ylabel("weight")
ax2.show()

#3rd graph
ax3.plot(x2, y2)
ax3.xlabel("x")
ax3.ylabel("y")
ax3.xlim(0, 28500)
ax3.yscale("log")
ax3.show()

#4th graph
ax4.plot(x3, y31, 'r--', label='C-14')
ax4.plot(x3, y32, 'g', label='Ra-226')
ax4.xlim(0, 20000)
ax4.ylim(0, 1)
ax4.legend(loc=1)
ax4.show()

#5th graph
ax5.xlabel('Grades')
ax5.ylabel('Number of Students')
ax5.title('Project A')
ax5.hist(student_grades, bins=10)
ax5.show()
