import matplotlib.pyplot as plt

##Data
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

##Title
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Ensure Int not float
plt.tick_params(axis='both', which='major', labelsize=14)

##Range

plt.axis([0,1100,0,1100000])


##Saves Pic of graph, Deletes white space
plt.savefig('Squares_plot.png', bbox_inches='tight')