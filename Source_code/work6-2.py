import matplotlib.pyplot as plt
import numpy as np
import csv

FileName = 'resource\\weather.csv'

with open(FileName) as File:
	reader = csv.reader(File)
	header_row = next(reader)
	print(header_row) 
