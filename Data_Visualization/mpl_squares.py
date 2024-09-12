import matplotlib.pyplot as plt

##Data
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

##Ui, and visuals
plt.title("tims Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

##Ensure Integer, and not Float
plt.tick_params(axis='both', labelsize=14)

##Show the Graph
plt.show()