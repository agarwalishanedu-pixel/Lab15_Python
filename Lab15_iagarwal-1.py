"""
Program Name: Lab 15
My name: Ishan Agarwal
Purpose: The purpose of this program is to understand how to generate data and visualize it using python 
Date: 05/03/2026
"""

import matplotlib.pyplot as plt

#First Part
ind_var1 = [1, 2, 3, 4, 5]
dep_var1 = [1, 8, 27, 64, 125]

figure, graph1 = plt.subplots()
graph1.plot(ind_var1, dep_var1, linewidth = 3, color = 'blue')
graph1.set_title('First 5 Cubes', fontsize = 24, loc = 'center')
graph1.set_xlabel('Values', fontsize = 14)
graph1.set_ylabel('Cubed Values', fontsize = 14)

#Saving the figure
plt.savefig ("cubes_5.png", bbox_inches = 'tight', pad_inches = 0.5)