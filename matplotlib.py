import matplotlib.pyplot as plt 


# data to display on plots 
x = [3, 1, 3] 
y = [3, 2, 1] 

# This will plot a simple line chart
# with elements of x as x axis and y
# as y axis
plt.plot(x, y)
plt.title("Line Chart")

# Adding the legends
plt.legend(["Line"])
plt.show()


###
x = np.linspace(0.1, 2 * np.pi, 41) 
y = np.exp(np.sin(x)) 

plt.stem(x, y, use_line_collection = True) 
plt.show() 


###
# This will plot a simple bar chart
plt.bar(x, y)

# Title to the plot
plt.title("Bar Chart")

# Adding the legends
plt.legend(["bar"])
plt.show()


###
# data to display on plots 
x = [1, 2, 3, 4, 5, 6, 7, 4] 

# This will plot a simple histogram
plt.hist(x, bins = [1, 2, 3, 4, 5, 6, 7])

# Title to the plot
plt.title("Histogram")

# Adding the legends
plt.legend(["bar"])
plt.show()


###
# This will plot a simple scatter chart
plt.scatter(x, y)

# Adding legend to the plot
plt.legend("A")

# Title to the plot
plt.title("Scatter chart")
plt.show()


###
# List of Days
days = [1, 2, 3, 4, 5]

# No of Study Hours
Studying = [7, 8, 6, 11, 7]

# No of Playing Hours
playing = [8, 5, 7, 8, 13]

# Stackplot with X, Y, colors value
plt.stackplot(days, Studying, playing,
            colors =['r', 'c'])

# Days
plt.xlabel('Days')

# No of hours
plt.ylabel('No of Hours')

# Title of Graph
plt.title('Representation of Study and \
Playing wrt to Days')

# Displaying Graph
plt.show()



###
# Creating dataset
np.random.seed(10)
data = np.random.normal(100, 20, 200)

fig = plt.figure(figsize =(10, 7))

# Creating plot
plt.boxplot(data)

# show plot
plt.show()


###
e  =(0.1, 0, 0, 0)

# This will plot a simple pie chart
plt.pie(x, explode = e)

# Title to the plot
plt.title("Pie chart")
plt.show()


###
# making a simple plot
x =[1, 2, 3, 4, 5, 6, 7]
y =[1, 2, 1, 2, 1, 2, 1]

# creating error
y_error = 0.2

# plotting graph
plt.plot(x, y)

plt.errorbar(x, y,
            yerr = y_error,
            fmt ='o')



###
# creating a list of 
# uniformly distributed values 
uniform = np.arange(-100, 100) 

# creating a list of normally 
# distributed values 
normal = np.random.normal(size = 100)*30

# creating figure and axes to 
# plot the image 
fig, (ax1, ax2) = plt.subplots(nrows = 1, 
                            ncols = 2, 
                            figsize =(9, 4), 
                            sharey = True) 

# plotting violin plot for 
# uniform distribution 
ax1.set_title('Uniform Distribution') 
ax1.set_ylabel('Observed values') 
ax1.violinplot(uniform) 

# plotting violin plot for 
# normal distribution 
ax2.set_title('Normal Distribution') 
ax2.violinplot(normal) 

# Function to show the plot 
plt.show() 


###
# Creating the figure object
fig = plt.figure()

# keeping the projection = 3d
# creates the 3d plot
ax = plt.axes(projection = '3d')


###
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
z = [1, 8, 27, 64, 125]
# Creating the figure object
fig = plt.figure()
# keeping the projection = 3d
# creates the 3d plot
ax = plt.axes(projection = '3d')
ax.plot3D(z, y, x)

