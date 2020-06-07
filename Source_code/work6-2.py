import matplotlib.pyplot as plt
import numpy as np
import csv

FileName = 'resource\\weather.csv'

with open(FileName) as File:
	reader = csv.reader(File)
	header_row = next(reader)
	
	# for index, column_h in enumerate(header_row):
	# 	print(index, column_h)

	highs = []
	for row in reader:
		highs.append(int(row[1]))

fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(highs, linestyle = '-.', marker = '.', color = 'coral')

plt.title('Temperature', fontsize = 18)
plt.xlabel('', fontsize =14)
plt.ylabel("(F)", fontsize = 14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 12)
plt.grid(True)

plt.show()

