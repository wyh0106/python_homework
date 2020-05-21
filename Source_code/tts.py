import matplotlib.pyplot as plt

labels = 'frogs', 'hogs', 'dogs', 'logs'
sizes = 30, 20, 40, 10
colors = 'purple', 'gold', 'lightskyblue', 'lightcoral'
explode = 0, 0.1, 0, 0
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
plt.axis('equal')
plt.show()
