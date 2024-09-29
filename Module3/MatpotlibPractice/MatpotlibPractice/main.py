from matplotlib import pyplot as plt

x = [1, 2, 3]

y1 = [10, 20, 30]

y2 = [0, 5, 15]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, y1, color = 'g')
ax1.plot(x, y2, color='b')

ax1.set_xlabel('Year')
ax1.set_ylabel('Bitcoin', color = 'g')
ax2.set_ylabel('Gold', color = 'b')

plt.show()