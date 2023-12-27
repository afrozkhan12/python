import matplotlib.pyplot as plt

# Line chart
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Bar graph
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [20, 35, 30, 15]

plt.bar(categories, values)
plt.title('Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()