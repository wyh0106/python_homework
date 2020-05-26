import matplotlib.pyplot as plt

squares = list(range(2000))

for i in squares:
	squares[i] *= squares[i]

plt.scatter(range(2000),squares,color = 'purple')
plt.title("Square number", fontsize = 18)
plt.xlabel("Value", fontsize = 16)
plt.ylabel("Square of value", fontsize = 16)

plt.tick_params(axis = 'both', labelsize = 14)
plt.show()