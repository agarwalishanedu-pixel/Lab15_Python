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

#Creating the graph itself
figure, graph1 = plt.subplots()
graph1.plot(ind_var1, dep_var1, linewidth = 3, color = 'blue')
graph1.set_title('First 5 Cubes', fontsize = 24, loc = 'center')
graph1.set_xlabel('Values', fontsize = 14)
graph1.set_ylabel('Cubed Values', fontsize = 14)

#Save graph 1
plt.savefig ("cubes_5.png", bbox_inches = 'tight', pad_inches = 0.5)

plt.close()

#-------------------------------------

#Second Part
ind_var2 = list(range(1,5001))
dep_var2 = [x**3 for x in ind_var2]

#Create graph itself
figure, graph2 = plt.subplots()
graph2.plot(ind_var2, dep_var2, linewidth = 3, color = 'blue')

graph2.set_title('First 5000 Cubes', fontsize = 24, loc = 'center')
graph2.set_xlabel('Values', fontsize = 14)
graph2.set_ylabel('Cubed Values', fontsize = 14)

#Save graph 2
plt.savefig ("cubes_5000.png", bbox_inches = 'tight', pad_inches = 0.5)

plt.close()